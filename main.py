import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(background='#000000')

        self.button_style = {'font': ('Helvetica', 20, 'bold'), 'width': 6, 'height': 5, 'bg': '#000000', 'fg': '#FFFFFF', 'borderwidth': 5}

        self.board = [None] * 9
        self.turn = 1

        
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text="", command=lambda i=i: self.click(i), **self.button_style)
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

    def click(self, i):
        if self.board[i] is None:
            self.board[i] = self.turn
            if self.turn == 1:
                self.buttons[i].config(text='X', fg='#00FFFF')
            else:
                self.buttons[i].config(text='O', fg='#FF0000')
            if self.check_win():
                winner = 'X' if self.turn == 1 else 'O'
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.window.quit()
            elif all(cell is not None for cell in self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            self.turn = 1 - self.turn

    def check_win(self):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if self.board[win[0]] is not None and self.board[win[0]] == self.board[win[1]] == self.board[win[2]]:
                return True
        return False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
