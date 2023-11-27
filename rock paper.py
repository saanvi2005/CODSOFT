import random
import tkinter as tk
from tkinter import font

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'paper' and comp_choice == 'rock') or \
         (user_choice == 'scissors' and comp_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    def on_choice_click(choice):
        comp_choices = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(comp_choices)

        result = determine_winner(choice, comp_choice)
        result_label.config(text=f"Result: {result}")

        user_choice_label.config(text=f"Your choice: {choice.capitalize()}")
        comp_choice_label.config(text=f"Computer's choice: {comp_choice.capitalize()}")

        if result == "You win!":
            user_score_var.set(user_score_var.get() + 1)
        elif result == "Computer wins!":
            comp_score_var.set(comp_score_var.get() + 1)

    root = tk.Tk()
    root.title("Let's play Rock, Paper, Scissors")

    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=18)

    user_score_var = tk.IntVar()
    comp_score_var = tk.IntVar()

    user_score_label = tk.Label(root, text="Your Score:", font=("Arial", 18, "bold"))
    user_score_label.grid(row=0, column=0)
    user_score_display = tk.Label(root, textvariable=user_score_var, font=("Arial", 18))
    user_score_display.grid(row=0, column=1)

    comp_score_label = tk.Label(root, text="Computer's Score:", font=("Arial", 18, "bold"))
    comp_score_label.grid(row=0, column=2)
    comp_score_display = tk.Label(root, textvariable=comp_score_var, font=("Arial", 18))
    comp_score_display.grid(row=0, column=3)

    rock_button = tk.Button(root, text="Rock", command=lambda: on_choice_click("rock"), font=("Arial", 18))
    rock_button.grid(row=1, column=0, padx=20, pady=10)

    paper_button = tk.Button(root, text="Paper", command=lambda: on_choice_click("paper"), font=("Arial", 18))
    paper_button.grid(row=1, column=1, padx=20, pady=10)

    scissors_button = tk.Button(root, text="Scissors", command=lambda: on_choice_click("scissors"), font=("Arial", 18))
    scissors_button.grid(row=1, column=2, padx=20, pady=10)

    user_choice_label = tk.Label(root, text="Your choice:", font=("Arial", 18))
    user_choice_label.grid(row=2, column=0, columnspan=2)

    comp_choice_label = tk.Label(root, text="Computer's choice:", font=("Arial", 18))
    comp_choice_label.grid(row=2, column=2, columnspan=2)

    result_label = tk.Label(root, text="Result:", font=("Arial", 18))
    result_label.grid(row=3, column=0, columnspan=4)

    root.mainloop()

play_game()
