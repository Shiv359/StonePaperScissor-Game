import random
from tkinter import *

root=Tk()
root.geometry("655x433")
root.title("Stone Paper Scissors")

USER_SCORE=0
COMP_SCORE=0
USER_CHOICE=""
COMP_CHOICE=""

def choice_to_number(choice):
    rps={'rock':0,'paper':1,'scissor':2}
    return rps[choice]

def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You Win")
        USER_SCORE+=1
    else:
        print("Comp wins")
        COMP_SCORE+=1
        textarea=Text(root,height=12,width=30)
        textarea.grid(column=4,row=8)
        answer="Your Choice :{uc}\nComputer choice:{cc}\nYour Score:{u}\ncomputer score:{c}".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)
        textarea.insert(END,answer)

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)



b1=Button(root,text="Rock",command=rock)
b2=Button(root,text="Paper",command=paper)
b3=Button(root,text="Scissor",command=scissor)

b1.grid(row=1,column=1,)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)




root.mainloop()