# import pywhatkit as kit
# import pyautogui
# import keyboard as k
# a=9175918775
# #a=str(a)
# a=f'+91{a}'
# a=str(a)
# print(type(a))
# print(a)
# #kit.sendwhatmsg(a,"voice assitant se bhej raha it works", 21,55)

# pyautogui.click(1334, 734)
# time.sleep(2)
# k.press_and_release('enter')
# # print(type(a))
# # print(a[0:4])
# # text='tell me about todays weather in mumbai'
# # text=text.replace('tell me about todays weather in','')
# # print(text)
# # text.replace(old, new)

# from  tkinter import *

# window = Tk()
# window.title("Guessing Game")

# welcome = Label(window, text="Welcome To The Guessing Game!", background="black", foreground="white")
# welcome.grid(row=0, column=0, columnspan=3)

# def Rules():
#    rule_window = Toplevel(window)
#    rule_window.title("The Rules")
#    the_rules = Label(rule_window, text="Here are the rules...\n how are hdhdhdh \nshshshshssh", foreground="black")
#    the_rules.grid(row=0, column=0, columnspan=3)

# rules = Button(window, text="Rules", command=Rules)
# rules.grid(row=1, column=0, columnspan=1)

# window.mainloop()

from tkinter import *
from tkinter import ttk

#Create an instance of tkinter window
root= Tk()
root.geometry("600x450")

#Define a function
def open_new():
    #Create a TopLevel window
    new_win= Toplevel(root)
    new_win.title("My New Window")

    #Set the geometry
    new_win.geometry("600x250")
    Label(new_win, text="Hello There!",font=('Georgia 15 bold')).pack(pady=30)

#Create a Button in main Window
btn= ttk.Button(root, text="New Window",command=open_new)
btn.pack()

root.mainloop() 
