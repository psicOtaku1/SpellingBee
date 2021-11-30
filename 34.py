import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
import random

team1=2
team2=2
team3=2
team4=2
Cword='a'

easy=['easy','big','the','cat','dog','door','open','close','chair','table','food','pencil','cow','milk','at','sister','brother','cousin','school','build','circle','little','Back','Children','called','people','looked','house','circle','certain','earth','guard','special']
medium=['rainbow','beautiful','everywhere','never','welcome','homework','country','dancing','culture','horse','tomorrow','yesterday','sentence','breath','knowledge','weight','subtraction','addition','forward','accident','actual','although','complete','grammar','reign','medicine','interesting','perhaps','extreme','consider','continue','different','disappear']
hard=['congratulations','flower','flour','were','wear','grade','great','grape','ghost','mysterious','thunder','particular','various','therefore','businesses','important','island','experiment','occasionally','opposite','remember']

def newWord():
    global Cword
    NuDiff=random.randint(1, 3)
    if NuDiff==1:
        diff=easy
    elif NuDiff==2:
        diff=medium
    elif NuDiff==3:
        diff=hard
    Nuword=random.randint(0, len(diff)-1)
    Cword=diff[Nuword]
    print(Cword)
def checkWord():
    global Cword
    if inputWord.get()==Cword:
        inputWord.configure(bg='#90ee90')
        lableWord.configure(bg='#90ee90')
    else:
        inputWord.configure(bg='#ff7f7f')
        lableWord.configure(bg='#ff7f7f')
    newWord()

def pointT1():
    global team1
    team1=team1 + 1
    scoreT1.configure(text=f'{team1-3}', width=team1*4)
    buttonT1.configure(width=team1*4)
def pointT2():
    global team2
    team2=team2 + 1
    scoreT2.configure(text=f'{team2-3}', width=team2*4)
    buttonT2.configure(width=team2*4)
def pointT3():
    global team3
    team3=team3 + 1
    scoreT3.configure(text=f'{team3-3}', width=team3*4)
    buttonT3.configure(width=team3*4)
def pointT4():
    global team4
    team4=team4 + 1
    scoreT4.configure(text=f'{team4-3}', width=team4*4)
    buttonT4.configure(width=team4*4)

##setup
root=tk.Tk()
root.title('Spelling Bee - St. George')
root.iconbitmap('./logo.ico')
root.geometry('800x600')
root.configure(bg='#becded')
##root.attributes('-fullscreen',True)

newWord()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
midleH=(screen_height/10)*8
pixel=tk.PhotoImage(width=1, height=1)

##fonts
heading = Font(size=40, weight='bold')
heading2 = Font(size=20)
bold = Font(weight='bold')

##top
top=tk.Canvas(root, bg='#1e325b', width=screen_width, height=screen_height/10)
top.pack(expand=1)
logo=ImageTk.PhotoImage(Image.open("logo.png").resize((90, 110)))
top.create_image(0, 0, image=logo, anchor=NW)
top.create_text(100, 50, anchor=W, text='St. Gearge Spelling Bee', fill='white', font=heading)

##mid
#frame1
mid=tk.Frame(root, bg='#becded', width=screen_width, height=(screen_height/10)*8)
mid.pack(expand=1)
midH=tk.Label(mid, bg='#becded', image=pixel, width=1, height=int((screen_height/10)*8))
midH.pack(expand=1, side='left')

#word input
word=tk.Frame(mid, width=screen_width)
word.pack(expand=1)
wordsH=tk.Label(word, bg='#becded', image=pixel, width=1, height=int(midleH/5))
wordsH.pack(expand=1, side='left')

inputWord=tk.Entry(word, bg='white', font=heading2)
inputWord.pack(side='left', fill='both')
lableWord=tk.Button(word, text='Check Spelling', font=heading2, command=checkWord)
lableWord.pack(side='right', fill='both')

#scores
scores=tk.Frame(mid, bg='#becded')
scores.pack(expand=1)
scoresH=tk.Label(scores, bg='#becded', image=pixel, width=1, height=int((midleH/3)*2))
scoresH.pack(expand=1, side='left')

buttonT1=tk.Button(scores, text='Malala', font=bold, bg='red', command=pointT1)
buttonT1.pack()
scoreT1=tk.Label(scores, font=bold, bg='red')
scoreT1.pack(expand=1, fill='y')

buttonT2=tk.Button(scores, text='Shakespeare', font=bold, bg='blue', command=pointT2)
buttonT2.pack()
scoreT2=tk.Label(scores, font=bold, bg='blue')
scoreT2.pack(expand=1, fill='y')

buttonT3=tk.Button(scores, text='Marie Curie', font=bold, bg='yellow', command=pointT3)
buttonT3.pack()
scoreT3=tk.Label(scores, font=bold, bg='yellow')
scoreT3.pack(expand=1, fill='y')

buttonT4=tk.Button(scores, text='Mandela', font=bold, bg='green', command=pointT4)
buttonT4.pack()
scoreT4=tk.Label(scores, font=bold, bg='green')
scoreT4.pack(expand=1, fill='y')

##bot
bot=tk.Canvas(root, bg='#1e325b', width=screen_width, height=screen_height/10)
bot.pack(expand=1, side='bottom')

root.mainloop()