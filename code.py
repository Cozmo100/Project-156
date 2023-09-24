from tkinter import *
from PIL import ImageTk , Image
import random

root = Tk()
root.geometry('800x400')

img1 = ImageTk.PhotoImage(Image.open('buttonblue.png'))
img2 = ImageTk.PhotoImage(Image.open('buttonblue.png'))
img3 = ImageTk.PhotoImage(Image.open('PIKACHUCARD.webp'))

l1 = Label(root, text = 'Player 1')
l1.place(relx = 0.2 , rely = 0.4 , anchor = CENTER)

l2 = Label(root, text = 'Player 2')
l2.place(relx = 0.8 , rely = 0.4 , anchor = CENTER)



p1 = 0
def f1():
    global p1
    r = random.randint(1,6)
    l5['text']= 'Player 1 Score : ' + str(r)
    p1 = p1 + r
    l3['text']= p1


p2 = 0
def f2():
    global p2
    r1 = random.randint(1,6)
    l5['text']= 'Player 2 Score : ' + str(r1)
    p2 = p2 + r1
    l4['text']= p2

b1 = Button(root, image = img1, command = f1)
b1.place(relx = 0.2 , rely = 0.5 , anchor = CENTER)

b2 = Button(root, image = img2, command = f2)
b2.place(relx = 0.8 , rely = 0.5 , anchor = CENTER)

b3 = Button(root, image = img3, command = f2)
b3.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)

root.mainloop()