import os
import time
from pathlib import Path
import sys
import subprocess

running = True


def add_user(cmd):
    if cmd[:6] == "addusr":
        new_username = cmd[7:]
        if cmd[7:] == "admin":
            print("Inavlid")
            time.sleep(1)
            print("YOU MESSED UP")
            exit()
        else:
            new_passwd = input("Enter the Password for the user: ")
            users.update({new_username: new_passwd})
            with open('log.lsx', 'w') as file:
                    file.write(f"users = {users}\nunique_user = True\nusername = '{username}'")
            exec(open("luxus.py").read())
def login(cmd):
    if cmd[3:] in users:
        enter_password = input("Enter the password of the user: ")
        if enter_password == users.get(cmd[3:]):
            username = cmd[3:]
            with open('log.lsx', 'w') as file:
                file.write(f"users = {users}\nunique_user = True\nusername = '{username}'")
            exec(open("luxus.py").read())
        else:
            print("Incorrect password")
    else:
        print("Invalid user")
def dirmk(cmd):
    new_dir = cmd[6:]
    path = os.path.join(dir, new_dir)
    os.mkdir(path)
    print("Directory created")
def cd(cmd):
    global dir
    dir_change = cmd[3:]
    if dir_change == "..":
        dir = Path.cwd()
        print("You are back in the / (Stem) directory")
    else:
        dir = str(dir) + dir_change + "\\"
        print(f"Directory Successfully changed to {dir}")
def flmk(cmd):
    fl_name = cmd[5:]
    subprocess.run(f'type nul > {dir}{fl_name}', shell=True)
def cont(cmd):
    try:
        cont_file = cmd[5:]
        if cont_file == "log.lsx" or cont_file == "luxus.py":
            print("You cannot concantonate a system-file")
        else:
            try:
                with open(cont_file) as file:
                    print(file.read())
            except FileNotFoundError:
                print("Invalid File")
    except PermissionError:
        print("You cannot concantonate directories")
            
exec(open('log.lsx').read())
dir = Path.cwd()

def help():
    print("""Currently available Commands in Luxus:
    lg <arg> - logs into a user
    addusr <arg> - adds a user
    pau - prints all active users
    pwu - prints working user
    pwd - prints working directory
    dirmk <arg> - makes a directory
    cd <arg> - changes directory
    flmk <arg> - makes a file
    lis - lists all files and sub-directories in the current working directory
    cont <arg> - lists the contents of a file
    clr - clears the terminal""")

while running:
    if unique_user != True:
        if str(input("Do you want to create a user?\nIf not you'll continue as the stem user\n(y,n)")).lower() != "y":
            username = "stem"
            print("Error")
        else:
            username = input("Enter a username: ")
            user_passwd = input("Enter a password: ")
            users.update({username: user_passwd})
            unique_user = True
            print(users)
            with open('log.lsx', 'w') as file:
                file.write(f"users = {users}\nunique_user = True\nusername = '{username}'")
            continue
    cmd = str(input(f"-{username}- "))
    if cmd[:2] == "lg":
        login(cmd)
    elif cmd[:6] == "addusr":
        add_user(cmd)
    elif cmd == "pau":
        for user in users.keys():
            print(user)
    elif cmd == "pwu":
        print(username)
    elif cmd == "pwd":
        print(dir)
    elif cmd[:5] == "dirmk":
        dirmk(cmd)
    elif cmd == "lis":
        for item in os.listdir(dir):
            print(item)
    elif cmd[:4] == "cont":
        cont(cmd)
    elif cmd == "clr":
        os.system('cls')
    elif cmd == "help":
        help()
    elif cmd[:2] == "cd":
        cd(cmd)
    elif cmd[:4] == "flmk":
        flmk(cmd)
