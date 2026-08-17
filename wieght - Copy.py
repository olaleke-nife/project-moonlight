import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Function to Convert Weight
# -----------------------------


def convert_weight():
    try:
        weight = float(entry_weight.get())

        from_unit = combo_from.get()
        to_unit = combo_to.get()

        # Convert everything to kilograms first
        if from_unit == "Kilograms":
            kg = weight
        elif from_unit == "Grams":
            kg = weight / 1000
        elif from_unit == "Pounds":
            kg = weight / 2.20462

        # Convert kilograms to the selected unit
        if to_unit == "Kilograms":
            result = kg
        elif to_unit == "Grams":
            result = kg * 1000
        elif to_unit == "Pounds":
            result = kg * 2.20462

        lbl_result.config(text=f"Result: {round(result, 2)} {to_unit}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# -----------------------------
# Clear Function
# -----------------------------


def clear():
    entry_weight.delete(0, tk.END)
    lbl_result.config(text="Result: ")


# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()
root.title("Simple Weight Converter")
root.geometry("800x500")
root.resizable(False, False)

# -----------------------------
# Heading
# -----------------------------
title = tk.Label(
    root,
    text="Weight Converter",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# -----------------------------
# Weight Entry
# -----------------------------
tk.Label(root, text="Enter Weight:", font=("Arial", 12)).pack()

entry_weight = tk.Entry(root, font=("Arial", 12), justify="center")
entry_weight.pack(pady=5)

# -----------------------------
# From Unit
# -----------------------------
tk.Label(root, text="From:", font=("Arial", 12)).pack()

combo_from = ttk.Combobox(
    root,
    values=["Kilograms", "Grams", "Pounds"],
    state="readonly"
)
combo_from.current(0)
combo_from.pack(pady=5)

# -----------------------------
# To Unit
# -----------------------------
tk.Label(root, text="To:", font=("Arial", 12)).pack()

combo_to = ttk.Combobox(
    root,
    values=["Kilograms", "Grams", "Pounds"],
    state="readonly"
)
combo_to.current(1)
combo_to.pack(pady=5)

# -----------------------------
# Buttons
# -----------------------------
btn_convert = tk.Button(
    root,
    text="Convert",
    font=("Arial", 12),
    command=convert_weight,
    width=12
)
btn_convert.pack(pady=10)

btn_clear = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12),
    command=clear,
    width=12
)
btn_clear.pack()

# -----------------------------
# Result Label
# -----------------------------
lbl_result = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 14, "bold")
)
lbl_result.pack(pady=15)

# -----------------------------
# Run Program
# -----------------------------
root.mainloop()
