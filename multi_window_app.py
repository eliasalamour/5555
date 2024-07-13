import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

class MultiWindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("برنامج متعدد النوافذ")
        self.root.geometry("300x200")
        
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.label = ttk.Label(self.main_frame, text="اختر لون للخلفية:")
        self.label.pack(pady=10)
        
        self.color_button = ttk.Button(self.main_frame, text="اختر لون", command=self.choose_color)
        self.color_button.pack(pady=10)
        
        self.new_window_button = ttk.Button(self.main_frame, text="افتح نافذة جديدة", command=self.open_new_window)
        self.new_window_button.pack(pady=10)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="اختر لون")[1]
        if color_code:
            self.root.configure(bg=color_code)

    def open_new_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("نافذة جديدة")
        new_window.geometry("300x200")
        
        label = ttk.Label(new_window, text="هذه نافذة جديدة")
        label.pack(pady=20)
        
        color_button = ttk.Button(new_window, text="اختر لون", command=lambda: self.change_bg_color(new_window))
        color_button.pack(pady=10)
        
    def change_bg_color(self, window):
        color_code = colorchooser.askcolor(title="اختر لون")[1]
        if color_code:
            window.configure(bg=color_code)

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiWindowApp(root)
    root.mainloop()
    git init
git add multi_window_app.py
git commit -m "Initial commit"
git remote add origin https://github.com/username/repository-name.git
git push -u origin master

