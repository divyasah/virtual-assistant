from logging import exception
from pip import main
import pyttsx3
import datetime
import  speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import code




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis sir.please tell me how may i help you")


def takeCommand():
    #it takes microphone input from the user and returns string input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......") 
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        #print (e)    


        print("say that again please......")
        return None
    return query    


if __name__=="__main__":
    wishMe() 
    while True:
    #if 1:   

        query=takeCommand().lower()  
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.......')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
        elif 'open google' in query:
            webbrowser.open("google.com")  
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"MAM, the time is{strTime} ")  
        elif 'open code' in query:
            codePath="C:\\Users\\wwwdi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'thank you' in query:
            speak("your welcome")
        elif 'are you smarter than google' in query:
            speak("yes i am smarter than ai that exists till now")
           
    
           

            






