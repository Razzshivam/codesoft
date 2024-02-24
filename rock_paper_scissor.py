import tkinter as tk
from tkinter import messagebox
import random

def play():
    user_choice = user_var.get()
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result_var.set(f"Computer chose: {computer_choice}\nIt's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_var.set(f"Computer chose: {computer_choice}\nYou win!")
    else:
        result_var.set(f"Computer chose: {computer_choice}\nComputer wins!")

def clear_result():
    result_var.set("")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

choices = ["Rock", "Paper", "Scissors"]

user_var = tk.StringVar()
result_var = tk.StringVar()

# UI Elements
user_label = tk.Label(root, text="Your Choice:")
user_label.grid(row=0, column=0, padx=10, pady=10)

user_option = tk.OptionMenu(root, user_var, *choices)
user_option.grid(row=0, column=1, padx=10, pady=10)

play_button = tk.Button(root, text="Play", command=play)
play_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, textvariable=result_var, wraplength=300)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear Result", command=clear_result)
clear_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
