import tkinter as tk
from tkinter import  messagebox
import random

def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6,],[1,4,7,],[2,5,8,],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] ==buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner=True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
            return
        
        
        
    #Draw condition
    if all(button["text"]!= "" for button in buttons) and not winner:
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        root.quit()
                        
def button_click(index):
    global winner
    if buttons[index]["text"]== "" and not winner and current_player =="X":
        buttons[index]["text"]= current_player
        check_winner()
        if not winner:
            toggle_player()
            root.after(500, ai_move)
        
def ai_move():
    global winner
    if winner or current_player!= "0":
        return
    empty_cells= [i for i in range(9) if buttons[i]["text"] == ""]
    if empty_cells:
        ai_choice = random.choice(empty_cells)
        buttons[ai_choice]["text"] = "0"
        check_winner()
        if not winner:
            toggle_player()        
    
def toggle_player():
    global current_player
    current_player ="0" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")
    
root =tk.Tk()
root.title("Tic-Tac-Toe Vs AI")

buttons = [tk.Button(root,text="", font=("Arial", 30), width=4, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3, padx=5, pady=5)
    
current_player ="X"
winner= False
label=tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16))
label.grid(row=3, column=0 , columnspan=3, pady=10)

root.mainloop()
