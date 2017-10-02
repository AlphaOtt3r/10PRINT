from tkinter import *
import random as ra

master = Tk()
master.title("10PRINT")
master.config(bg="white")

c = Canvas(master, width="800", height="600", bg="steelblue")
c.pack()

sp = 30
x  = 0
y  = 0

def draw_line(x,y,c,sp):
	if ra.randint(0,1) <= 0.5:
		c.create_line(x, y, x+sp, y+sp, fill="black")
	else:
		c.create_line(x, y+sp, x+sp, y)


while y <= int(c["height"]):
	draw_line(x,y,c,sp)  
	if int(c["width"]) < x:
		x = 0
		y = y +sp
	else:
		x = x +sp

mainloop()