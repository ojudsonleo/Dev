from tkinter import*
import random
a=Tk()
a.geometry('700x700')
p1=random.randint(0,680)
p1=random.randint(0,680)
a.title("Bouncing Ball")
a.config(bg='black')
x1=p1
y1=p1
i1=10
j1=10
p2=250
v=400
c2=Canvas(a,width=90,height=10,bg='brown',highlightthickness=0)
c3=Canvas(a,width=90,height=10,bg='brown',highlightthickness=0)
c4=Canvas(a,width=90,height=10,bg='brown',highlightthickness=0)
c5=Canvas(a,width=90,height=10,bg='brown',highlightthickness=0)
c6=Canvas(a,width=90,height=10,bg='brown',highlightthickness=0)
c7=Canvas(a,width=10,height=90,bg='brown',highlightthickness=0)
c8=Canvas(a,width=10,height=90,bg='brown',highlightthickness=0)
c2.place(x=50,y=60)
c3.place(x=600,y=100)
c4.place(x=300,y=300)
c5.place(x=200,y=200)
c6.place(x=460,y=200)
c7.place(x=10,y=350)
c8.place(x=680,y=350)
c1=Canvas(a,width=90,height=30,bg='brown',highlightthickness=0)
score=0
h=0
sc=Label(a,text='score   '+str(score),font='vardana 10',bg='black', fg='green')
sc.place(x=5,y=2)
hs=Label(a,text='higest score   '+str(h),font='vardana 10',bg='black', fg='green')
hs.place(x=70,y=2)
c1.place(x=350,y=670)
class m:
   def __init__(self):
      self.c=Canvas(a,width=35,height=35,bg='orange',highlightthickness=0)
      self.mv()
   def mv(self):
      i=random.randint(1,5)
      j=random.randint(5,10)
      global x1,y1,i1,j1,p2,score,h
      self.c.place(x=x1,y=y1)
      x1=i1+x1
      y1=y1+j1
      if x1>=680:
         self.c.config(bg='green')
         i1=-i
      elif x1<=0:
         self.c.config(bg='#963258')
         i1=i
      if y1>=800:
         self.c.config(bg='violet')
         p1=random.randint(0,680)
         z1=random.randint(0,100)
         x1=p1
         y1=z1
         score=0
         sc.config(text='score   '+str(score))
      elif y1<=0:
         self.c.config(bg='violet')
         j1=j

      if (x1>=50 and x1<=140) and (y1>=60 and y1<=70):
         j1=-j-10
      if (x1>=600 and x1<=690) and (y1>=100 and y1<=110):
         j1=-j-10
      if (x1>=300 and x1<=390) and (y1>=300 and y1<=310):
         j1=-j-10
      if (x1>=200 and x1<=290) and (y1>=200 and y1<=210):
         j1=-j-10
      if (x1>=460 and x1<=550) and (y1>=200 and y1<=210):
         j1=-j-10
      if (x1>=0 and x1<=10) and (y1>=250 and y1<=440):
         i1=-i-10
         j1=-j-10
      if (x1>=680 and x1<=700) and (y1>=250 and y1<=440):
         i1=-i-10
         j1=-j-10


      if (x1>=p2-10 and x1<=p2+90) and (y1>=640 and y1<=670) :
         j1=-j-10
         score=score+1
         if score>h:
            h=score
         if score>1:
            c1.config(bg='brown')
            color='red'
         else:
            color='blue'
         sc.config(text='score   '+str(score))
         hs.config(text='higest score   '+str(h))
         self.c.config(bg=color)
      a.after(10,self.mv)
   def mv1(event):
      global p2
      c1.place(x=p2,y=670)
      p2=p2+20
   def mv2(event):
      global p2
      c1.place(x=p2,y=670)
      p2=p2-20
   a.bind("<Right>",mv1)     
   a.bind("<Left>",mv2)        
m()      
a.mainloop()