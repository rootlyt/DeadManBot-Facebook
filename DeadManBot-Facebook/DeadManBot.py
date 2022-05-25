import tkinter as deadmanswitchbot
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def job():
    status.config(text="Bot starting .. please wait until it logout.")
    # deadmanswitchbot.messagebox.showinfo('Browser will be opened','Window will be open, please let the bot do its thing')
    import bot_ok.py as bot_ok
    # deadmanswitchbot.messagebox.showinfo('Done','Browser exiting, your last word has been posted.')
    root.destroy()

def countdown(time, msg='Counting down'):
    
    time -= 1
    status.config(text=f'{msg} ({time}sec)')

    if time != 0:
        root.after(1000, countdown, time)

    else:
        job()  # if job is blocking then create a thread


root = deadmanswitchbot.Tk()
root.title('DeadManBot Facebook')
root.resizable(False, False)


canvas1 = deadmanswitchbot.Canvas(root, width = 300, height = 300, bg='black')
canvas1.pack()

label1 = deadmanswitchbot.Label(root, text='DeadmanSwitchBot',bg='black',fg='white')
label1.config(font=('Arial', 14))
canvas1.create_window(150, 20, window=label1)

label2 = deadmanswitchbot.Label(root, text='This bot will counting down until 24H\nto automatically post your last word.\nYou can click the red button to confirm now,\nor yellow to cancel the countdown',bg='black',fg='white')
label2.config(font=('Arial', 9))
canvas1.create_window(150, 250, window=label2)

def ExitApplication():
    MsgBox = deadmanswitchbot.messagebox.askquestion ('Im still alive','It looks like you are still alive, exit app?',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        deadmanswitchbot.messagebox.showinfo('Return','You will now return to the application screen')

def LaunchInformation():
    deadmanswitchbot.messagebox.showinfo('Browser will be opened','Window will be open, please let the bot do its thing')
    import bot_ok.py as bot_ok
    deadmanswitchbot.messagebox.showinfo('Done','Browser exiting, your last word has been posted.')
    root.destroy()


def About():
    deadmanswitchbot.messagebox.showinfo('About DeadManBot','This program will post your last word to your status profile.\nTo edit your last word, you can edit the lastword.txt file on the directory,\nThis app will automatically count until 24H waiting your response to cancel the countdown\nor click red button then browser will be opened and release your lastword,\nplease let the bot do its thing')

        
button1 = deadmanswitchbot.Button (root, text='Im still here(EXIT)',command=ExitApplication,bg='yellow',fg='black')
canvas1.create_window(150, 165, window=button1)

button2 = deadmanswitchbot.Button (root, text='Im no longer here',command=LaunchInformation,bg='red',fg='white')
canvas1.create_window(150, 115, window=button2)

button3 = deadmanswitchbot.Button (root, text='What is this?',command=About,bg='blue',fg='white')
canvas1.create_window(150, 65, window=button3)


status = deadmanswitchbot.Label(root)
status.pack()

countdown(10)

root.mainloop()