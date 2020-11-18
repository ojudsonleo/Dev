from tkinter import *

canvas_width = 500
canvas_height =500

root = Tk()

canvas = Canvas(root, 
           width=canvas_width, 
           height=canvas_height, bg="white")
canvas.pack()

canvas.create_image(0,0, anchor=NW)

mainloop()