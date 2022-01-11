
from tkinter import*
import random
import time
import webbrowser
import os 
import time
from pynput import mouse
import os
import pyautogui as pt
import signal
from pynput.keyboard import Key, Listener

def func_test_1():
    webbrowser.open("https://www.youtube.com/watch?v=rwSJwzE7lAg")

def func_test_2():
    webbrowser.open("https://www.youtube.com/watch?v=fcZXfoB2f70")

def func_test_3():
    webbrowser.open("https://www.youtube.com/watch?v=tZGpRd-t7jg")

def func_test_4():
    webbrowser.open("https://www.youtube.com/watch?v=ZYzbalQ6Lg8")

root = Tk()


def intro():
    print("Welcome to the program")

def current_position():
    return [root.winfo_pointerx(), root.winfo_pointery()]


def choosetime():
    usrin = input("Please choose one of the time management programs :D: (options : 25,50,90 mins) ")
    if "25" in usrin:
        print("25min selected")
        chooseinput()
        time.sleep(3)
        TFMIN()
    

    elif "50" in usrin:
        print("50min selected")
        FTMIN()
    elif "90" in usrin:
        print("90 min selected")
        NTMIN()

    else:
        print("something went wrong! retry :)")
        choosetime()


def chooseinput():
    usrin = input("Please choose one of the input blocking method:\n1.mouse only\n2.keyboard only\n3.both mouse and keyboard\nEnter either 1,2 or 3: ")
    if "1" in usrin:
        print("disabling mouse")
        blockmouse()
    elif "2" in usrin:
        print("disabling keyboard")
        blockkb()
    elif "3" in usrin:
        print("both disabled!!")
        blockboth()


def blockkb():
    ok()


def klog(key):
    # print("no")
       #check variables
    count = 1
    kds = "Key.shift"
    kdsr = "Key.shift_r"
    kdc = "Key.ctrl"
    kdce = "Key.ctrl_r"
    lak = "Key.left"
    rak = "Key.right"
    pressed_key = str(key).replace("'", "")
    # print(pressed_key)

    if key == Key.esc:
       exit()
    elif pressed_key == kds:
       print("detected kb")
       
    elif pressed_key == lak:
        print("detected kb")
        exit()
    elif pressed_key == rak:
        print("detected kb")
        exit()
    elif pressed_key == kdc:
       exit()
    elif pressed_key == kdce:
        print("detected kb")
        exit()
    else: 
        print("detected kb")
        exit()
   

def ok():
 with Listener(on_press=klog) as listener:
    listener.join()
    
def blockmouse():
        
        while True:
            time.sleep(0.5)
            pos2 = current_position()
            if not pos1 == pos2:
                # run a command:
                my_list = [func_test_1, func_test_2, func_test_3, func_test_4]
                random.choice(my_list)()
            pos1 = pos2
                

def blockboth():
    os.system("python3 kb.py &")
    os.system("python3 mouse.py &")
   
    
def TFMIN():
        print("starting the 25min timer, if you are found properly focusing on your work during this period and not getting distracted then you will be awarded 25 Shib-Inu as a prize :D but if you are found lacking then you wont recieve anything and you may retry")
        pos1 = current_position()
        t_end = time.time() + 60 * 25
        while time.time() < t_end :
            blockmouse()
               
 
def FTMIN():
    pass

def NTMIN():
    pass



intro()
choosetime()
