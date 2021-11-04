import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes 
import google
from ytmusicapi import YTMusic

listener = sr.Recognizer()
engine = pyttsx3.init()
#Getting different voices.
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "bablu" in command:
                #You want to give a command, without the bot processing
                #it's name along, for example "guru, play wizkid"
                command = command.replace("bablu", '')
    except:
        pass
    return command

def run_bot(): 
    command = listen()
    print(command)
    if 'what is your name' in command:
        talk("My name is Bablu and I was creted by Seriki")
    elif 'Seriki' in command:
        talk("This is my boss and my creator, a senior man of the highest order. You must have been hearing it")
    elif 'Kamal' in command:
        talk("This is my boss and my creator, a senior man of the highest order. You must have been hearing it")
    elif 'play' in command:
        song = command.replace("play", '')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The time is " + time)
    elif ("what is") in command:
        wiki = command.replace("what is", "")
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)
    elif ("who is") in command:
        wiki = command.replace("who is", "")
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)
    elif ("how") in command:
        wiki = command.replace("how", "")
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)
    elif "jokes" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)  
    else:
        rep = "can you be more direct or audible"
        print(rep) 
        talk(rep)
        run_bot()
                
while True:
    run_bot()
          
         