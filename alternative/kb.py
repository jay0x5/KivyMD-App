from pynput.keyboard import Key, Listener
import os
import pyautogui as pt
import os
import signal

def checkpid():
    opfil = open("/home/jay/Desktop/app[linux]/PIDOFMOUSESEC.txt", "r")
    opfil = int(opfil.read())
    # print(f"mouse val: " + opfil)
    try:
     os.kill(opfil, signal.SIGKILL)
     print("mouse ended")

    except:
        print("process not found - kb")


def pidret():
    valpid = os.getpid()
    wrfil = open("/home/jay/Desktop/app[linux]/PIDOFKBSEC.txt", "w+")
    wrfil.write(str(valpid))
    wrfil.close()

   

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
        print("detected kb!")
        checkpid()
        exit()

    elif pressed_key == kds:
       print("detected kb")
       checkpid()
       exit()

    elif pressed_key == lak:
        print("detected kb")
        checkpid()
        exit()

    elif pressed_key == rak:
        print("detected kb")
        checkpid()
        exit()

    elif pressed_key == kdc:
        print("detected kb")
        checkpid()
        exit()
    

    elif pressed_key == kdce:
        print("detected kb")
        checkpid()
        exit()
       

    else: 
        print("detected kb")
        checkpid()
        exit()

    # elif len(pressed_key) == count:
    #     print("detected kb")
    #     takesss()
    #     exit()




def ok():
 with Listener(on_press=klog) as listener:
    listener.join()
  

 



if __name__ == "__main__":
    print("activating...")
    pidret()
    ok()