from tkinter import *

class Gui:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Minimum Spanning Tree")
        self.window.geometry("1280x720")

        left_frame = Frame(self.window, relief="solid", bd=1)
        right_frame = Frame(self.window, relief="solid", bd=1)

        left_frame.pack(side="left", fill="both", expand=True)
        right_frame.pack(side="right", fill="both", expand=True)

        canvas = Canvas(left_frame, relief="solid", bd=2)
        canvas.pack(fill="both", expand=True)

        canvas.bind("<Button-1>", mouse)

        super().__init__()

    def start(self) -> None:
        self.window.mainloop()

def mouse(event):
    print(event.x, event.y)