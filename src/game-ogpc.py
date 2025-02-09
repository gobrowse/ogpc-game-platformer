from tkinter import *
import random
import time
import graphics-ogpc

tk = Tk()
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
tk.title("OGPC Game")

my_ladder = graphics.Ladder(canvas,0,0,60,50,4,5,'red')
my_platform = graphics.Platform(canvas,150,140,300,200,'peru')

tk.update()
