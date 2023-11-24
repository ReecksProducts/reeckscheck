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
    # Открываем лог-файл для добавления (mode='a') с использованием utf-8
    with open(log_file, 'a', encoding='utf-8', errors='replace') as log:
        # Выводим сообщение о начале поиска в консоль и добавляем его в лог
        message = "Идет поиск файлов - подождите, пожалуйста..."
        print(message)
        log.write(message + '\n')

        for root_path in root_paths:
            # Проходим по всем файлам и подкаталогам в указанном каталоге
            for root, dirs, files in os.walk(root_path):
                # Проверяем, содержится ли хотя бы одно из заданных имен в имени файла (без учета регистра)
                for file in files:
                    for target_name in target_names:
                        if target_name.lower() in file.lower():
                            file_path = os.path.join(root, file)
                            # Выводим сообщение в консоль и добавляем его в лог
                            message = f"{target_name} » Найден файл с именем '{file}' по пути: {file_path}"
                            print(message)
                            log.write(message + '\n')


# Указываем диски, на которых будет выполняться поиск
root_paths = ["C:\\", "D:\\"]

# Указываем имена файлов для поиска
target_names = ["Impact", "Aristois", "XRAY", "Wurst",
                "Hack", "Baritone", "Fabritone", "Inertia", "Celestial", "Expensive", "Gumbaloff", "Recode", "celka", "Ares", "Sigmaclient", "Salhack", "KAMI", "WWE", "SkillClient", "Liquid Bounce", "Matix"]

# Указываем имя лог-файла
log_file = "log.txt"

# Вызываем функцию для поиска на указанных дисках
search_files_with_names(root_paths, target_names, log_file)


print("⚠ Проверка окончена ⚠")
print("⚠ Закрытие через 3 секунды ⚠")
time.sleep(3)
print("██████╗ ██████╗  ██████╗ ██████╗ ███████╗██████╗ ██╗  ██╗ █████╗ ")
print("██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔══██╗")
print("██████╔╝██████╔╝██║   ██║██████╔╝█████╗  ██████╔╝█████╔╝ ███████║")
print("██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██╔══╝  ██╔═══╝ ██╔═██╗ ██╔══██║")
print("██║     ██║  ██║╚██████╔╝██████╔╝███████╗██║     ██║  ██╗██║  ██║")
print("╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝")
time.sleep(3)
