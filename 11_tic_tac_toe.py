import tkinter as tk
from tkinter import messagebox

# Check Winner Function
def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            root.quit()

# Button Click Function
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

# Player Switch Function
def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

# Window Setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
winner = False

# Turn Label
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 15))
label.grid(row=0, column=0, columnspan=3)

# Buttons Creation
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                      command=lambda i=i: button_click(i)) for i in range(9)]

# Grid Layout
for i, button in enumerate(buttons):
    button.grid(row=(i // 3) + 1, column=i % 3)

root.mainloop()


