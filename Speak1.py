from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3 
from datetime import datetime
import webbrowser
import subprocess
root=Tk()
root.geometry("600x600")
root.title("Speech Recognizer")

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio(): 
    speak("How can I help you?")
    spr=sr.Recognizer()
    with sr.Microphone() as source:
        audio=spr.listen(source)
        voice_data=''
        try:
            voice_data=spr.recognize_google(audio, language='en-in')
        except:
            print("Sorry, Could you repeat that")
        print(voice_data)
        
    respond(voice_data)        

def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Harini")
        print("My name is Harini")
    if "time" in voice_data:
        speak("The Current time is")
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
    if "search" in voice_data:
        speak("Opening Google")
        print("Opening Google") 
        webbrowser.get().open("https://www.google.com/")
    if "videos" in voice_data:
        speak("Opening Youtube")
        print("Opening Youtube") 
        webbrowser.get().open("https://www.youtube.com/")
    if "text editor" in voice_data:
        speak("Opening Notepad")
        print("Opening Notepad") 
        subprocess.Popen(["notepad.exe"]) 
        
button1=Button(root, text="Start", command=respond)
button1.place(relx=0.5, rely=0.85,anchor=CENTER)
r_audio()
root.mainloop()