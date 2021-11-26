#!usr/bin/python
import sys
import os # this is for pulling the files from the aur

#make syntax for the command
args = sys.argv
lenargs = len(args)

#the -S is going to be second
instructor = args[1]

if (instructor == "-S"):
    print("sync requested")
    #do some math to figure out the packages
    packages = []
    packagecount = 0
    x = 1
    while True:
        try:
            print(args[x])
            x += 1
            packages.append(args[x])
            packagecount += 1
            print(packages)
        except:
            if (IndexError):
                break
        for package in packages:
            os.system("git clone https://aur.archlinux.org/" + package + ".git")
            os.chdir(package)
            os.system("makepkg -s -si")
if (instructor == "-R"):
    packages = []
    packagecount = 0
    x = 1
    while True:
        try:
            x += 1
            packages.append(args[x])
            packagecount += 1
        except:
            if (IndexError):
                break

        for package in packages:
            os.system("sudo rm -rf /bin/" + package)
