#some practice code implementing user input

from Tkinter import *
from tkMessageBox import askokcancel

print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Add user")
print ("2. Delete User")
print ("3. View Users")
print (30 * '-')

list = []
some = 1

while some != 0:
    choice = raw_input('Enter your choice [1-3] and [0] to exit : ')
    choice = int(choice)
    if choice == 1:
            print ("Add user process starting...")
            user = raw_input("Add Username : ")
            list.insert(0,user)
            print list
    elif choice == 2:
            print ("Delete user process starting...")
            input1 = raw_input("Delete Username: ")
            list.remove(input1)
            print list
    elif choice == 3:
            print list

    elif choice == 0:   
            print ("Exiting.....")
            break
