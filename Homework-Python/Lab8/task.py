#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageDraw, ImageFont, ImageTk


# =========================
# СВОЁ ИСКЛЮЧЕНИЕ
# =========================
class MemeError(Exception):
    pass


# =========================
# КЛАСС МЕМА
# =========================
class MemeGenerator:

    def __init__(self):
        self.image_path = None
        self.image = None

    def load_image(self, path):
        if not path:
            raise MemeError("Файл не выбран!")
        self.image_path = path
        self.image = Image.open(path)

    def create_meme(self, top_text, bottom_text, color, size):
        if not self.image:
            raise MemeError("Сначала выберите изображение!")

        img = self.image.copy()
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", size)
        except:
            font = ImageFont.load_default()

        width, height = img.size

        draw.text((width/2, 10), top_text, fill=color, anchor="mm", font=font)
        draw.text((width/2, height - 40), bottom_text, fill=color, anchor="mm", font=font)

        return img

    def save(self, img):
        img.save("meme_result.png")


# =========================
# GUI
# =========================
gen = MemeGenerator()
text_color = "white"


def load_image():
    path = filedialog.askopenfilename()
    try:
        gen.load_image(path)

        img = gen.image.resize((300, 200))
        img_tk = ImageTk.PhotoImage(img)

        panel.config(image=img_tk)
        panel.image = img_tk

        status.config(text="Изображение загружено")

    except MemeError as e:
        messagebox.showerror("Ошибка", str(e))


def choose_color():
    global text_color
    color = colorchooser.askcolor()[1]
    if color:
        text_color = color


def generate():
    try:
        img = gen.create_meme(
            entry_top.get(),
            entry_bottom.get(),
            text_color,
            font_size.get()
        )

        gen.save(img)
        status.config(text="Мем сохранён (meme_result.png)")

    except MemeError as e:
        messagebox.showerror("Ошибка", str(e))


# =========================
# ОКНО
# =========================
window = tk.Tk()
window.title("🔥 Meme Generator PRO")
window.geometry("500x500")
window.configure(bg="#2b2b2b")

# стиль текста
def label(text):
    return tk.Label(window, text=text, bg="#2b2b2b", fg="white")

label("Выберите изображение").pack()
tk.Button(window, text="Загрузить", command=load_image).pack(pady=5)

panel = tk.Label(window)
panel.pack(pady=5)

label("Верхний текст").pack()
entry_top = tk.Entry(window, width=40)
entry_top.pack()

label("Нижний текст").pack()
entry_bottom = tk.Entry(window, width=40)
entry_bottom.pack()

label("Размер шрифта").pack()
font_size = tk.IntVar(value=30)
tk.Scale(window, from_=10, to=80, orient="horizontal", variable=font_size).pack()

tk.Button(window, text="Выбрать цвет текста", command=choose_color).pack(pady=5)

tk.Button(window, text="Создать мем", command=generate, bg="#4CAF50", fg="white").pack(pady=10)

status = tk.Label(window, text="", bg="#2b2b2b", fg="lightgreen")
status.pack()

window.mainloop()