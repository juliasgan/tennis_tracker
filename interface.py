import Tkinter as tk
from Tkinter import *


class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.t = SimpleTable(self, 4,4)
        self.t.pack(side="top", fill="x")


class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=3, columns=3):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column),
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

        w2 = Label(self, text="Opponent")
        w1 = Label(self, text="Cate")
        w1.grid(row=0, column=0, sticky="nsew", padx=1, pady=1, columnspan = 4)
        w2.grid(row=1, column=0, sticky="nsew", padx=1, pady=1, rowspan = 4)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

if __name__ == "__main__":
    app = Interface()
    app.mainloop()