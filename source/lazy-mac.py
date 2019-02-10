#!/usr/bin/env python3
import time, os , sys, subprocess
import threading
import argparse
response = None

# Commands
sleepCommand = "sleep"
quitAllCommand = "quitall"
shutdownCommand = "shutdown"

# Applescripts
closeSafariTabsScript='''
tell application "Safari"
    repeat with i from (count of windows) to 1 by -1
        repeat with j from (count of tabs of window i) to 1 by -1
            set thistab to tab j of window i
            set foo to name of thistab
            if foo is not equal to "bar" then close thistab
        end repeat
    end repeat
end tell
tell application "Safari" to quit

'''
closeChromeTabsScript = '''
tell application "Google Chrome"
	repeat with i from (count of windows) to 1 by -1
        repeat with j from (count of tabs of window i) to 1 by -1
            set thistab to tab j of window i
            set foo to name of thistab
            if foo is not equal to "bar" then close thistab
        end repeat
    end repeat
end tell
tell application "Google Chrome" to quit

'''
quitAllScript='''
tell application "System Events"
    set selectedProcesses to (name of every process where background only is false)
end tell
repeat with processName in selectedProcesses
    if processName does not contains "Terminal"
        do shell script "Killall " & quoted form of processName
    end if
end repeat
tell application "Terminal" to quit
'''
shutdownScript ='''
tell application "System Events"
shut down
end tell
'''

sleepScript = '''
tell application "Finder" to sleep
'''

#Parser
parser = argparse.ArgumentParser(description= "Timer to make Mac falls asleep")
commands = parser.add_mutually_exclusive_group()
commands.add_argument('-sleep','--sleep', metavar = '', type=int, help='Sleep in number of minutes')
commands.add_argument('-quitall','--quitall', metavar = '', type=int, help='Quit all applications in shutdown in number of minutes')
commands.add_argument('-shutdown','--shutdown', metavar = '', type=int, help='Shutdown in number of minutes')

args = parser.parse_args()
thread1 = threading.Thread()

def timer(seconds,command):    
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
            print(time_left + "\r" , end="")
            time.sleep(1)
            timer -= 1

        performCommand(command)
        break

def performCommand(command):
        if command == sleepCommand:
            lockScreen()
            print("\r", end= "")
            print("Enter 'q' to quit")
        if command == quitAllCommand:
            print("\r", end= "")
            print("Enter 'q' to quit")
            quitall()
        if command == shutdownCommand:
            shutdown()

def quit():
    while True:
        global response
        response = input()
        if response == 'q':
            print("\r", end="")
            sys.exit()   
    
def lockScreen():
    executeApplescript(sleepScript)

def shutdown():
    executeApplescript(closeSafariTabsScript)
    executeApplescript(closeChromeTabsScript)
    executeApplescript(shutdownScript)

def quitall():
    executeApplescript(closeSafariTabsScript)
    executeApplescript(closeChromeTabsScript)
    executeApplescript(quitAllScript)

def startTiming(seconds,commands):
        thread1 = threading.Thread(target=timer,args=[seconds, commands])
        thread1.daemon = True
        thread1.start()

def waitToQuit(seconds):
    userInputThread = threading.Thread(target=quit)
    userInputThread.daemon = True
    userInputThread.start()
    userInputThread.join()
    t=threading.Thread(target=sys.exit)
    t.setDaemon(True)
    t.start()

def minuteToSeconds(seconds):
    return abs((int(seconds) * 1))

def argsSwitch(minutes,command):
    seconds = minuteToSeconds(minutes)
    startTiming(seconds, command)
    waitToQuit(seconds)
    pass

def executeApplescript(applescript):
    argsScript = [item for x in [("-e",l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
    proc = subprocess.Popen(["osascript"] + argsScript ,stdout=subprocess.PIPE )
    progname = proc.stdout.read().strip()
    sys.stdout.write(str(progname))
    proc.wait()
    return proc


if __name__ == "__main__":
    if args.sleep:
        argsSwitch(args.sleep , sleepCommand)
    if args.shutdown:
        argsSwitch(args.shutdown, shutdownCommand)
    if args.quitall:
        argsSwitch(args.quitall, quitAllCommand)
    else: 
        print("Unknown argument\nEnter \"lazy-mac -h\" to view list of arguments ")
pass