from tkinter import *
import random
import time

class Ladder:
    def __init__(self, canvas, x1,y1,x2,y2,number_rungs, width, color):
        self.Canvas = canvas
        self.side1 = canvas.create_rectangle(x1,y1,x1+width,y2, fill=color)
        self.side2 = canvas.create_rectangle(x2-width,y1,x2,y2, fill=color)
        separation = (y2-y1)/number_rungs
        self.rungs = []
        for rung in range(0,number_rungs):
            x_left = x1
            y_left = y1 + rung*separation
            x_right = x2
            y_right = y1 + width + rung*separation
            self.rungs.append(canvas.create_rectangle(x_left,y_left,x_right,y_right, fill=color))
class Platform:
    def __init__(self, canvas, x1,y1,x2,y2,color):
        self.Canvas = canvas
        self.id = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
    def draw(self):
        pass

tk = Tk()
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
tk.title("OGPC Game")

my_ladder = Ladder(canvas,0,0,60,50,4,5,'red')
my_platform = Platform(canvas,150,140,300,200,'peru')

tk.update()
