# python gmail application



from tkinter import * 
import smtplib
from email.mime.text import MIMEText
from tkinter import messagebox
import sys

global Home
Home = Tk()
Home.geometry("800x500")

def getting_values():
    from_email = e1.get()
    to_email = e2.get()
    subject = e3.get()
    message = e4.get("1.0",END)

    msg = MIMEText(message)
    from_addr = from_email
    to_addr = to_email

    msg['from'] = from_addr
    msg['To'] = to_addr
    msg['subject'] = subject
    
    server = smtplib.SMTP('smtp.gmail.com',3306)#Here type your port no.. 

    '''
    # for check Desktop Port open cmd and type "netstat -a",
    or open google and type steps to check port no
    Thank U
    '''




    server.starttls()
    server.login(from_addr,"*****")#and here type your gmail account password..not in double cots and stars...

    send = server.send_message(msg)

    if send:
        messagebox.showinfo("success","email is send")
    else:
        messagebox.showinfo("Error","Check Your internet connection")



    server.quit()






labelfont = ('Lucida Console',10,'bold')

l1_name = Label(Home, text = 'Enter your Email')
l1_name.grid(padx = 40, pady = 10 ,row = 1, column = 0)
l1_name.config(font = labelfont)

#from_email = StringVar()
e1 = Entry(Home,width = 40)
e1.grid(padx = 20, pady = 10 ,row = 1 , column = 3)

l2_name = Label(Home, text = 'Enter Recipient Email')
l2_name.grid(padx = 40, pady = 10 ,row = 5, column = 0)
l2_name.config(font = labelfont)

#to_email = StringVar()
e2 = Entry(Home,width = 40)
e2.grid(padx = 20, pady = 10 ,row = 5 , column = 3)

l3_name = Label(Home, text = 'Subject')
l3_name.grid(padx = 40, pady = 10 ,row = 6, column = 0)
l3_name.config(font = labelfont)

subject = StringVar()
e3 = Entry(Home,width = 40,textvar = subject)
e3.grid(padx = 20, pady = 10 ,row = 6 , column = 3)

l4_name = Label(Home, text = 'Enter Your Message')
l4_name.grid(padx = 40, pady = 10 ,row = 7, column = 0)
l4_name.config(font = labelfont)

e4 = Text(Home,width = 50,height = 10)
e4.grid(padx = 20, pady = 10 ,row = 7 , column = 3)


b2 = Button(Home, text = 'send',bg='brown',fg='white',width = 20,command = getting_values)
b2.grid(padx = 20, pady = 10 ,row = 8 , column = 3)


b2 = Button(Home, text = 'Exit',bg='brown',fg='white',width = 20,command = sys.exit)
b2.grid(padx = 20, pady = 10 ,row = 10 , column = 3)


Home.mainloop()

# code in description...thank u...

