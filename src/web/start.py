import os
import time

print("")
print("███████╗██╗██████╗ ███████╗    ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ ")
print("██╔════╝██║██╔══██╗██╔════╝    ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗")
print("█████╗  ██║██████╔╝█████╗      ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║")
print("██╔══╝  ██║██╔══██╗██╔══╝      ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║")
print("██║     ██║██║  ██║███████╗    ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝")
print("╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ")
print("Программа для проверки на сервере fireworld.servop.ru by ReecksJres")
print("Начало через 5 секунд")
time.sleep(5)
print("⚠ Ищем Impact... (Может занять некоторое время)")
time.sleep(3)


def search_files_with_impact(target_string="Impact"):
    # Получаем список всех дисков
    drives = [d for d in os.listdir(
        '/') if os.path.isdir(os.path.join('/', d))]

    # Проходим по каждому диску и выполняем поиск
    for drive in drives:
        root_path = os.path.join('/', drive)
        search_files_in_drive(root_path, target_string)


def search_files_in_drive(root_path, target_string):
    # Проходим по всем файлам и подкаталогам в указанном каталоге
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Проверяем, содержится ли строка "Impact" в имени файла (без учета регистра)
            if target_string.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(
                    f"Impact » ⚠ Найден файл с именем '{file}' по пути: {file_path}")


# Вызываем функцию для поиска на всех дисках
search_files_with_impact()

print("⚠ Ищем Aristois... (Может занять некоторое время)")
time.sleep(3)


def search_files_with_aristois(target_string="Aristois"):
    # Получаем список всех дисков
    drives = [d for d in os.listdir(
        '/') if os.path.isdir(os.path.join('/', d))]

    # Проходим по каждому диску и выполняем поиск
    for drive in drives:
        root_path = os.path.join('/', drive)
        search_files_in_drives(root_path, target_string)


def search_files_in_drives(root_path, target_string):
    # Проходим по всем файлам и подкаталогам в указанном каталоге
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Проверяем, содержится ли строка "Impact" в имени файла (без учета регистра)
            if target_string.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(
                    f"Aristois »⚠ Найден файл с именем '{file}' по пути: {file_path} ⚠")


# Вызываем функцию для поиска на всех дисках
search_files_with_aristois()

print("⚠ Ищем XRAY... (Может занять некоторое время)")
time.sleep(3)


def search_files_with_xray(target_string="Xray"):
    # Получаем список всех дисков
    drives = [d for d in os.listdir(
        '/') if os.path.isdir(os.path.join('/', d))]

    # Проходим по каждому диску и выполняем поиск
    for drive in drives:
        root_path = os.path.join('/', drive)
        search_files_in_drivess(root_path, target_string)


def search_files_in_drivess(root_path, target_string):
    # Проходим по всем файлам и подкаталогам в указанном каталоге
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Проверяем, содержится ли строка "Impact" в имени файла (без учета регистра)
            if target_string.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(
                    f"Xray » ⚠ Найден файл с именем '{file}' по пути: {file_path} ⚠")


# Вызываем функцию для поиска на всех дисках
search_files_with_xray()

print("⚠ Ищем Wurst... (Может занять некоторое время)")
time.sleep(3)


def search_files_with_wurst(target_string="Wurst"):
    # Получаем список всех дисков
    drives = [d for d in os.listdir(
        '/') if os.path.isdir(os.path.join('/', d))]

    # Проходим по каждому диску и выполняем поиск
    for drive in drives:
        root_path = os.path.join('/', drive)
        search_files_in_drivesss(root_path, target_string)


def search_files_in_drivesss(root_path, target_string):
    # Проходим по всем файлам и подкаталогам в указанном каталоге
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Проверяем, содержится ли строка "Impact" в имени файла (без учета регистра)
            if target_string.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(
                    f"Wurst » ⚠ Найден файл с именем '{file}' по пути: {file_path} ⚠")


# Вызываем функцию для поиска на всех дисках
search_files_with_wurst()

print("⚠ Ищем BleachHack... (Может занять некоторое время)")
time.sleep(3)


def search_files_with_blc(target_string="BleachHack"):
    # Получаем список всех дисков
    drives = [d for d in os.listdir(
        '/') if os.path.isdir(os.path.join('/', d))]

    # Проходим по каждому диску и выполняем поиск
    for drive in drives:
        root_path = os.path.join('/', drive)
        search_files_in_drivessss(root_path, target_string)


def search_files_in_drivessss(root_path, target_string):
    # Проходим по всем файлам и подкаталогам в указанном каталоге
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Проверяем, содержится ли строка "Impact" в имени файла (без учета регистра)
            if target_string.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(
                    f"BleachHack » ⚠ Найден файл с именем '{file}' по пути: {file_path} ⚠")


# Вызываем функцию для поиска на всех дисках
search_files_with_blc()

print("⚠ Ищем Baritone... (Может занять некоторое время)")
time.sleep(3)


def search_files_with_brt(target_string="Baritone"):
    # Получаем список всех дисков
    drives = [d for d in os.listdir(
        '/') if os.path.isdir(os.path.join('/', d))]

    # Проходим по каждому диску и выполняем поиск
    for drive in drives:
        root_path = os.path.join('/', drive)
        search_files_in_drivesssss(root_path, target_string)


def search_files_in_drivesssss(root_path, target_string):
    # Проходим по всем файлам и подкаталогам в указанном каталоге
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Проверяем, содержится ли строка "Impact" в имени файла (без учета регистра)
            if target_string.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(
                    f"Barritone » ⚠ Найден файл с именем '{file}' по пути: {file_path} ⚠")


# Вызываем функцию для поиска на всех дисках
search_files_with_brt()

print("⚠ Ищем Inertia... (Может занять некоторое время)")
time.sleep(3)


def search_files_with_inr(target_string="Inertia"):
    # Получаем список всех дисков
    drives = [d for d in os.listdir(
        '/') if os.path.isdir(os.path.join('/', d))]

    # Проходим по каждому диску и выполняем поиск
    for drive in drives:
        root_path = os.path.join('/', drive)
        search_files_in_drivessssss(root_path, target_string)


def search_files_in_drivessssss(root_path, target_string):
    # Проходим по всем файлам и подкаталогам в указанном каталоге
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Проверяем, содержится ли строка "Impact" в имени файла (без учета регистра)
            if target_string.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(
                    f"Inertia » ⚠ Найден файл с именем '{file}' по пути: {file_path} ⚠")


search_files_with_inr()

print("⚠ Ищем Celestial... (Может занять некоторое время)")
time.sleep(3)


def search_files_with_cel(target_string="Celestial"):
    # Получаем список всех дисков
    drives = [d for d in os.listdir(
        '/') if os.path.isdir(os.path.join('/', d))]

    # Проходим по каждому диску и выполняем поиск
    for drive in drives:
        root_path = os.path.join('/', drive)
        search_files_in_drivesssssss(root_path, target_string)


def search_files_in_drivesssssss(root_path, target_string):
    # Проходим по всем файлам и подкаталогам в указанном каталоге
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Проверяем, содержится ли строка "Impact" в имени файла (без учета регистра)
            if target_string.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(
                    f"Celestial » ⚠ Найден файл с именем '{file}' по пути: {file_path} ⚠")


# Вызываем функцию для поиска на всех дисках
search_files_with_cel()

# Вызываем функцию для поиска на всех дисках


print("⚠ Проверка окончена ⚠")
print("⚠ Закрытие через 5 секунд ⚠")
time.sleep(5)
print("██████╗ ██████╗  ██████╗ ██████╗ ███████╗██████╗ ██╗  ██╗ █████╗ ")
print("██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔══██╗")
print("██████╔╝██████╔╝██║   ██║██████╔╝█████╗  ██████╔╝█████╔╝ ███████║")
print("██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██╔══╝  ██╔═══╝ ██╔═██╗ ██╔══██║")
print("██║     ██║  ██║╚██████╔╝██████╔╝███████╗██║     ██║  ██╗██║  ██║")
print("╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝")
time.sleep(3)
