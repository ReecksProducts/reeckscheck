import os
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, font
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
        self.theme_var = tk.StringVar(value="arc")

        self.create_widgets()

    def create_widgets(self):
        self.root.set_theme(self.theme_var.get())

        # Используем альтернативный шрифт (смотрите изменение здесь)
        custom_font = font.Font(family="Arial", size=12)

        self.label = ttk.Label(
            self.root, text='Reecks Check', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, columnspan=2,
                        pady=(10, 20), sticky='w')

        self.log_text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=60, height=15, font=custom_font, state='disabled')
        self.log_text.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        self.search_button = ttk.Button(
            self.root, text='Начать поиск', command=self.start_search, style='TButton')
        self.search_button.grid(
            row=2, column=0, pady=(0, 10), padx=10, sticky='w')

        self.browse_button = ttk.Button(
            self.root, text='Обзор', command=self.browse_folder, style='TButton')
        self.browse_button.grid(row=2, column=1, pady=(
            0, 10), padx=(0, 10), sticky='e')

        self.settings_button = ttk.Button(
            self.root, text='Настройки', command=self.open_settings, style='TButton')
        self.settings_button.grid(row=3, column=0, columnspan=2, pady=10)

        style = ttk.Style(self.root)
        style.configure('TButton', font=('Arial', 12), padding=10)

    def start_search(self):
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(
            tk.END, 'Идет поиск файлов - подождите, пожалуйста...\n')
        self.log_text.config(state='disabled')

        search_thread = threading.Thread(target=self.perform_search)
        search_thread.start()

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Выбрать папку")
        if folder:
            self.log_text.config(state='normal')
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, f"Выбрана папка: {folder}\n")
            self.log_text.config(state='disabled')

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Настройки")

        ttk.Label(settings_window, text="Выберите тему:").grid(
            row=0, column=0, pady=10)

        theme_combobox = ttk.Combobox(settings_window, textvariable=self.theme_var,
                                      values=["arc", "breeze", "equilux", "yaru"])
        theme_combobox.grid(row=0, column=1, pady=10)
        theme_combobox.set(self.theme_var.get())

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
        found_files = set()  # Используем множество для хранения уникальных файлов
        for root, dirs, files in os.walk('/'):
            for file in files:
                file_lower = file.lower()
                for target_name in self.target_names:
                    if target_name.lower() in file_lower and file_lower.endswith(('.exe', '.jar')):
                        file_path = os.path.join(root, file)
                        found_files.add((file, file_path))

        for file_name, file_path in found_files:
            message = f"Найден файл с именем '{file_name}' по пути: '{file_path}'\n"
            self.root.after(0, self.update_log, message)

    def update_log(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message)
        self.log_text.config(state='disabled')
        self.log_text.update_idletasks()


if __name__ == '__main__':
    root = ThemedTk(theme="arc")
    app = FileSearchApp(root)
    root.mainloop()
