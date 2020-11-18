from tkinter import *
from PIL import ImageTk,Image 

root = Tk()
root.title('Learn To Code at Codemy.com')




button_quit = Button(root, text="Exit", command=root.quit)

label = Label()
label.pack()


button_quit.pack()
t = Text(root, height=5, width=30)
t.insert(END, "What the Fuck!\nChuck!")
#t.pack()


root.mainloop()