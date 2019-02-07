import os, subprocess
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
if __name__ == "__main__":
    pass

def removeFile():
    print("Removing sleeper...")
    os.system("rm sleeper")

def checkSuccess():
    proc = subprocess.Popen(["find . -print | grep -i 'sleeper'"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    strOut = str(out)
    if(strOut.__contains__("./sleeper") ):
        print("Uninstallation failed")
    else:
        print("sleeper was removed")


if __name__ == "__main__":
    if prompt_sudo() != 0:
        print("Need root permission")
    goToBin()
    removeFile()
    checkSuccess()
    pass
