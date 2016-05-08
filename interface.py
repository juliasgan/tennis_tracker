import Tkinter as tk
from Tkinter import *


class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("Cate School Tennis Tracker")



        self.t = SimpleTable(self, 5,5)
        self.t.pack(side="top", fill="x")


class SimpleTable(tk.Frame):
#http://zetcode.com/gui/tkinter/layout/
    def __init__(self, parent, rows=3, columns=3):
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if row == 4 and column == 4:
                    label = tk.Label(self, text="%s/%s" % (row, column),
                                    borderwidth=0, width=10, font = "-weight bold")
                elif row == 1 and column == 4 or column == 1 and row == 4:
                    label = tk.Label(self, text="%s/%s" % (row, column),
                                     borderwidth=0, width=10, bg = "yellow")
                elif row == 2 and column == 4 or column == 2 and row == 4:
                    label = tk.Label(self, text="%s/%s" % (row, column),
                                     borderwidth=0, width=10, bg="orange")
                elif row == 3 and column == 4 or column == 3 and row == 4:
                    label = tk.Label(self, text="%s/%s" % (row, column),
                                     borderwidth=0, width=10, bg="red")


                else:
                    label = tk.Label(self, text="%s/%s" % (row, column),
                                     borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

        w2 = Label(self, text="Opponent", font="-weight bold", bg = "green")
        w1 = Label(self, text="Cate", font="-weight bold", bg = "blue")
        w1.grid(row=0, column=0, sticky="nsew", padx=1, pady=1, columnspan = 5)
        w2.grid(row=1, column=0, sticky="nsew", padx=1, pady=1, rowspan = 5)
        #w1.grid(row=0, column=1, sticky="nsew", padx=1, pady=1, columnspan = 5)
        #w2.grid(row=2, column=0, sticky="nsew", padx=1, pady=1, rowspan = 5)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


if __name__ == "__main__":
    app = Interface()
    app.mainloop()