from tkinter import*
import math

x1 = y1 = 0
dist=200
angle=0
value=int(360/5)

def moving(event):
    global x1, y1
    x1, y1 = event.x, event.y  
    canvas.moveto(pic, x1-80, y1-80)

window = Tk()

canvas = Canvas(window, width=1200, height=800, bg="skyblue")
canvas.pack()

img0 = PhotoImage(file="냐옹이.png")

for i in range(0, 6):
    rad=3.141592*angle/180
    tx = dist*math.cos(rad)
    ty = dist*math.sin(rad)
    angle += value
    tx += 600
    ty += 300
    pic = canvas.create_image(tx, ty, image=img0)


canvas.bind("<B1-Motion>", moving)

window.mainloop()