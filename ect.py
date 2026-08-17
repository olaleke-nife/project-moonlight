import tkinter as tk
from tkinter import ttk, messagebox


emojis = {
    "happy": "😊",
    "sad": "😢",
    "winking": "😉",
    "grinning": "😃",
    "love": "❤️",
    "confused": "😳",
    "annoyed": "😠",
    "laughing": "😂",
    "impressed": "😊",
    "skeptical": "😒",
    "neutral": "😑",
    "sad": "😭",
    "cool": "😎",
    "sweet": "😘",
    "pouting": "😕",
    "disappointed": "😕",
    "annoyed": "😐",
    "why": "😐",
    "shocked": "😳",
    "wow": "😳",
    "Y:\n": "🤐",
    "i cant say": "🤐",
    "sleepy": "😴",
    "i am": "😴",
    "sad": "😖",
    "ugh": "😖",
    "furious": "😡",
    "cool": "😎",
}


def convert_emojis():

    text = txt_input.get("1.0", tk.END)

    for shortcut, emoji in emojis.items():
        text = text.replace(shortcut, emoji)

    lbl_output.config(text=f"Converted Text:\n{text.strip()}")


root = tk.Tk()
root.title("EMOJI CONVERTER")
root.geometry("600x500")


title = tk.Label(root, text="Emoji Converter", font=("Arial", 16, "bold"))
title.pack(pady=10)

tk.Label(root, text="Enter your text here:", font=("Arial", 12)).pack(pady=5)


txt_input = tk.Text(root, height=5, width=50, font=("Arial", 12))
txt_input.pack(padx=10, pady=5)


btn_convert = tk.Button(
    root,
    text="Convert to Emojis",
    font=("Arial", 12, "bold"),
    command=convert_emojis,
    width=18
)
btn_convert.pack(pady=15)

# Output Display Label
lbl_output = tk.Label(
    root,
    text="Converted Text: ",
    font=("Arial", 14),
    justify="center",
    wraplength=500
)
lbl_output.pack(pady=15)

# Run GUI
root.mainloop()
