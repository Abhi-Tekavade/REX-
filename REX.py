import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import pyjokes
import datetime
from tkinter import *
import os
import time
import wikipedia
import smtplib
import requests
import pyautogui
import keyboard as k
from playsound import playsound

root = Tk()
path=os.getcwd()

var = StringVar()
var1 = StringVar()

frameCnt = 100
frames = [PhotoImage(file=path+"/Assistant.gif",format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
def get_weather(city):
        result = requests.get(url.format(city,'99c9db04fb83ce087fb75dedc820a6ae'))
        if result:
            json = result.json() 
            city = json['name']
            country = json['sys']['country']
            temp_kelvin = json['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            temp_farenheit = (temp_celsius) * 9/5 +32
            weather = json['weather'][0]['main']
            a=str(temp_celsius)
            temp_celsius=a[0:4]
            #final = (city,country,temp_celsius,temp_farenheit,weather)
            #print(final)
            var.set(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ")
            root.update()
            talk(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ")
            print(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ") 

def Commands():
    file=path+"/command.txt"
    file1 = open(file, "a")

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning abhishek") 
        root.update()
        talk("Good Morning abhishek!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon abhishek!")
        root.update()
        talk("Good Afternoon abhishek!")
    else:
        var.set("Good Evening abhishek")
        root.update()
        talk("Good Evening abhishek!")
    talk("Myself Rex! How may I help you sir") 

engine=pyttsx3.init()

def talk(text):
    engine.say(text)         
    engine.runAndWait()

def take_command():  
    r=sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        root.update()
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)          
        audio= r.listen(source)
        
    try:
        var.set("Recognising...")
        root.update()
        print("Recognising...")

        text = r.recognize_google(audio)
        text=text.lower()
        print(text)
        var1.set(text)
        root.update()
    except:
        var.set("say that again plese...")
        root.update()
        print("say that again plese...")
        talk("say that again plese...")
        return "None"

           
    
    return text

def run_rex():
    wishme()
    while True:
    # btn2['state'] = 'disabled'
    # btn3['state'] = 'disabled'
        btn1.configure(bg = 'orange')
        
        text=take_command()

        if 'play' in text:
            song=text.replace('play','')
            var.set("playing"+song)
            root.update()
            talk("playing"+song)
            print("  playing"+song)
            pywhatkit.playonyt(song)

        elif 'what is the time' in text:
            time=datetime.datetime.now().strftime('%H:%M %p')
            var.set("The curren time is "+time)
            root.update()
            print(time)
            talk("The current time is "+time)

        elif 'open' in text:

            if 'google'in text:
                site="google"
                var.set("opening "+site)
                root.update()
                webbrowser.open('https://www.google.com/')
                talk("opening"+site)
            
            elif 'youtube' in text:
                site="youtube"
                var.set("opening "+site)
                root.update()
                webbrowser.open('https://www.youtube.com/')
                talk("opening"+site)
            
            elif 'wikipedia' in text:
                site="wikipedia"
                var.set("opening "+site)
                root.update()
                webbrowser.open('https://www.wikipedia.org/')
                talk("opening"+site)
        
        elif 'wikipedia' in text:
            var.set('Searching on Wikipedia...')
            root.update()
            talk(f'Searching on Wikipedia...')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences = 1)
            var.set(results)
            root.update()
            talk("According to Wikipedia")
            print(results)
            talk(results)

        elif 'information' in text:
            var.set("Wait a min searching...")
            talk("wait a min searching...")
            text=text.replace("give me some information about","")
            result=pywhatkit.info(text)
            var.set(result)
            root.update()
            print(result)
            talk(result)

        elif 'whatsapp message' in text:
            talk("who do you want to send message to")
            text=take_command()
            if 'abhishek' in text:
                phone_no="+919922839147"
                var.set(phone_no)
                root.update()
            elif 'jaishnu' in text:
                phone_no=str("+917021798849")
                var.set(phone_no)
                root.update()
            elif 'chaitanya' in text:
                phone_no=str("+917303991660")
                var.set(phone_no)
                root.update()
            elif 'ashutosh' in text:
                phone_no=str("+917030526388")
                var.set(phone_no)
                root.update()
            else:
                # talk("Who do you want to send message to")
                a=text
                a=f'+91{a}'
                a=str(a)
                phone_no=a
                var.set(phone_no)
                root.update()
            print(phone_no)
            talk("What message do u want to send")
            text=take_command()
            message=text
            var.set(message)
            root.update()
            talk("at what hour do u want to send the message to be sent")
            b=take_command()
            if 'tu' in b:
                b=b.replace("tu",2)
            elif "free" in b:
                b=b.replace("free",3)
            hour=int(b)
            var.set(hour)
            root.update()
            talk("at what minute do u want to send the message ")
            c=take_command()
            if 'tu' in c:
                c=c.replace('tu',2)
            min=int(c)
            var.set(min)
            root.update()
            pywhatkit.sendwhatmsg(phone_no, message,hour,min)
            
            pyautogui.click(1334, 734)
            time.sleep(30)
            pyautogui.press('enter')

        elif 'joke' in text:
            a=pyjokes.get_joke()
            var.set(a)
            root.update()
            print(a)
            talk(a)

        elif 'weather' in text:
            # if "tell me about today's weather" in text:
            #     city='loni'
            #     get_weather(city)
            # elif "Tell me about today's weather forecast" in text:
            #     city='loni'
            #     get_weather(city)
                
            # else:
                text=text.replace("tell me about today's weather in",'')
                city=text
                get_weather(city)
        
        elif "covid" in text:
                var.set("Opening Government Website...")
                root.update()
                talk("Opening Government Website...")
                webbrowser.open("mohfw.gov.in")

        elif "news" in text:
                var.set("Opening news flash....")
                root.update()
                talk("Opening news flash....")
                webbrowser.open("indiatoday.in")
            

        elif "where is" in text:
            text = text.replace("where is", "")
            location = text
            var.set(f"opening {location} on google maps wait a second")
            root.update()
            talk(f"opening {location} on google maps wait a second")
            webbrowser.open("https://www.google.co.in/maps/place/ " + location)
        
        elif 'hello' in text:
            var.set('Hello Sir')
            root.update()
            talk("Hello Sir")

        elif 'who created you' in text:
            var.set("My creaters are Abhishek Jaishnu chaitanya and ashutosh")
            root.update()
            talk("My creaters are Abhishek Jaishnu chaitanya and ashutosh")

        elif "What can you do " in text:
            var.set("I can perform various functions like sending emails,whatsapp msg,give u weather report etc")
            root.update()
            talk("I can perform various functions like sending emails,whatsapp msg,give u weather report etc")

        elif "Who are you" in text:
            var.set("I am rex your voice assitant")
            root.update()
            talk("I am rex your voice assitant")

        elif "good" in text:
            var.set("great to hear that")
            root.update()
            talk("great to hear that")
        
        # elif "exit" in text:
        #     root.destroy


def Commands():
   command_window = Toplevel(root,bg="black")
   command_window.title("REX commands")
   command_window.geometry('600x180')
   commands = Label(command_window, text="1) Send a message on whatsapp - to send a whatsapp msg.\n2) Open google/youtube/wikipedia/stackoverflow. \n3) Tell me about today's weather - gives u weather report of a city. \n4) Where is [cityname]-opens google maps and shows location. \n5) What is the time - tells the current time.\n6) Tell me a joke.\n7) Search something on wikipedia. \n8) Send a mail to someone.\n9) Play [song-name]",font=("Courier", 10), bg="black",foreground="#F2AA4C",justify=LEFT) 
   commands.grid()


root.title("REX")
menubar=Menu(root,background="#101820",fg='#F2AA4C')
menubar.add_command(label="Commands",command=Commands)
root.config(menu=menubar) 
label2 = Label(root, textvariable = var1,bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(root, textvariable = var, bg = '#ADD8E6',wraplength=1200)
label1.config(font=("Courier", 20))
var.set('Hey i am REX,how may i help you ')
label1.pack()


label = Label(root,height=500,width=800)
label.pack()
root.after(0, update, 0)

btn1 = Button(text = 'PLAY',command=run_rex,width = 20,bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()

# btn2 = Button(text="WISH ME",command= wishme,width= 20,bg='#5C85FB')
# btn2.config(font=("Courier",12))
# btn2.pack()

btn3 = Button(text='EXIT',command=root.destroy,width= 20,bg = '#5C85FB')
btn3.config(font=("Courier", 12))
btn3.pack()
root.mainloop()  

