from tkinter import *
import random
import time
import graphics_ogpc

tk = Tk()
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
tk.title("VERY GOOD GAME! Game")

hero = graphics_ogpc.MainKid(canvas,0,390)
my_ladder = graphics_ogpc.Ladder(canvas,250,340,280,390,4,5,'red')
my_platform = graphics_ogpc.Platform(canvas,0,390,500,400,'peru')

while True:
    hero.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.0001)
    
