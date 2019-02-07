#!/usr/bin/env python3
import time, os , sys
import threading

response = None

def timer(seconds):
    while True:
        try:
            timer = abs(seconds)
        except KeyboardInterrupt:
            break
        except: 
            print("Not a number!")
            break
        while timer > -1 :     
            m, s = divmod(timer,60)
            h, m = divmod(m,60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2)+ ":" +str(s).zfill(2)
            print(time_left + "\r" , end=" ")
            time.sleep(1)
            timer -= 1
        lockScreen()
        break

def quit():
    while True:
        global response
        response = input()
        if response == 'q':
            sys.exit()   
    
def lockScreen():
    os.system("osascript -e 'tell application \"Finder\" to sleep'")

def startTiming(seconds):
        thread1 = threading.Thread(target=timer,args=[seconds])
        thread1.daemon = True
        thread1.start()

def waitToQuit(seconds):
    userInputThread = threading.Thread(target=quit)
    userInputThread.daemon = True
    userInputThread.start()
    userInputThread.join(seconds+1)
    t=threading.Thread(target=sys.exit)
    t.setDaemon(True)
    t.start()

def minuteToSeconds(seconds):
    return abs((int(seconds) * 60))

if __name__ == "__main__":
    timming = False
    seconds = 0
    while timming == False:
        uin = input("Timer in minutes: ")
        try:
            seconds = minuteToSeconds(uin)
            startTiming(seconds)
            timming = True
        except: 
            if uin == "q":
                sys.exit()
            else:
                print("Enter number of minutes or \"q\" to quit")
            continue
    waitToQuit(seconds+2)
    pass