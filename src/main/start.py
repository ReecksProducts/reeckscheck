import os
import sys
import time
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from ttkthemes import ThemedTk
import threading


class FileSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Reecks Check')

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.target_names = ["Impact", "Aristois", "Xray", "Wurst", "Hack", "Baritone", "Fabritone", "Inertia", "Celestial", "Expensive", "Gumbaloff", "celka", "Ares", "Sigmaclient", "Salhack", "KAMI", "WWE", "SkillClient",
                             "Liquid Bounce", "Matix", "FATAL", "ZAMOROZKA", "NEVERHOOK", "Flux", "Xatz", "Exist", "AVALON", "DEADCODE", "Nursultan", "Boze", "EXCELLENT", "Wild", "Calestial", "X-ray", "XRAY", "xray", "cheats", "cheat", "autoclicker"]
        self.log_file = "log.txt"
        # Переменная для хранения выбранной темы
        self.theme_var = tk.StringVar(value="arc")

        self.create_widgets()

    def create_widgets(self):
        self.root.set_theme(self.theme_var.get())  # Установка темы ttkthemes

        self.label = ttk.Label(
            self.root, text='Reecks Check', font=('Helvetica', 16, 'bold'))
        self.label.grid(row=0, column=0, columnspan=2,
                        pady=(10, 20), sticky='w')

        self.log_text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=60, height=15, font=('Helvetica', 12), state='disabled')  # Добавлен state='disabled'
        self.log_text.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        self.search_button = ttk.Button(
            self.root, text='Начать поиск', command=self.start_search, style='TButton')
        self.search_button.grid(
            row=2, column=0, pady=(0, 10), padx=10, sticky='w')

        self.browse_button = ttk.Button(
            self.root, text='Обзор', command=self.browse_folder, style='TButton')
        self.browse_button.grid(row=2, column=1, pady=(
            0, 10), padx=(0, 10), sticky='e')

        # Кнопка для открытия окна настроек
        self.settings_button = ttk.Button(
            self.root, text='Настройки', command=self.open_settings, style='TButton')
        self.settings_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Определение стилей
        style = ttk.Style(self.root)
        style.configure('TButton', font=('Helvetica', 12), padding=10)

    def start_search(self):
        # Очистка текстового поля перед началом поиска
        self.log_text.configure(state='normal')  # Разрешаем редактирование
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(
            tk.END, 'Идет поиск файлов - подождите, пожалуйста...\n')
        self.log_text.configure(state='disabled')  # Запрещаем редактирование

        # Запуск поиска в отдельном потоке
        search_thread = threading.Thread(target=self.perform_search)
        search_thread.start()

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Выбрать папку")
        if folder:
            self.log_text.configure(state='normal')  # Разрешаем редактирование
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, f"Выбрана папка: {folder}\n")
            # Запрещаем редактирование
            self.log_text.configure(state='disabled')

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Настройки")

        # Надпись
        ttk.Label(settings_window, text="Выберите тему:").grid(
            row=0, column=0, pady=10)

        # Выпадающий список с выбором тем
        theme_combobox = ttk.Combobox(settings_window, textvariable=self.theme_var,
                                      values=["arc", "breeze", "equilux", "yaru"])
        theme_combobox.grid(row=0, column=1, pady=10)
        theme_combobox.set(self.theme_var.get())  # Установка текущей темы

        # Кнопка "Применить изменения"
        apply_button = ttk.Button(
            settings_window, text="Применить изменения", command=self.apply_settings)
        apply_button.grid(row=1, column=0, columnspan=2, pady=10)

    def apply_settings(self):
        selected_theme = self.theme_var.get()
        self.root.set_theme(selected_theme)
        print(f"Выбрана тема: {selected_theme}")

    def on_close(self):
        self.root.destroy()

    def perform_search(self):
        for root, dirs, files in os.walk('/'):
            for file in files:
                for target_name in self.target_names:
                    if target_name.lower() in file.lower() and file.lower().endswith(('.exe', '.jar')):
                        file_path = os.path.join(root, file)
                        message = f"{target_name} » Найден файл с именем '{file}' по пути: '{file_path}'\n"
                        self.root.after(0, self.update_log, message)

    def update_log(self, message):
        self.log_text.configure(state='normal')  # Разрешаем редактирование
        self.log_text.insert(tk.END, message)
        self.log_text.configure(state='disabled')  # Запрещаем редактирование
        self.log_text.update_idletasks()


if __name__ == '__main__':
    root = ThemedTk(theme="arc")  # Создание экземпляра ThemedTk с темой "arc"
    app = FileSearchApp(root)
    root.mainloop()

print("⚠ Проверка окончена ⚠")
print("⚠ Закрытие через 3 секунды ⚠")
print("⚠ Лог проверки сохранен в log.txt ⚠")
time.sleep(3)
print("██████╗ ██████╗  ██████╗ ██████╗ ███████╗██████╗ ██╗  ██╗ █████╗ ")
print("██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔══██╗")
print("██████╔╝██████╔╝██║   ██║██████╔╝█████╗  ██████╔╝█████╔╝ ███████║")
print("██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██╔══╝  ██╔═══╝ ██╔═██╗ ██╔══██║")
print("██║     ██║  ██║╚██████╔╝██████╔╝███████╗██║     ██║  ██╗██║  ██║")
print("╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝")
time.sleep(3)
