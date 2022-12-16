from tkinter import Tk
from tkinter import Canvas
import random
import time
 
window = Tk()
window.geometry("650x550")
window.configure(background = "grey")
window.title("Canvas - Draw Shapes")
window.resizable(False, False)

def paint(x,y):
    canvas.create_oval(x-1, y-1, x+1, y+1, fill="green")
    
def findMiddle(x,y):
    count = 0
    while (count < 15000):
        refpoint=random.randint(1,3)
        if refpoint == 1:
            midx = (x + 100) / 2
            midy = (y + 400) / 2
        if refpoint == 2:
            midx = (x + 500) / 2
            midy = (y + 400) / 2
        if refpoint == 3:
            midx = (x + 300) / 2
            midy = (y + 100) / 2
        paint(midx, midy)
        x = midx
        y = midy
        count = count+1
    


 
# setting up the canvas
canvas = Canvas(width = 600, height = 500, bg = "white")
canvas.pack(pady = 20)

#draw 3 points of triangle
paint(100,400)
paint(500,400)
paint(300,100)
paint(300,400)
findMiddle(300,400)
window.mainloop()