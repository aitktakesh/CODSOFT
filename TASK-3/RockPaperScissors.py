#CREATED BY TAKESHWAR.J
import random
import tkinter as tk
from tkinter import messagebox

def get_symbol(choice):
    symbols = {"rock": "✊", "paper": "✋", "scissors": "✌"}
    return symbols[choice]

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "tie"
    elif (
        (player1_choice == "rock" and player2_choice == "scissors") or
        (player1_choice == "scissors" and player2_choice == "paper") or
        (player1_choice == "paper" and player2_choice == "rock")
    ):
        return "player1"
    else:
        return "player2"

def play_vs_computer(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    if result == "player1":
        user_score += 1
        result_text = "You win!"
    elif result == "player2":
        computer_score += 1
        result_text = "You lose!"
    else:
        result_text = "It's a tie!"

    result_label.config(text=f"You chose: {get_symbol(user_choice)}\nComputer chose: {get_symbol(computer_choice)}\n{result_text}")
    score_label.config(text=f"Scores: You - {user_score}, Computer - {computer_score}")

def start_player2_ui():
    def player2_select():
        player2_choice = player2_var.get()

        if player2_choice not in ["rock", "paper", "scissors"]:
            messagebox.showerror("Invalid Choice", "Player 2 must choose rock, paper, or scissors.")
            return

        result = determine_winner(player1_choice, player2_choice)
        if result == "player1":
            result_text = "Player 1 wins!"
        elif result == "player2":
            result_text = "Player 2 wins!"
        else:
            result_text = "It's a tie!"

        player2_window.destroy()

        final_window = tk.Toplevel(root)
        final_window.title("Result")
        final_window.configure(bg="darkslategray")

        result_label = tk.Label(final_window, text=f"Player 1 chose: {get_symbol(player1_choice)}\nPlayer 2 chose: {get_symbol(player2_choice)}\n{result_text}", font=("Arial", 14), bg="darkslategray", fg="white")
        result_label.pack(pady=20)

        close_button = tk.Button(final_window, text="Close", font=("Arial", 14), bg="firebrick", fg="white", command=final_window.destroy)
        close_button.pack(pady=20)

    player2_window = tk.Toplevel(root)
    player2_window.title("Player 2 Select")
    player2_window.configure(bg="darkslategray")

    tk.Label(player2_window, text="Player 2, make your choice:", font=("Arial", 14), bg="darkslategray", fg="white").pack(pady=10)

    player2_var = tk.StringVar()

    button_frame = tk.Frame(player2_window, bg="darkslategray")
    button_frame.pack(pady=20)

    tk.Radiobutton(button_frame, text="✊ Rock", variable=player2_var, value="rock", font=("Arial", 12), bg="darkslategray", fg="white", selectcolor="darkslategray").grid(row=0, column=0, padx=5)
    tk.Radiobutton(button_frame, text="✋ Paper", variable=player2_var, value="paper", font=("Arial", 12), bg="darkslategray", fg="white", selectcolor="darkslategray").grid(row=0, column=1, padx=5)
    tk.Radiobutton(button_frame, text="✌ Scissors", variable=player2_var, value="scissors", font=("Arial", 12), bg="darkslategray", fg="white", selectcolor="darkslategray").grid(row=0, column=2, padx=5)

    tk.Button(player2_window, text="Submit", font=("Arial", 14), bg="mediumseagreen", fg="white", command=player2_select).pack(pady=20)

def start_player1_ui():
    def player1_select():
        global player1_choice
        player1_choice = player1_var.get()

        if player1_choice not in ["rock", "paper", "scissors"]:
            messagebox.showerror("Invalid Choice", "Player 1 must choose rock, paper, or scissors.")
            return

        player1_window.destroy()
        start_player2_ui()

    player1_window = tk.Toplevel(root)
    player1_window.title("Player 1 Select")
    player1_window.configure(bg="darkslategray")

    tk.Label(player1_window, text="Player 1, make your choice:", font=("Arial", 14), bg="darkslategray", fg="white").pack(pady=10)

    player1_var = tk.StringVar()

    button_frame = tk.Frame(player1_window, bg="darkslategray")
    button_frame.pack(pady=20)

    tk.Radiobutton(button_frame, text="✊ Rock", variable=player1_var, value="rock", font=("Arial", 12), bg="darkslategray", fg="white", selectcolor="darkslategray").grid(row=0, column=0, padx=5)
    tk.Radiobutton(button_frame, text="✋ Paper", variable=player1_var, value="paper", font=("Arial", 12), bg="darkslategray", fg="white", selectcolor="darkslategray").grid(row=0, column=1, padx=5)
    tk.Radiobutton(button_frame, text="✌ Scissors", variable=player1_var, value="scissors", font=("Arial", 12), bg="darkslategray", fg="white", selectcolor="darkslategray").grid(row=0, column=2, padx=5)

    tk.Button(player1_window, text="Submit", font=("Arial", 14), bg="mediumseagreen", fg="white", command=player1_select).pack(pady=20)

def start_game():
    choice = game_mode_var.get()

    if choice == "computer":
        instruction_label.config(text="Choose rock, paper, or scissors:")
        button_frame.pack()
    elif choice == "player":
        button_frame.pack_forget()
        start_player1_ui()
    else:
        messagebox.showerror("Invalid Choice", "Please select a game mode.")

def quit_game():
    messagebox.showinfo("Final Scores", f"Final Scores:\nYou - {user_score}\nComputer - {computer_score}")
    root.destroy()


# Initialize scores
user_score = 0
computer_score = 0
player1_choice = ""

# Set up the UI
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.configure(bg="darkslategray")

welcome_label = tk.Label(root, text="Welcome to Rock-Paper-Scissors!", font=("Arial", 20, "bold"), bg="darkslategray", fg="white")
welcome_label.pack(pady=15)

game_mode_var = tk.StringVar(value="")

instruction_label = tk.Label(root, text="Select game mode:", font=("Arial", 14), bg="darkslategray", fg="white")
instruction_label.pack(pady=5)

mode_frame = tk.Frame(root, bg="darkslategray")
mode_frame.pack(pady=10)

tk.Radiobutton(mode_frame, text="Player vs Computer", variable=game_mode_var, value="computer", font=("Arial", 12), bg="darkslategray", fg="white", selectcolor="darkslategray").grid(row=0, column=0, padx=10)

tk.Radiobutton(mode_frame, text="Player vs Player", variable=game_mode_var, value="player", font=("Arial", 12), bg="darkslategray", fg="white", selectcolor="darkslategray").grid(row=0, column=1, padx=10)

button_frame = tk.Frame(root, bg="darkslategray")

button_style = {
    "font": ("Arial", 14, "bold"),
    "relief": "raised",
    "bd": 2,
    "width": 10,
    "height": 2,
    "borderwidth": 2
}

rock_button = tk.Button(button_frame, text="✊ Rock", bg="tomato", fg="white", command=lambda: play_vs_computer("rock"), **button_style)
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = tk.Button(button_frame, text="✋ Paper", bg="cornflowerblue", fg="white", command=lambda: play_vs_computer("paper"), **button_style)
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = tk.Button(button_frame, text="✌ Scissors", bg="mediumseagreen", fg="white", command=lambda: play_vs_computer("scissors"), **button_style)
scissors_button.grid(row=0, column=2, padx=10, pady=5)

# Add the result and score labels
result_label = tk.Label(root, text="", font=("Arial", 14), bg="darkslategray", fg="white")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Scores: You - 0, Computer - 0", font=("Arial", 14), bg="darkslategray", fg="white")
score_label.pack(pady=10)

# Add start and quit buttons
start_button = tk.Button(root, text="Start Game", font=("Arial", 14), bg="mediumseagreen", fg="white", command=start_game)
start_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", font=("Arial", 14), bg="firebrick", fg="white", command=quit_game)
quit_button.pack(pady=10)

root.mainloop()