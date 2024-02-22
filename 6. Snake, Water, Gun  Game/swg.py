import random
import tkinter as tk

def play_game(user_choice):
    computer_choice = random.choice(["snake", "water", "gun"])
    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    result_label.config(text=winner)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "snake":
        return "You win!" if computer_choice == "water" else "Computer wins!"
    elif user_choice == "water":
        return "You win!" if computer_choice == "gun" else "Computer wins!"
    elif user_choice == "gun":
        return "You win!" if computer_choice == "snake" else "Computer wins!"

# Create main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x200")  # Increase the size of the window

# Function to pass user choice to play_game function
def choose_option(option):
    play_game(option)

# Create buttons for user choice
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
button_font = ('Helvetica', 14)  # Increase the font size for buttons
snake_button = tk.Button(button_frame, text="Snake", font=button_font, command=lambda: choose_option("snake"))
snake_button.pack(side=tk.LEFT, padx=5)
water_button = tk.Button(button_frame, text="Water", font=button_font, command=lambda: choose_option("water"))
water_button.pack(side=tk.LEFT, padx=5)
gun_button = tk.Button(button_frame, text="Gun", font=button_font, command=lambda: choose_option("gun"))
gun_button.pack(side=tk.LEFT, padx=5)

# Create result display
label_font = ('Helvetica', 12)  # Increa    se the font size for labels
user_label = tk.Label(root, text="", font=label_font)
user_label.pack()
computer_label = tk.Label(root, text="", font=label_font)
computer_label.pack()
result_label = tk.Label(root, text="", font=label_font)
result_label.pack()

root.mainloop()
