# note : install Pillow library before running

from tkinter import *
from PIL import ImageTk,Image
import random

# main widget
root = Tk()

root.title('Rock Paper Scissors')

root.iconbitmap('roc.ico')

root.resizable(width=False, height=False)

click = True

rHandPhoto = ImageTk.PhotoImage(file='rHand.png')
pHandPhoto = ImageTk.PhotoImage(file='pHand.png')
sHandPhoto = ImageTk.PhotoImage(file='sHand.png')

rockPhoto = ImageTk.PhotoImage(file='rock.png')
paperPhoto = ImageTk.PhotoImage(file='paper.png')
scissorsPhoto = ImageTk.PhotoImage(file='scissors.png')

winPhoto = ImageTk.PhotoImage(file='win.png')
loosePhoto = ImageTk.PhotoImage(file='loose.png')
tiePhoto = ImageTk.PhotoImage(file='tie.png')

rHandButton = ''
pHandButton = ''
sHandButton = ''

# function to choose options
def play():
    splash_root.destroy()
    global rHandButton, pHandButton, sHandButton

    rHandButton = Button(root, image=rHandPhoto, command=lambda: youPick('rock'))
    pHandButton = Button(root, image=pHandPhoto,
                         command=lambda: youPick('paper'))
    sHandButton = Button(root, image=sHandPhoto,
                         command=lambda: youPick('scissors'))

    rHandButton.grid(row=0, column=0)
    pHandButton.grid(row=0, column=1)
    sHandButton.grid(row=0, column=2)

# function to let computer choose (randomly)
def computerPick():
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

# function to give end result
def youPick(yourChoice):
    global click

    compPick = computerPick()

    if click == True:
        if yourChoice == 'rock':
            rHandButton.configure(image=rockPhoto)
            if compPick == 'rock':
                pHandButton.configure(image=rockPhoto)
                sHandButton.configure(image=tiePhoto)
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image=paperPhoto)
                sHandButton.configure(image=loosePhoto)
                click = False
            else:
                pHandButton.configure(image=scissorsPhoto)
                sHandButton.configure(image=winPhoto)
                click = False

        elif yourChoice == 'paper':
            pHandButton.configure(image=paperPhoto)
            if compPick == 'rock':
                rHandButton.configure(image=rockPhoto)
                sHandButton.configure(image=winPhoto)
                click = False
            elif compPick == 'paper':
                rHandButton.configure(image=paperPhoto)
                sHandButton.configure(image=tiePhoto)
                click = False
            else:
                rHandButton.configure(image=scissorsPhoto)
                sHandButton.configure(image=loosePhoto)
                click = False

        elif yourChoice == 'scissors':
            sHandButton.configure(image=scissorsPhoto)
            if compPick == 'rock':
                pHandButton.configure(image=rockPhoto)
                rHandButton.configure(image=loosePhoto)
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image=paperPhoto)
                rHandButton.configure(image=winPhoto)
                click = False
            else:
                pHandButton.configure(image=scissorsPhoto)
                rHandButton.configure(image=tiePhoto)
                click = False
    else:
        if yourChoice == 'rock' or yourChoice == 'paper' or yourChoice == 'scissors':
            rHandButton.configure(image=rHandPhoto)
            pHandButton.configure(image=pHandPhoto)
            sHandButton.configure(image=sHandPhoto)
            click = True



# instructions widget
def instructions():
    ins = Tk()
    ins.title('Instructions')
    ins.geometry('1024x576')

    my_label= Label(ins,
          text="Instructions",
          font="normal 40 bold",
          fg="blue").pack(pady=50)
    my_label2= Label(ins,text="click on the image to choose from \n rock paper and scissor"
                              " \n 1- Rock beats scissor "
                              "\n 2- Paper beats Rock "
                              "\n 3-Scissor beats Paper"
                              "\n If you click on any option you \n will see the result window"
                              "\n If you again click on any image \n you will be back to the start of the game",
          font="normal 18 bold",
          fg="orange").pack(pady=50)
    ready = Button(ins, text="close",
                font=10, width=10, command=ins.quit)
    ready.pack(padx=10)


# welcome and menu widget
splash_root = Tk()
splash_root.title('Splash screen!')
splash_root.geometry('1024x576')

Label(splash_root,
        text="Rock Paper Scissor",
        font="normal 60 bold",
        fg="red").pack(pady=50)

Label(splash_root,
        text="Menu",
        font="normal 40 bold",
        fg="green").pack(pady=40)

frame = Frame(splash_root)
frame.pack()
frame1 = Frame(splash_root)
frame1.pack()

b1 = Button(frame1, text="start",
            font=10, width=10,bg='black',fg='orange',command=play)

b2 = Button(frame1, text="Instructions ",
            font=10, width=15,bg='black',fg='orange',command=instructions)

b3 = Button(frame1, text="Exit",
            font=10, width=10,bg='black',fg='orange',command=splash_root.quit)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Label(splash_root,
      text="Ayush Ambhore",font="normal 25 bold",
      fg="blue").pack(side=RIGHT,pady=60)
Label(splash_root,
      text="Created by-",font="normal 20 bold",
      fg="blue").pack(side=RIGHT,pady=50)


# execution of everything
mainloop()

