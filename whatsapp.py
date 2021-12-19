import pyautogui
import keyboard 
import pywhatkit
import time

def take_commond():
    text=input("Enter details")
    

# print("Who do you want to send message to")
# a=take_commond()
# a=f'+91{a}'
# a=str(a)
# phone_no=a
# print("What message do u want to send")
# d=take_commond()
# message=d
# print("at what hour do u want to send the message to be sent")
# b=take_commond()
# time_hour=(b)
# print("at what minute do u want to send the message ")
# c=take_commond()
# time_min=c
pywhatkit.sendwhatmsg('+919922839147', "hello",4,38)
print("heheheh")
pyautogui.click(1334, 734)
time.sleep(10)
print("after 5 sec")
pyautogui.press('enter')