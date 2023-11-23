import os
import sys
import time

print("")
print("██████╗ ███████╗███████╗ ██████╗██╗  ██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗")
print("██╔══██╗██╔════╝██╔════╝██╔════╝██║ ██╔╝██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝")
print("██████╔╝█████╗  █████╗  ██║     █████╔╝ ███████╗    ██║     ███████║█████╗  ██║     █████╔╝ ")
print("██╔══██╗██╔══╝  ██╔══╝  ██║     ██╔═██╗ ╚════██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ")
print("██║  ██║███████╗███████╗╚██████╗██║  ██╗███████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗")
print("╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝")
print("Программа для проверки на читы by ReecksJres")
print("Начало через 5 секунд")
time.sleep(5)


def search_files_with_names(root_paths, target_names, log_file):
    # Выводим сообщение о начале поиска
    print("Идет поиск файлов - подождите, пожалуйста...")

    # Записываем сообщение в лог-файл
    with open(log_file, 'a', encoding='utf-8', errors='replace') as log:
        log.write("Идет поиск файлов - подождите, пожалуйста...\n")

    for root_path in root_paths:
        # Проходим по всем файлам и подкаталогам в указанном каталоге
        for root, dirs, files in os.walk(root_path):
            # Проверяем, содержится ли хотя бы одно из заданных имен в имени файла (без учета регистра)
            for file in files:
                for target_name in target_names:
                    if target_name.lower() in file.lower():
                        file_path = os.path.join(root, file)
                        message = f"{target_name} » Найден файл с именем '{file}' по пути: {file_path}\n"

                        # Выводим сообщение в консоль
                        print(message)

                        # Записываем сообщение в лог-файл
                        with open(log_file, 'a', encoding='utf-8', errors='replace') as log:
                            log.write(message)


# Указываем диски, на которых будет выполняться поиск
root_paths = ["C:\\", "D:\\"]

# Указываем имена файлов для поиска
target_names = ["Impact", "Aristois", "XRAY", "Wurst",
                "Hack", "Baritone", "Fabritone", "Inertia", "Celestial", "Sigma", "Expensive", "Gumbaloff", "Recode", "celka"]

# Указываем имя лог-файла
log_file = "log.txt"

# Перенаправляем стандартный вывод в файл
sys.stdout = open(log_file, 'a', encoding='utf-8', errors='replace')

# Вызываем функцию для поиска на указанных дисках
search_files_with_names(root_paths, target_names, log_file)

# Восстанавливаем стандартный вывод
sys.stdout = sys.__stdout__


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
