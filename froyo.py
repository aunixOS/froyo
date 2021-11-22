#!usr/bin/python
import sys
import os # this is for pulling the files from the aur

#get the package to install


try:
    print("https://aur.archlinux.org/" + sys.argv[1] + ".git")
    os.system("git clone https://aur.archlinux.org/" + sys.argv[1] + ".git")
    os.chdir(sys.argv[1])
    os.system("makepkg -s -si")
except:
    pass
