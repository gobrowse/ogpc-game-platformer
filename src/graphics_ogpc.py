from tkinter import *
from PIL import Image, ImageTk
class Ladder:
    def __init__(self, canvas, x1,y1,x2,y2,number_rungs, width, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
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
class MainKid:
    def __init__(self, canvas, x1,y1,ladderslist):
        self.canvas = canvas
        self.ladderslist = ladderslist
        self.x1 = x1
        self.y1 = y1
#        self.photoimage = PhotoImage(file="../assets/images/person.gif")
        self.photoimage = [PhotoImage(file="../assets/images/personframes/sprite_0.png"),PhotoImage(file="../assets/images/personframes/sprite_1.png"),PhotoImage(file="../assets/images/personframes/sprite_2.png"),PhotoImage(file="../assets/images/personframes/sprite_3.png"),PhotoImage(file="../assets/images/personframes/sprite_4.png"),PhotoImage(file="../assets/images/personframes/sprite_5.png")]
        self.animate = 0
        self.image = canvas.create_image(x1,y1,image=self.photoimage[self.animate],anchor="sw")
        canvas.bind_all("<KeyPress-Left>", self.move_left)
        canvas.bind_all("<KeyPress-Right>", self.move_right)
        canvas.bind_all("<KeyPress-Up>", self.climb)
        self.xmove = 0
        self.ymove = 0
    def move_right(self,event):
        self.animate = self.animate + 1
        self.xmove = 4
    def move_left(self,event): 
        self.animate = self.animate + 1
        self.xmove = -4
    def climb(self,event):
        if self.is_near_ladder():
            self.ymove = -4
    def is_near_ladder(self):
        for x in self.ladderslist:
            if self.x1 >= x.x1 and self.x1 <= x.x2:
                return True
        return False
    def draw(self):
        if self.animate == 5:
            self.animate = 0
        self.canvas.itemconfig(self.image,image=self.photoimage[self.animate])
        if (self.x1 + self.xmove) <= 0:
            self.xmove = 0
        if (self.x1 + self.xmove) >= 450:
            self.xmove = 0
        self.canvas.move(self.image,self.xmove,self.ymove)
        self.x1 = self.x1 + self.xmove
        self.xmove = 0
        self.ymove = 0
