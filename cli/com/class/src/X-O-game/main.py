# https://www.youtube.com/watch?v=mcP9qehN1_Q

import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1350x750+0+0")
root.title("X VS O")
root.configure(background="Cadet Blue")


Tops = Frame(root, bg="Cadet Blue", pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=("arial", 50, "bold"), text="Advanced X or O", bd=21, bg="Cadet Blue", fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg="Powder Blue", pady=2, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)

buttons = StringVar()
click = True


def checker(buttons):
	global click
	if buttons["text"] == "" and click == True:
		buttons["text"] = "X"
		click = False
		scorekeeper()
	elif buttons["text"] == "" and click == False:
		buttons["text"] = "0"
		click = True
		scorekeeper()


def scorekeeper():
	if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
		button1.configure(background="blue")
		button2.configure(background="blue")
		button3.configure(background="blue")
		n = int(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
		reset()
	elif (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
		button4.configure(background="blue")
		button5.configure(background="blue")
		button6.configure(background="blue")
		n = int(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
		reset()
	elif (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
		button7.configure(background="blue")
		button8.configure(background="blue")
		button9.configure(background="blue")
		n = int(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
		reset()
	elif (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
		button1.configure(background="blue")
		button4.configure(background="blue")
		button7.configure(background="blue")
		n = int(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
		reset()
	elif (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"):
		button2.configure(background="blue")
		button5.configure(background="blue")
		button8.configure(background="blue")
		n = int(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
		reset()
	elif (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
		button3.configure(background="blue")
		button6.configure(background="blue")
		button9.configure(background="blue")
		n = int(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
		reset()
	elif (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
		button1.configure(background="blue")
		button5.configure(background="blue")
		button9.configure(background="blue")
		n = int(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
		reset()
	elif (button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
		button3.configure(background="blue")
		button5.configure(background="blue")
		button7.configure(background="blue")
		n = int(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
		reset()
	
	elif (button1["text"] == "0" and button2["text"] == "0" and button3["text"] == "0"):
		button1.configure(background="red")
		button2.configure(background="red")
		button3.configure(background="red")
		n = int(playerO.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo("Winner O", "You have just won a game")
		reset()
	elif (button4["text"] == "0" and button5["text"] == "0" and button6["text"] == "0"):
		button4.configure(background="red")
		button5.configure(background="red")
		button6.configure(background="red")
		n = int(playerO.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo("Winner O", "You have just won a game")
		reset()
	elif (button7["text"] == "0" and button8["text"] == "0" and button9["text"] == "0"):
		button7.configure(background="red")
		button8.configure(background="red")
		button9.configure(background="red")
		n = int(playerO.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo("Winner O", "You have just won a game")
		reset()
	elif (button1["text"] == "0" and button4["text"] == "0" and button7["text"] == "0"):
		button1.configure(background="red")
		button4.configure(background="red")
		button7.configure(background="red")
		n = int(playerO.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo("Winner O", "You have just won a game")
		reset()
	elif (button2["text"] == "0" and button5["text"] == "0" and button8["text"] == "0"):
		button2.configure(background="red")
		button5.configure(background="red")
		button8.configure(background="red")
		n = int(playerO.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo("Winner O", "You have just won a game")
		reset()
	elif (button3["text"] == "0" and button6["text"] == "0" and button9["text"] == "0"):
		button3.configure(background="red")
		button6.configure(background="red")
		button9.configure(background="red")
		n = int(playerO.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo("Winner O", "You have just won a game")
		reset()
	elif (button1["text"] == "0" and button5["text"] == "0" and button9["text"] == "0"):
		button1.configure(background="red")
		button5.configure(background="red")
		button9.configure(background="red")
		n = int(playerO.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo("Winner O", "You have just won a game")
		reset()
	elif (button3["text"] == "0" and button5["text"] == "0" and button7["text"] == "0"):
		button3.configure(background="red")
		button5.configure(background="red")
		button7.configure(background="red")
		n = int(playerO.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo("Winner O", "You have just won a game")
		reset()


def reset():
	button1["text"] = ""
	button2["text"] = ""
	button3["text"] = ""
	button4["text"] = ""
	button5["text"] = ""
	button6["text"] = ""
	button7["text"] = ""
	button8["text"] = ""
	button9["text"] = ""
	
	button1.configure(background="gainsboro")
	button2.configure(background="gainsboro")
	button3.configure(background="gainsboro")
	button4.configure(background="gainsboro")
	button5.configure(background="gainsboro")
	button6.configure(background="gainsboro")
	button7.configure(background="gainsboro")
	button8.configure(background="gainsboro")
	button9.configure(background="gainsboro")


def NewGame():
	reset()
	playerX.set(0)
	playerO.set(0)


lblTitleX = Label(RightFrame1, font=("arial", 50, "bold"), text="Player X :", bd=21, bg="Cadet Blue", fg="Cornsilk",
                  justify=CENTER)
lblTitleX.grid(row=0, column=0, sticky=W)

txtPlayerX = Entry(RightFrame1, font=("arial", 40, "bold"), bd=2, fg="black", textvariable=playerX, width=14, justify=LEFT)
txtPlayerX.grid(row=0, column=1)

lblTitleO = Label(RightFrame1, font=("arial", 50, "bold"), text="Player O :", bd=21, bg="Cadet Blue", fg="Cornsilk",
                  justify=CENTER)
lblTitleO.grid(row=1, column=0, sticky=W)

txtPlayerO = Entry(RightFrame1, font=("arial", 40, "bold"), bd=2, fg="black", textvariable=playerO, width=14, justify=LEFT).grid(
	row=1, column=1)

btnReset = Button(RightFrame2, text="Reset", font=("Times", 26, "bold"), height=3, width=20, bg="gainsboro", command=reset)
btnReset.grid(row=0, column=0)

btnNewGame = Button(RightFrame2, text="New Game", font=("Times", 26, "bold"), height=3, width=20, bg="gainsboro", command=NewGame)
btnNewGame.grid(row=1, column=0)

button1 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(LeftFrame, text="", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

root.mainloop()
