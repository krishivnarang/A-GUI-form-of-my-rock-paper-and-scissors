# Project of a simple game of Rock Paper and Scissors
# Now in updated window form :D
import tkinter as t
import random as r
# Global variables
l,pcount,ccount=[],0,0
## Difficulty Functions

def baby(player):
    """
    A simple difficulty level where the player always wins.
    """
    if player.lower()=="rock": return "scissors"
    elif player.lower()=="paper": return "rock"
    elif player.lower()=="scissors": return "paper"
    
def medium(player):
    return r.choice(["rock","paper","scissors"])

def hard(l):
    # This will check for the favourite move of the player thus punishing them if they are too carefree
    if len(l)==0: return "paper" 
    getback="paper"
    count={"rock":0,"paper":0,"scissors":0}
    for move in l: count[move]+=1
    common=max(count,key=count.get) # Checks for the player's most commom , i.e., favourrite move
    if r.random()<=0.15: return r.choice(["rock","paper","scissors"])
    # The above line is only here to give the player a fighting and winning chance because without this line , THE HOUSE ALWAYS DRAWS (WINS)
    elif common=="rock": getback="paper"
    elif common=="paper": getback="scissors"
    elif common=="scissors": getback="rock"
    recent=l[-3:]
    if len(recent)==3 and recent[0]==recent[1]==recent[2]:
        if recent[0]=="rock": return "paper"
        if recent[0]=="paper": return "scissors"
        if recent[0]=="scissors": return "rock"
    return getback

# The actual visible part
def playing(player) :
    global l,pcount,ccount
    mode=difficultymode.get()
    l.append(player) # the variable check roughly translates to checkmate
    if mode==1: check=baby(player)
    elif mode==2: check=medium(player)
    elif mode==3: check=hard(l)
    upd(check)
    # Who won ? Program or by some error the player ?
    res=""
    if player==check: 
        res="Twas' a draw !"
        pcount+=1
        ccount+=1 #extending the below line into multiple lines with "\"
    elif (player=="rock" and check=="paper") or \
         (player=="scissors" and check=="rock") or \
         (player=="paper" and check=="scissors") :
        res="The program won, you lost"
        ccount+=1
    else : 
        res="You won !!"
        pcount+=1 
    stats.config(text=f"You: {player.title()} vs Program: {check.title()}\n\n{res}")
    score.config(text=f"Challenger: {pcount}  |  Program: {ccount}")

def upd(move):
    if move in jraphics: googly.config(image=jraphics[move],text="",width=0,height=0) # Necessary to update height and width of images specifically otherwise they appear only as a part of their corners
    else : googly.config(image="",text=f"[{move.upper()}]",width=20,height=7) # Backup option in case images are not found
def ragequit():
    global l,pcount,ccount
    l,pcount,ccount=[],0,0
    score.config(text=f"Challenger: {pcount}  |  Program: {ccount}")
    stats.config(text="Choose your move to start !")
    googly.config(image="",text="Waiting for move....")

# The thing were everything fits
tictaccer=t.Tk()
tictaccer.title("The Rock , Paper , and also Scissors Game")
tictaccer.geometry("500x600")
hand=t.PhotoImage(file="hand.png")
tictaccer.iconphoto(True,hand)
jraphics={}
try:
    jraphics["rock"]=t.PhotoImage(file="rock.png")
    jraphics["paper"]=t.PhotoImage(file="papers.png")
    jraphics["scissors"]=t.PhotoImage(file="scissor.png")
except Exception: print("The images ran away ! Using low power (text-only) mode :(")
# Heading title of game , not really
t.Label(tictaccer,text="+~The Game in Question~+",font=("Arial",20,"bold")).pack(pady=10) 
t.Label(tictaccer,text="Choose your Fight !").pack(pady=5)
diffy_cult=t.Frame(tictaccer)
diffy_cult.pack(pady=5)
difficultymode=t.IntVar(value=2)
t.Radiobutton(diffy_cult,text="Baby mode",variable=difficultymode,value=1).pack(side=t.LEFT,padx=10)
t.Radiobutton(diffy_cult,text="The Classics",variable=difficultymode,value=2).pack(side=t.LEFT,padx=10)
t.Radiobutton(diffy_cult,text="HARDEST",variable=difficultymode,value=3,fg="red").pack(side=t.LEFT,padx=10)
googly=t.Label(tictaccer,text="[Program's move]",font=("Arial",14),bg="#ddd",width=20,height=7)
googly.pack(pady=20)
stats=t.Label(tictaccer,text="Choose a move to fight !",font=("Arial",14))
stats.pack(pady=20)
score=t.Label(tictaccer,text="Challenger: 0  |  Program: 0",font=("Arial",14))
score.pack(pady=20)
# Clickety-Clack , since buttons have to be updated or something i dunno i just work here just kidding
butts=t.Frame(tictaccer)
butts.pack(pady=20,fill=t.X)
def buttery(text,move):
    return t.Button(butts,text=text,font=("Arial",12),width=10,command=lambda: playing(move))
# Buttons to make choices
buttery("ROCK","rock").pack(side=t.LEFT, padx=20, expand=True)
buttery("PAPER","paper").pack(side=t.LEFT, padx=20, expand=True)
buttery("SCISSORS","scissors").pack(side=t.LEFT, padx=20, expand=True)
t.Button(tictaccer,text="Reset Scores",command=ragequit,fg="red").pack(pady=5)
tictaccer.mainloop()