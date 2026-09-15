"""
CalculatorYakova — кроссплатформенный калькулятор на Kivy.
Поддерживает базовые арифметические операции, проценты,
удаление последнего символа и очистку.

Совместим с Android (через Buildozer), Linux, Windows, macOS.
"""

import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

# Минимальная ширина окна для комфортной работы на ПК
Window.minimum_width = 320
Window.minimum_height = 480


class CalculatorLayout(BoxLayout):
    """
    Корневой layout калькулятора.
    Вся визуальная структура описана в calculator.kv.
    Здесь — только логика ввода и вычислений.
    """

    # Текст, отображаемый на дисплее
    display_text = StringProperty("0")

    # Флаг: было ли только что выполнено вычисление
    # (нужен, чтобы следующая цифра начинала новое число)
    _just_calculated = False

    # Максимальная длина вводимого выражения
    MAX_LENGTH = 32

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # ── Ввод ──────────────────────────────────────────────

    def append_digit(self, digit: str) -> None:
        """Добавляет цифру или точку к текущему выражению."""
        current = self.display_text

        # После вычисления начинаем новое выражение
        if self._just_calculated:
            current = "0"
            self._just_calculated = False

        # Защита от ввода двух точек в одном числе
        if digit == ".":
            # Разбиваем по операторам и проверяем последнее число
            last_number = re.split(r"[+\-×÷%]", current)[-1]
            if "." in last_number:
                return

        # Если текущее значение — "0", заменяем его цифрой
        if current == "0" and digit != ".":
            new_text = digit
        else:
            new_text = current + digit

        # Проверка длины
        if len(new_text) > self.MAX_LENGTH:
            self.display_text = "Ошибка"
            self._just_calculated = True
            return

        self.display_text = new_text

    def append_operator(self, operator: str) -> None:
        """Добавляет арифметический оператор к выражению."""
        current = self.display_text

        if current == "Ошибка":
            return

        # После вычисления можно продолжить работу с результатом
        self._just_calculated = False

        # Не добавляем оператор сразу после другого оператора
        if current and current[-1] in "+-×÷%":
            # Заменяем последний оператор на новый
            self.display_text = current[:-1] + operator
        else:
            self.display_text = current + operator

    # ── Управление ────────────────────────────────────────

    def clear_display(self) -> None:
        """Полная очистка дисплея (кнопка C)."""
        self.display_text = "0"
        self._just_calculated = False

    def backspace(self) -> None:
        """Удаляет последний символ (кнопка ⌫)."""
        if self.display_text == "Ошибка":
            self.clear_display()
            return

        self._just_calculated = False
        new_text = self.display_text[:-1]

        if not new_text:
            new_text = "0"

        self.display_text = new_text

    def toggle_sign(self) -> None:
        """Меняет знак текущего числа на противоположный."""
        if self.display_text == "Ошибка":
            return

        current = self.display_text

        # Находим последнее число в выражении
        match = re.search(r"(\d+\.?\d*)$", current)
        if not match:
            return

        number_str = match.group(1)
        start = match.start(1)

        if number_str.startswith("-"):
            new_number = number_str[1:]
        else:
            new_number = "-" + number_str

        self.display_text = current[:start] + new_number

    # ── Вычисление ────────────────────────────────────────

    def calculate_result(self) -> None:
        """Вычисляет выражение и выводит результат."""
        expression = self.display_text

        if expression == "Ошибка" or not expression:
            return

        try:
            # Заменяем символы на понятные Python
            expr = expression.replace("×", "*").replace("÷", "/")

            # Обработка процентов: N% → N/100
            expr = re.sub(r"(\d+\.?\d*)%", r"(\1/100)", expr)

            # Безопасная проверка допустимых символов
            allowed = set("0123456789.+-*/() ")
            if not all(c in allowed for c in expr):
                raise ValueError("Недопустимые символы")

            # Вычисляем
            result = eval(expr, {"__builtins__": {}}, {})

            # Округляем до 10 знаков, убираем лишние нули
            result = round(result, 10)

            if result == int(result):
                result = int(result)

            self.display_text = str(result)
            self._just_calculated = True

        except ZeroDivisionError:
            self.display_text = "Ошибка"
            self._just_calculated = True
        except Exception:
            self.display_text = "Ошибка"
            self._just_calculated = True


class CalculatorYakovaApp(App):
    """Главный класс приложения."""

    def build(self):
        self.title = "CalculatorYakova"
        return CalculatorLayout()

    def on_pause(self):
        """Разрешает сворачивание на Android без перезапуска."""
        return True

    def on_resume(self):
        """Вызывается при возврате из свёрнутого состояния."""
        pass


if __name__ == "__main__":
    CalculatorYakovaApp().run()