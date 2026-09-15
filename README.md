# CalculatorYakova

Кроссплатформенный калькулятор на Python + Kivy с поддержкой Android, Linux, Windows и macOS.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Kivy](https://img.shields.io/badge/Kivy-2.3.1-green)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Описание

**CalculatorYakova** — это лёгкий и адаптивный калькулятор, написанный на Python с использованием фреймворка **Kivy**. Приложение одинаково хорошо работает как на сенсорных экранах смартфонов, так и на десктопных мониторах.

### Возможности

- ✅ Базовые арифметические операции: сложение, вычитание, умножение, деление
- ✅ Работа с процентами (`%`)
- ✅ Смена знака числа (`+/-`)
- ✅ Удаление последнего символа (`⌫`)
- ✅ Полная очистка (`C`)
- ✅ Обработка ошибок: деление на ноль, переполнение ввода
- ✅ Адаптивный интерфейс — крупные кнопки, чёткий дисплей
- ✅ Поддержка портретной ориентации на мобильных устройствах

---

## 🛠 Стек технологий

| Компонент | Версия | Назначение |
|-----------|--------|------------|
| Python | 3.10+ | Язык разработки |
| Kivy | 2.3.1 | Кроссплатформенный UI-фреймворк |
| Buildozer | 1.5.0 | Сборка APK для Android |
| Cython | 0.29.36 | Компиляция Python-кода для Android |

---

## 🚀 Локальный запуск

### Предварительные требования

- **Python 3.10 или выше** — [скачать](https://www.python.org/downloads/)
- **pip** — менеджер пакетов Python
- **Git** — для клонирования репозитория

### Пошаговая инструкция

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/your-username/CalculatorYakova.git
cd CalculatorYakova

# 2. Создайте виртуальное окружение
python -m venv venv

# Активация:
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Запустите приложение
python main.py
```

После запуска откроется окно калькулятора. На ПК окно можно масштабировать — интерфейс адаптируется автоматически.

---

## 📱 Сборка APK для Android

> **Важно:** сборка APK возможна только на **Linux** или **macOS**. На Windows используйте **WSL 2** (Windows Subsystem for Linux) или Docker.

### Шаг 1: Установка системных зависимостей

```bash
sudo apt update
sudo apt install -y \
    python3-pip python3-setuptools python3-virtualenv \
    git zip unzip openjdk-17-jdk \
    autoconf libtool pkg-config zlib1g-dev \
    libncurses5-dev libncursesw5-dev libtinfo6 \
    cmake libffi-dev libssl-dev
```

### Шаг 2: Установка Buildozer

```bash
pip install buildozer cython
```

### Шаг 3: Инициализация проекта (если `buildozer.spec` отсутствует)

```bash
buildozer init
```

> В нашем проекте `buildozer.spec` **уже включён** в репозиторий. Проверьте, что параметры `title`, `package.name` и `requirements` соответствуют вашим ожиданиям.

### Шаг 4: Сборка APK

```bash
# Debug-сборка (для тестирования, не требует подписи)
buildozer -v android debug
```

Первый запуск займёт **30–60 минут** — Buildozer скачает Android SDK, NDK и скомпилирует Python для Android. Последующие сборки будут значительно быстрее.

### Шаг 5: Готовый APK

После успешной сборки файл появится в:

```
bin/pycalculator-1.0.0-debug.apk
```

### Шаг 6: Установка на устройство

```bash
# Подключите Android-устройство по USB с включённой отладкой
adb install bin/pycalculator-1.0.0-debug.apk
```

Или скопируйте APK на телефон и установите вручную (разрешите установку из неизвестных источников).

---

## 🔧 Частые проблемы при сборке

| Проблема | Решение |
|----------|---------|
| `Command failed: ... sdkmanager` | Установите JDK 17 и убедитесь, что `JAVA_HOME` указывает на него |
| Сборка падает на `cython` | Зафиксируйте версию: `pip install cython==0.29.36` |
| `ModuleNotFoundError: No module named '_ctypes'` | Установите `libffi-dev` и пересоберите |
| APK не устанавливается | Включите «Установка из неизвестных источников» в настройках Android |

---

## 📁 Структура проекта

```
CalculatorYakova/
├── main.py              # Логика приложения
├── calculator.kv        # UI на языке Kv
├── requirements.txt     # Python-зависимости
├── buildozer.spec       # Конфигурация сборки Android
├── .gitignore           # Исключения Git
├── README.md            # Этот файл
└── assets/
    └── icon.png         # Иконка (опционально)
```

---

## 📄 Лицензия

Проект распространяется под лицензией **MIT**. Подробности — в файле `LICENSE`.

---

## 👤 Автор

**Yakova** — [GitHub](https://github.com/your-username)

---

## ⭐ Поддержка

Если проект оказался полезным — поставьте ⭐ на GitHub! Это мотивирует развивать проект дальше.