from pynput import mouse
import os
import pyautogui as pt
import signal

def checkpid():
    opfil = open("/home/jay/Desktop/app[linux]/PIDOFKBSEC.txt", "r")
    opfil = int(opfil.read())
    # print(f"mouse val: " + opfil)
    try:
     os.kill(opfil, signal.SIGKILL)
     print("kb ended")

    except:
        print("process not found - mouse")


def pidret():
    valpid = os.getpid()
    wrfil = open("/home/jay/Desktop/app[linux]/PIDOFMOUSESEC.txt", "w+")
    wrfil.write(str(valpid))
    wrfil.close()



def macti():
 mr = mouse.Button.right
 ml = mouse.Button.left
 with mouse.Events() as events:
    for event in events:
        try:
         if event.button == ml:
            print("detected")
            checkpid()
            exit()
           
            
         elif event.button == mr:
            print("user bailout!")
            checkpid()
            exit()
          

        except:
            print("detected")
            checkpid()
            exit()
           


if __name__ == "__main__":
   pidret()
   print("ok")
   macti()
   