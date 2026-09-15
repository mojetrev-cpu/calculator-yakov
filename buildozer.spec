[app]
# ── Основная информация о приложении ─────────────────────
title = CalculatorYakova
package.name = pycalculator
package.domain = org.example

# Исходный код находится в корне проекта
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
source.exclude_dirs = .buildozer,bin,venv,.venv,__pycache__

# ── Версия и ориентация ──────────────────────────────────
version = 1.0.0
orientation = portrait

# ── Python-зависимости ───────────────────────────────────
# ВАЖНО: для Android используем python3 и kivy.
# Версии фиксированы для стабильной сборки.
requirements = python3,kivy==2.3.1

# ── Иконка приложения ────────────────────────────────────
# Раскомментируйте, если добавите assets/icon.png (512x512)
# icon.filename = %(source.dir)s/assets/icon.png

# ── Android: разрешения ──────────────────────────────────
# Калькулятору сеть не нужна, поэтому INTERNET не запрашиваем.
# Если добавите экспорт истории или синхронизацию — добавьте:
# android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.permissions =

# ── Android: версии API и SDK ────────────────────────────
# Целевой API: 33 (Android 13) — актуально на 2026 год
android.api = 33
# Минимальный API: 21 (Android 5.0) — покрывает ~99% устройств
android.minapi = 21
# Целевой NDK
android.ndk = 25b
# Разрешаем AndroidX (современные библиотеки поддержки)
android.enable_androidx = True
# Отключаем старый support library
android.accept_sdk_license = True

# ── Android: архитектуры ─────────────────────────────────
# arm64-v8a — современные устройства (основная)
# armeabi-v7a — старые устройства (совместимость)
android.archs = arm64-v8a, armeabi-v7a

# ── p4a (python-for-android) ─────────────────────────────
# SDL2 — стандартный bootstrap для Kivy-приложений
p4a.bootstrap = sdl2
# Исключаем неиспользуемые модули — уменьшает размер APK
p4a.exclude_src = Lib/lib2to3, Lib/test, Lib/idlelib, Lib/bsddb, Lib/distutils, Lib/tkinter, Lib/turtledemo, Lib/ensurepip
# Уровень логирования p4a (1 = warn)
p4a.loglevel = 1

# ── Настройки отладки ────────────────────────────────────
# Раскомментируйте для отладки на устройстве через logcat:
# android.logcat_filters = *:S python:D
# android.debug = True

# ── Параметры сборки ─────────────────────────────────────
# Формат выходного файла: apk (для прямой установки)
# Для Google Play используйте: aab
android.artifact_format = apk
# Время ожидания сборки (секунды)
android.build_timeout = 3600

# ── Иконка и заставка (опционально) ──────────────────────
# presplash.filename = %(source.dir)s/assets/splash.png

# ── Подпись релизных сборок ──────────────────────────────
# Для debug-сборок подпись не требуется.
# Для release раскомментируйте и укажите путь к keystore:
# android.release_artifact = apk
# android.keystore = /path/to/your.keystore
# android.keystore_passwd = your_password
# android.keyalias = your_alias
# android.keyalias_passwd = your_alias_password

[buildozer]
# Уровень логирования Buildozer (1 = warn, 2 = info)
log_level = 2
# Разрешить сборку от root (не рекомендуется, но иногда нужно в Docker/CI)
warn_on_root = 0