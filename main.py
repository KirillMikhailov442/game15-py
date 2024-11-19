import random
from tkinter import ttk
from constants import *
from tkinter import *

class Puzzle15:
    def __init__(self, root) -> None:
        self.root: Tk = root
        self.frm = Frame(padx=2, pady=2)
        self.board = []
        self.buttons = []
        self.emptry_pos = (0, 0)
        self.selected_pos = (0, 0)
        self.lab_count = None
        self.lab_timer = None
        self.creat_window()


    def creat_window(self):
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(False, False)
        self.create_widget()


    def create_widget(self):
        label_count = ttk.Label(self.root, text=f"Кол-во ходов: 0", font=(FONT_FAMILY, FONT_SIZE - 10))
        self.lab_count = label_count
        label_count.pack(anchor='nw', padx=3, pady=3)

        label_timer = ttk.Label(self.root, text=f"Время: 0", font=(FONT_FAMILY, FONT_SIZE - 10))
        self.lab_timer = label_timer
        label_timer.pack(anchor='nw', padx=3, pady=3) 
        
        self.frm.pack(fill=BOTH, expand=True)

        self.generation_numbers()
        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        
        for y in range(4):
            for x in range(4):
                button = Button(self.frm, text=self.board[y][x], background="#BC8651", foreground="#2B1D0F", font=(FONT_FAMILY, FONT_SIZE), width=3, height=3)
                button.grid(row=y, column=x, sticky=NSEW)
                self.frm.columnconfigure(index=y, weight=1)
                self.frm.rowconfigure(index=x, weight=1)
                self.buttons[y][x] = button


    def generation_numbers(self):
        numbers = list(range(1, 16)) + [None]
        self.board = [numbers[i:i + 4] for i in range(0, 16, 4)]
                

if __name__ == "__main__":
    tk = Tk()
    puzzle15 = Puzzle15(tk)
    tk.mainloop()