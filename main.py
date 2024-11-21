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
        self.seconds = 0
        self.count = 0
        self.creat_window()


    def creat_window(self):
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(False, False)
        self.create_widget()


    def create_widget(self):
        label_count = ttk.Label(self.root, text=f"Кол-во ходов: {self.count}", font=(FONT_FAMILY, FONT_SIZE - 10))
        self.lab_count = label_count
        label_count.pack(anchor='nw', padx=3, pady=3)

        label_timer = ttk.Label(self.root, text=f"Время: {self.seconds}", font=(FONT_FAMILY, FONT_SIZE - 10))
        self.lab_timer = label_timer
        label_timer.pack(anchor='nw', padx=3, pady=3) 
        
        self.frm.pack(fill=BOTH, expand=True)

        self.generation_numbers()
        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        
        for y in range(4):
            for x in range(4):
                button = Button(self.frm, text=self.board[y][x], background="#BC8651", foreground="#2B1D0F", font=(FONT_FAMILY, FONT_SIZE), width=3, height=3, command=lambda X=x, Y=y: self.move_button(X, Y))
                button.grid(row=y, column=x, sticky=NSEW)
                self.frm.columnconfigure(index=y, weight=1)
                self.frm.rowconfigure(index=x, weight=1)
                self.buttons[y][x] = button

        
    def update_widget(self):
        for y in range(4):
            for x in range(4):
                new_val = self.board[y][x]
                if(new_val == None):
                    new_val = ''
                self.buttons[y][x]['text'] = new_val
        self.lab_count['text'] = f"Кол-во ходов: {self.count}"


    def move_button(self, x: int, y: int):
        if (x, y) == self.emptry_pos:
            return
        
        # слева
        if(y == self.emptry_pos[1] and x > self.emptry_pos[0]):
            for i in range(abs(x - self.emptry_pos[0])):
                self.board[y][self.emptry_pos[0] + i], self.board[y][self.emptry_pos[0] + i + 1] = self.board[y][self.emptry_pos[0] + i + 1], self.board[y][self.emptry_pos[0] + i]
                self.count += 1

        # справа
        elif(y == self.emptry_pos[1] and x < self.emptry_pos[0]):
            for i in range(abs(x - self.emptry_pos[0])):
                self.board[y][self.emptry_pos[0] - i], self.board[y][self.emptry_pos[0] - i - 1] = self.board[y][self.emptry_pos[0] - i - 1], self.board[y][self.emptry_pos[0] - i] 
                self.count += 1          

        # сверху
        elif(x == self.emptry_pos[0] and y > self.emptry_pos[1]):
            for i in range(abs(self.emptry_pos[1] - y)):
                self.board[self.emptry_pos[1] + i][x], self.board[self.emptry_pos[1] + i + 1][x] = self.board[self.emptry_pos[1] + i + 1][x], self.board[self.emptry_pos[1] + i][x]
                self.count += 1          
            

        # снизу
        elif(x == self.emptry_pos[0] and y < self.emptry_pos[1]):
            for i in range(abs(self.emptry_pos[1] - y)):
                self.board[self.emptry_pos[1] - i][x], self.board[self.emptry_pos[1] - i - 1][x] = self.board[self.emptry_pos[1] - i - 1][x], self.board[self.emptry_pos[1] - i][x]
                self.count += 1  

        else: return 0

        self.emptry_pos = (x, y)
        self.update_widget()   


    def generation_numbers(self):
        numbers = list(range(1, 16)) + [None]
        random.shuffle(numbers)
        self.board = [numbers[i:i + 4] for i in range(0, 16, 4)]
        
        for y in range(4):
            for x in range(4):
                if(self.board[y][x] == None): self.emptry_pos = (x, y)


    def update_timer(self):
        self.seconds += 1
        
        seconds = self.seconds % 60
        minutes = int(self.seconds / 60)
        self.lab_timer['text'] = f"Время: {minutes}:{seconds}"
        self.root.after(1000, self.update_timer)
                

if __name__ == "__main__":
    tk = Tk()
    puzzle15 = Puzzle15(tk)
    tk.mainloop()