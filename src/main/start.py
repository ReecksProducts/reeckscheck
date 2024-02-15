import os
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# Список ключевых слов
keywords_list = ["Impact", "Aristois", "Xray", "Wurst", "Hack", "Baritone", "Fabritone", "Inertia", "Celestial", "Expensive", "Gumbaloff", "celka", "Ares", "Sigmaclient", "Salhack", "KAMI", "WWE", "SkillClient",
                 "Liquid Bounce", "Matix", "FATAL", "ZAMO", "NEVERHOOK", "Flux", "Xatz", "Exist", "AVALON", "DEADCODE", "Nursultan", "Boze", "EXCELLENT", "Wild", "Calestial", "X-ray", "XRAY", "xray", "cheats", "cheat", "autoclicker"]


def search_files(keywords):
    results_list.delete(0, tk.END)
    found_items = 0
    for drive in range(ord('A'), ord('Z')+1):
        drive_letter = chr(drive)
        root_path = f"{drive_letter}:\\"
        if os.path.exists(root_path):
            for root, dirs, files in os.walk(root_path):
                for file in files:
                    if any(keyword.lower() in file.lower() for keyword in keywords):
                        results_list.insert(tk.END, os.path.join(root, file))
                        found_items += 1
                for dir in dirs:
                    if any(keyword.lower() in dir.lower() for keyword in keywords):
                        results_list.insert(tk.END, os.path.join(root, dir))
                        found_items += 1
    messagebox.showinfo(
        "Поиск завершен", f"Найдено файлов и папок: {found_items}")


def start_search():
    button_start.config(text="Стоп", command=stop_search)
    threading.Thread(target=search_background).start()


def stop_search():
    # Остановка поиска - необходимо при использовании многопоточности
    button_start.config(text="Начать", command=start_search)


def search_background():
    search_files(keywords_list)
    button_start.config(text="Начать", command=start_search)


# Создание главного окна
root = tk.Tk()
root.title("ReecksCheck")

# Установка темы оформления
style = ttk.Style()
style.theme_use("clam")  # Вы можете выбрать любую тему, которая вам нравится

# Создание и размещение виджетов
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

button_start = ttk.Button(frame, text="Начать", command=start_search)
button_start.pack(pady=5, padx=10, side=tk.TOP)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

results_list = tk.Listbox(frame, width=100, yscrollcommand=scrollbar.set)
results_list.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

scrollbar.config(command=results_list.yview)

# Запуск основного цикла
root.mainloop()
