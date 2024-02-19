import os
import threading
import psutil
import tkinter as tk
from tkinter import ttk

# Список ключевых слов
keywords_list = ["Impact", "Aristois", "Xray", "Wurst", "Hack", "Baritone", "Fabritone", "Inertia", "Celestial", "Expensive", "Gumbaloff", "celka", "Ares", "Sigmaclient", "Salhack", "KAMI", "WWE", "SkillClient",
                 "Liquid Bounce", "Matix", "FATAL", "ZAMO", "NEVERHOOK", "Flux", "Xatz", "Exist", "AVALON", "DEADCODE", "Nursultan", "Boze", "EXCELLENT", "Wild", "Calestial", "X-ray", "XRAY", "xray", "cheats", "cheat", "autoclicker"]

# Глобальные переменные
searching = False
search_thread = None


def search_files():
    global searching
    searching = True
    results_list.delete(0, tk.END)
    for drive in range(ord('A'), ord('Z')+1):
        drive_letter = chr(drive)
        root_path = f"{drive_letter}:\\"
        if os.path.exists(root_path):
            for root, dirs, files in os.walk(root_path):
                if not searching:
                    return
                for file in files:
                    if any(keyword.lower() in file.lower() for keyword in keywords_list):
                        results_list.insert(tk.END, os.path.join(root, file))
                for dir in dirs:
                    if any(keyword.lower() in dir.lower() for keyword in keywords_list):
                        results_list.insert(tk.END, os.path.join(root, dir))
    ram_usage = psutil.virtual_memory().used / (1024 * 1024)  # RAM usage in MB
    status_var.set(f"Поиск завершен | Нагрузка RAM: {ram_usage:.2f} мб")


def start_search():
    global search_thread
    if search_thread and search_thread.is_alive():
        return
    button_start.config(text="Стоп", command=stop_search)
    search_thread = threading.Thread(target=search_files)
    search_thread.start()


def stop_search():
    global searching
    searching = False
    button_start.config(text="Начать", command=start_search)


def on_closing():
    if search_thread and search_thread.is_alive():
        stop_search()
        # Повторная попытка закрыть окно через 100 миллисекунд
        root.after(100, on_closing)
    else:
        root.destroy()


# Создание главного окна
root = tk.Tk()
root.title("ReecksCheck")

# Установка темы оформления
style = ttk.Style()
style.theme_use("clam")  # Вы можете выбрать любую тему, которая вам нравится

# Создание и размещение виджетов
frame_top = tk.Frame(root)
frame_top.pack(fill=tk.BOTH, expand=True)

button_start = ttk.Button(frame_top, text="Начать", command=start_search)
button_start.pack(pady=5, padx=10, side=tk.TOP)

scrollbar = tk.Scrollbar(frame_top)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

results_list = tk.Listbox(frame_top, width=100, yscrollcommand=scrollbar.set)
results_list.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

scrollbar.config(command=results_list.yview)

frame_bottom = tk.Frame(root)
frame_bottom.pack(fill=tk.X)

status_var = tk.StringVar()
status_label = tk.Label(frame_bottom, textvariable=status_var,
                        bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(fill=tk.X)

# Обработчик закрытия окна
root.protocol("WM_DELETE_WINDOW", on_closing)

# Запуск основного цикла
root.mainloop()
