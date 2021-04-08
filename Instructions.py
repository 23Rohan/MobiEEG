from tkinter import *
from tkinter import messagebox
import os
import pygame
import random
import time
from PIL import ImageTk, Image

t=3
counter = 0
pygame.init()
pygame.mixer.init()
mute = True
taskCounter = 0
arrowCounter = 10

def exGui():
    response = messagebox.askyesno(message=exMessage)
    if response == 1:
        import ConnToCap
        ConnToCap.exitFromInstruction()
        root.destroy()
        
def ex():
    import ConnToCap
    ConnToCap.exitFromInstruction()
    root.destroy()

def disMute():
    global btnMute
    btnMute.destroy()


def countDown():
    global lblCount
    global t
    global counter
    lblCount = Label(root, width=28, height=5, bg='black', fg='white')
    lblCount.grid(column=0, row=0)
    if t>-1:
        t=t-1
        GuiFrame.config(font=("Arial", 20), text='-')
        if t>-1:
            lblCount.configure(text=t+1, font=("Arial", 150), width=2, height=0)
            pygame.mixer.music.load("Sounds\SoftBeep.mp3")
            pygame.mixer.music.play()
            lblCount.after(1000, countDown)
        else:
            lblCount.configure(text='+', font=("Arial", 280), width=2, height=0)
            pygame.mixer.music.load("Sounds\SoftBeep2.mp3")
            pygame.mixer.music.play()
            # Carmen watns to have controll over the time of the Cross
            lblCount.after(carmenCtrl, countDown)
        
    elif t==-1:
        counter = counter + 1
        checkInst(counter)

def checkInst(cc):
    global arrowCounter
    global taskCounter

    if cc==1:
        instrOpenEye()
    if cc==2:
        instrCloseEye()
    if cc==3:
        instrPause(carmenB4Imagin) # It should be 3000 = 3 seconds
    if cc==4:
        instrMessage()
    if cc==5:
        taskCounter = taskCounter +1
        arrowCounter =  carmenArrowCounter      # Carmen wants it from 60
        # GuiFrame.config(font=("Arial", 20), text='-')
        instrArrows()
    if cc==6:
        instrPause(carmenBtwAndB) # It should be around 120000 = 120 seconds/2 minutes
    if cc==7:
        taskCounter = taskCounter +1
        # GuiFrame.config(font=("Arial", 20), text='-')
        arrowCounter= carmenArrowCounter
        instrArrows()
    if cc==8:
        instrPause(carmenAfterImagin) # It should be 10000 = 10 seconds
    if cc==9:
        instrOpenEye()
    if cc==10:
        instrThanks()

def doInstr():
    global t
    t=0
    # GuiFrame.configure(bg='black', text='-')
    lblCount.config(text='')
    lblCount.after(1000,countDown)

def instrOpenEye():
    global taskCounter
    taskCounter = taskCounter + 1
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text=txtEyeOpen)
    if mute == True:
        pygame.mixer.music.load("Sounds\KeepEyeOpen.mp3")
        pygame.mixer.music.play()
    lblCount.after(carmenEyesTask, doInstr)
    
def instrCloseEye():
    global taskCounter
    taskCounter = taskCounter + 1
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text=txtEyeClose)
    if mute == True:
        pygame.mixer.music.load("Sounds\CloseEyes.mp3")
        pygame.mixer.music.play()
    lblCount.after(carmenEyesTask, doInstr)

def instrPause(seconds):
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text='')
    lblCount.after(seconds, doInstr)

def instrMessage():
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text=txtImagin)
    if mute == True:
        pygame.mixer.music.load("Sounds\KeepEyeOpen.mp3") # should change
        pygame.mixer.music.play()
    lblCount.after(2000,doInstr)

def arrowPause():
    lblCount.configure(text='+', font=("Arial", 280))
    pygame.mixer.music.load("Sounds\SoftBeep2.mp3")
    pygame.mixer.music.play()
    lblCount.after(carmenBtwArrows, instrArrows)

def rand():
    return random.randint(0,1)

def instrArrows():
    global arrowCounter
    global taskCounter
    # image = Image.open("Images\Eng.png")
    # bgImage = ImageTk.PhotoImage(image)
    temp = rand()
    arrow = ''
    if temp==1:
        arrow='=>'
    elif temp==0:
        arrow='<='
    
    if arrowCounter>0:
        arrowCounter=arrowCounter-1
        lblCount.configure( text=arrow, font=("Arial", 280), width=2, height=0)
        if arrowCounter == 0:
            lblCount.after(carmenArrowTime, doInstr)
        else:
            lblCount.after(carmenArrowTime, arrowPause)
    
def instrThanks():
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text=txtTnx)
    if mute==True:
        pygame.mixer.music.load("Sounds\Thanks.mp3")
        pygame.mixer.music.play()
    btnCncl.configure(text='Exit', command=ex)

def setMute():
    global mute
    if mute == True:
        mute = False
        btnMute.configure(text='-----')
    elif mute == False:
        mute = True
        btnMute.configure(text=txtMute)

def initializeGui():
    global root
    root = Tk()
    #Reading the texts from the language file
    readFile = open("LanguageSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("LanguageSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()
    global exMessage
    global txtMute
    global txtTask
    global txtEyeOpen
    global txtEyeClose
    global txtImagin
    global txtPaus
    global txtTnx
    exMessage = language[13].replace('\n', '')
    taskTitle = language[21].replace('\n', '')
    btnCncel = language[6].replace('\n', '')
    btnReady = language[22].replace('\n', '')
    txtMute = language[23].replace('\n', '')
    txtTask = language[24].replace('\n', '')
    txtEyeOpen = language[25].replace('\n', '')
    txtEyeClose = language[26].replace('\n', '')
    txtImagin = language[27].replace('\n', '')
    txtPaus = language[28].replace('\n', '')
    txtTnx = language[29].replace('\n', '')

    #Reading the time from TimeSettings file
    readFile = open("LanguageSettings\TimeSettings.txt", "r")
    temp = readFile.readlines()
    global carmenCtrl
    global carmenEyesTask
    global carmenArrowCounter
    global carmenB4Imagin
    global carmenArrowTime
    global carmenBtwArrows
    global carmenBtwAndB
    global carmenAfterImagin
    carmenCtrl = int(temp[0].replace('\n', ''))             #Beep between instructions              /2 seconds def
    carmenEyesTask = int(temp[1].replace('\n', ''))         #Close and Open eyes instructions       /2 minutes def
    carmenB4Imagin = int(temp[2].replace('\n', ''))       #Break B4 imagination task              /5 seconds def
    carmenArrowCounter = int(temp[3].replace('\n', ''))     #How many times the arrows shoud run    /60 times def
    carmenArrowTime = int(temp[4].replace('\n', ''))        #How long an arrow should be shown      /3 seconds def
    carmenBtwArrows = int(temp[5].replace('\n', ''))        #Beep between arrows                    /2 seconds def
    carmenBtwAndB = int(temp[6].replace('\n', ''))           #Break between Task A and Task B        /2 minutes def
    carmenAfterImagin =int(temp[7].replace('\n', ''))       #Break after imagination tasks          /10 seconds def
    
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()
    root.configure(bg='black')
    global GuiFrame
    GuiFrame = LabelFrame(root, text=taskTitle, bg='black', fg='white')
    GuiFrame.grid(column=0, row=0, padx= scrnWidth/30, pady= scrnHeight/10, ipadx=scrnWidth/2.2, ipady=scrnHeight/2.5)
    GuiFrame.config(font=("Arial", 20))

    btnOk = Button(root, text=btnReady,font=("Arial", 20), bg='black',
        command=lambda:[countDown(), disMute()], borderwidth=8, fg='white')
    btnOk.grid(column=0, row=0)
    global btnCncl
    btnCncl = Button(GuiFrame, text=btnCncel, font=("Arial", 20), 
        command=exGui, bg='black', borderwidth=8, fg='white')
    btnCncl.place(x=scrnWidth/1.3, y=scrnHeight/1.6)
    global btnMute
    btnMute = Button(GuiFrame, command=setMute, font=("Arial", 20), text=txtMute, bg='black', borderwidth=8, fg='white')
    btnMute.place(x=scrnWidth/1.3, y=scrnHeight/5.6)


    root.geometry(f'{scrnWidth}x{scrnHeight}+{-10}+{0}')
    root.attributes("-fullscreen", True)
    root.mainloop()

def main():
    if __name__ == '__main__':
        initializeGui()






main()