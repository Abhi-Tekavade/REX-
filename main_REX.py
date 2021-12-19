import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time
import webbrowser
import wikipedia
import pyjokes
import smtplib
import requests
import pyautogui
import keyboard as k
from playsound import playsound
from tkinter import *



#weather api
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

engine=pyttsx3.init()

def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour <12: 
            talk("Good morning") 
    elif hour>=12 and hour <18: 
            talk("Good Afternoon") 
    else: 
        talk("Good evening") 
        
    talk("I am REX, how can i help you") 

def talk(text):
    engine.say(text)         #function for talk
    engine.runAndWait()

def take_commond():  
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source,duration=1)          #function for taking command
        audio= r.listen(source)
        
        try:
            print("Recognising...")
            text = r.recognize_google(audio)
            text=text.lower()
            # if 'rex' in text:
            #     text=text.replace('rex','')
            # elif 'capital a' in text:
            #     text=text.replace('capital a','A')
        
            # elif 'capital b' in text:
            #     text=text.replace('capital b','B')

            # elif 'capital c' in text:
            #     text=text.replace('capital c','C')

            # elif 'capital d' in text:
            #     text=text.replace('capital d','D')

            # elif 'capital e' in text:
            #     text=text.replace('capital e','E')

            # elif 'capital f' in text:
            #     text=text.replace('capital f','F')

            # elif 'capital g' in text:
            #     text=text.replace('capital g','G')

            # elif 'capital h' in text:
            #     text=text.replace('capital h','H')

            # elif 'capital i' in text:
            #     text=text.replace('capital i','I')

            # elif 'capital j' in text:
            #     text=text.replace('capital j','J')

            # elif 'capital k' in text:
            #     text=text.replace('capital k','K')

            # elif 'capital l' in text:
            #     text=text.replace('capital l','L')

            # elif 'capital m' in text:
            #     text=text.replace('capital m','M')

            # elif 'capital n' in text:
            #     text=text.replace('capital n','N')

            # elif 'capital o' in text:
            #     text=text.replace('capital o','O')

            # elif 'capital p' in text:
            #     text=text.replace('capital p','P')

            # elif 'capital q' in text:
            #     text=text.replace('capital q','Q')

            # elif 'capital r' in text:
            #     text=text.replace('capital r','R')

            # elif 'capital s' in text:
            #     text=text.replace('capital s','S')

            # elif 'capital t' in text:
            #     text=text.replace('capital t','T')

            # elif 'capital u' in text:
            #     text=text.replace('capital u','U')

            # elif 'capital v' in text:
            #     text=text.replace('capital v','V')

            # elif 'capital w' in text:
            #     text=text.replace('capital w','W')

            # elif 'capital x' in text:
            #     text=text.replace('capital x','X')

            # elif 'capital y' in text:
            #     text=text.replace('capital y','Y')

            # elif 'capital ' in text:
            #     text=text.replace('capital z','Z')

            # elif 'capital a' in text:
            #     text=text.replace('a','A')

            # elif 'hashtag' in text:
            #     text=text.replace('hashtag','#')

            # elif 'attherate' in text:
            #     text=text.replace('at the rate','@')

            # elif 'comma' in text:
            #     text=text.replace('comma',',')

            # elif 'dot' in text:
            #     text=text.replace('dot','.')

            # elif 'dollar' in text:
            #     text=text.replace('dollar','$')

            # elif 'and' in text:
            #     text=text.replace('and','&')

            # elif 'exclamatory mark' in text:
            #     text=text.replace('exclamatory mark','!')
                    
            print(text)

            # talk(text)     function call for repeating
        
        except:
            print("say that again plese...")
            talk("say that again plese...")
    
            run_rex()
    
    return text

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
                talk(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ")
                print(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ") 
                
def countdown(t):      #works in sec convert to min T-T
    while t:
        hours,mins = divmod(t, 3600)
        timer = '{:02d}:{:02d}'.format(hours,mins)
        print(timer, end="\r")
        time.sleep(t)
        t -= 1/3600

        playsound('/home/abhi/Downloads/Alarm Clock Alarm.mp3')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com','rdbklyddnlgvepxx')
    server.ehlo()
    server.starttls()
    server.login('abhishektekavade@gmail.com', 'getjinxed2002')
    server.sendmail('abhishektekavade@gmail.com', to, content)
    server.close()

def run_rex():
    wishMe()
    text=take_commond()
    
    if 'play' in text:
        song=text.replace('play','')
        talk("playing"+song)
        print("  playing"+song)
        pywhatkit.playonyt(song)
    
    elif 'what is the time' in text:
        time=datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk("The current time is "+time)

    elif 'open' in text:

        if 'google'in text:
            site="google"
            webbrowser.open('https://www.google.com/')
            talk("opening"+site)
        
        elif 'youtube' in text:
            site="youtube"
            webbrowser.open('https://www.youtube.com/')
            talk("opening"+site)
        
        elif 'wikipedia' in text:
            site=wikipedia
            webbrowser.open('https://www.wikipedia.org/')
            talk("opening"+site)
        
    elif 'email' in text:            
        try:
            talk("What should I say?")
            # content = take_commond()
            to = "exoticblistered@gmail.com"    
            content = take_commond()
            sendEmail(to, content)
            talk("Email has been sent!")
        except Exception as e:
            print(e)
        # pywhatkit.send_mail("abhishektekavade@gmail.com",'getjinxed2002', 'sample mail', 'hello trying funciton','exoticblistered@gmail.com')
            # talk("sending email")
        
            # # talk("who do you want to send email to ")
            # # take_commond()
            # email_receiver='abhishektekavade@gmail.com'
            # # talk("Enter your email")
            # # take_commond()
            # email_sender='abhishektekavade@gmail.com'
            # # talk("Enter your password")
            # # take_commond()
            # password='qwerty2002'
            # # talk("what are the contents of this mail")
            # # take_commond()
            # message="HEllo trial mail"
            # subject='trying'
            # pywhatkit.send_mail(email_sender, password, subject, message, email_receiver)
    
    elif 'wikipedia' in text:
        talk(f'Searching on Wikipedia...')
        text = text.replace("wikipedia", "")
        results = wikipedia.summary(text, sentences = 3)
        talk("According to Wikipedia")
        print(results)
        talk(results)
    
    elif 'information' in text:
        talk("wait a min searching")
        text=text.replace("give me some information about","")
        result=pywhatkit.info(text)
        print(result)
        talk(result)
    
    elif 'whatsapp message' in text:
        if 'abhishek' in text:
            phone_no='+919922839147'
        elif 'jaishnu' in text:
            phone_no='+917021798849'
        elif 'chaitanya' in text:
            phone_no="+917303991660"
        elif 'ashutosh' in text:
            phone_no="+917030526388"
        else:
            talk("Who do you want to send message to")
            a=take_commond()
            a=f'+91{a}'
            a=str(a)
            phone_no=a
        talk("What message do u want to send")
        take_commond()
        message=text
        talk("at what hour do u want to send the message to be sent")
        b=take_commond()
        time_hour=int(b)
        talk("at what minute do u want to send the message ")
        c=take_commond()
        time_min=int(c)
        pywhatkit.sendwhatmsg(phone_no, message, time_hour, time_min)
        pyautogui.click(1334, 734)
        time.sleep(2)
        k.press_and_release('enter')

    elif 'joke' in text:
    
        a=pyjokes.get_joke()
        print(a)
        talk(a)
    
    elif 'weather' in text:
        text=text.replace("tell me about today's weather in",'')
        city=text
        get_weather(city) 
            
    elif "where is" in text:
        text = text.replace("where is", "")
        location = text
        talk(f"opening {location} on google maps just a second")
        webbrowser.open("https://www.google.co.in/maps/place/ " + location)

    elif "timer" in text:
        talk("for how many mins do u want to set the timer for")
        t=take_commond()
        t=t.replace('minutes','')
        t=int(float(t))
        countdown(t)

    elif 'exit' in text:
        talk("Thanks for giving me your time")
        exit()

window = Tk()
window.geometry("720x420")
window.title("REX")
window.config(bg="#5cfcff")
photo = PhotoImage(file='/home/abhi/Downloads/images2.png')

label = Label(window,text='Voice-assistant REX',font=('arial',20,'bold'),fg='blue',bg='lavender',relief=RAISED,bd=5,image=photo,compound='bottom')
label.pack()

button = Button(window,text='Take command!',command=run_rex,font=("Comic sans",30),padx=10,pady=10)
button.pack()


# window.mainloop()
run_rex()