import tkinter as tk

def on_button_click():
    label.config(text="Привет, " + entry.get())

# Создание основного окна
root = tk.Tk()
root.title("Пример GUI")

# Создание элементов интерфейса
label = tk.Label(root, text="Введите ваше имя:")
entry = tk.Entry(root)
button = tk.Button(root, text="Привет", command=on_button_click)

# Размещение элементов в окне
label.pack()
entry.pack()
button.pack()

# Запуск основного цикла обработки событий
root.mainloop()
