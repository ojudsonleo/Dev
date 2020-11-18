# code by theinsidecodes
from tkinter import *
import tkinter.font as font
from tkinter import scrolledtext
import smtplib
from email.message import EmailMessage
msg = EmailMessage()

root = Tk()
root.geometry('550x440')
root.title("EMAIL APPLICATION BY THEINSIDECODES")
myFont = font.Font(size=16)
large_font = ('Verdana',16)

account = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
msgbody = StringVar()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

def sendemail():
    sender = account.get()
    recepient = receiver.get()
    sub = subject.get()
    pswrd = password.get()
    message = text_area.get('1.0', 'end-1c')

    msg.set_content(message)

    msg['Subject'] = sub
    msg['From'] = sender
    msg['To'] = recepient

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com' , 465)
    server.login(sender, pswrd)
    server.send_message(msg)
    server.quit()

labelemail = Label(root,text="Email Account", justify = LEFT, bg = "yellow", font = "Verdana 10 bold")
labelemail.grid(row = 0, column = 0)

account_entry = Entry(root, textvariable = account, width = 30, font=large_font)
account_entry.grid(row = 0, column = 1)

labelpassword = Label(root , text="Password", justify = LEFT, padx = 10, bg = "yellow", font = "Verdana 10 bold")
labelpassword.grid(row=1 , column=0)

password_entry = Entry(root , textvariable=password, width = 30, font=large_font, show = '*')
password_entry.grid(row=1 , column=1)

Label(root, text = "================PLEASE LOGIN FIRST==================", bg = "yellow", font = "Verdana 10 bold").grid(row = 2, column = 0, columnspan = 2,padx = 10, pady = 10)

label1 = Label(root, text = "To", justify = LEFT, padx = 30, bg = "yellow", font = "Verdana 10 bold")
label1.grid(row = 3, column = 0)

receiver_entry = Entry(root,  width = 30, font=large_font, textvariable = receiver)
receiver_entry.grid(row = 3, column = 1)

label2 = Label(root, text = "Subject", justify = LEFT, padx = 10, bg = "yellow", font = "Verdana 10 bold")
label2.grid(row = 4, column = 0)

Subject_entry = Entry(root,  width = 30, font=large_font, textvariable = subject)
Subject_entry.grid(row = 4, column = 1)

text_area = scrolledtext.ScrolledText(root, wrap=WORD, width=50, height=10, font=("Times New Roman",15))
text_area.grid(row = 5, columnspan = 2, pady=10, padx = 10)

send_button = Button(root, text = "Send",  relief='groove', width  = 10, command = sendemail)
send_button.grid(row = 6, column = 0)

root.mainloop()