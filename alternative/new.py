import os 
import time
from pynput import mouse
import os
import pyautogui as pt
import signal
from pynput.keyboard import Key, Listener


def intro():
    print("Welcome to the program")


def choosetime():
    usrin = input("Please choose one of the time management programs :D: ")
    if "25" in usrin:
        print("25min selected")
        chooseinput()
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
        mr = mouse.Button.right
        ml = mouse.Button.left
        with mouse.Events() as events:
            for event in events:
                try:
                    if event.button == ml:
                        exit()

                    elif event.button == mr:
                        exit()
    
                except:
                    exit()
                

def blockboth():
    os.system("python3 kb.py &")
    os.system("python3 mouse.py &")
   
    
def TFMIN():
        print("starting the 25min timer, if you are found properly focusing on your work during this period and not getting distracted then you will be awarded 25 Shib-Inu as a prize :D but if you are found lacking then you wont recieve anything and you may retry")
        blockmouse()
               
 
def FTMIN():
    pass

def NTMIN():
    pass



intro()
choosetime()

