import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 100)
engine.say("I am the text spoken after changing the speech rate.")
engine.runAndWait()