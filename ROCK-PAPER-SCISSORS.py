import tkinter as tk
import random


user_score = 0
computer_score = 0


def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)


heading = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"))
heading.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('rock'))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('paper'))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('scissors'))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)


result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue")
result_label.pack(pady=10)


score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack(pady=10)


exit_btn = tk.Button(root, text="Exit", command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()