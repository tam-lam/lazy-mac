#!/usr/bin/env python3
import os, subprocess, sys
filename = "lazy-mac"
rootDirPath = "/"
def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "Administrator/root permission is required\n[sudo] password for %u:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

def returnToParentDir(path):
    os.chdir("../")
    return os.getcwd()
    
def goToBin():
    while True:
        path = os.getcwd()
        path = returnToParentDir(path)
        if path == rootDirPath:
            break
    os.chdir("usr/local/bin")
    path = os.getcwd()
    
def isSuccess():
    proc = subprocess.Popen(["find . -print | grep -i %s" % (filename)], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    strOut = str(out)
    if(strOut.__contains__("./%s" %(filename)) ):
        print("Install successfully")
        return True
    else:
        print("Installation failed")
        return False
    
def copyToBin():
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    os.system("sudo cp %s /usr/local/bin/" %  (os.path.join(application_path, filename)))

def grantPermissions():
    os.system("sudo chmod 777 %s" % (filename))

if __name__ == "__main__":
    
    print("Installing %s..." % (filename))
    if prompt_sudo() != 0:
        print("Need root permission")
    copyToBin()
    goToBin()
    if isSuccess():
        grantPermissions()

