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