import pyttsx3 #text will be converted in speech
import speech_recognition as sr 
import pyaudio
import  webbrowser 
import datetime
import pyjokes
import os
import time


def sptext():
    recognizer =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio =recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.unknownValueError:
            print("not understanding") 
 #sptext()             

def speechtx(x):
    engine = pyttsx3.init('sapi5')    #sapi5 --microsoft speech API
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)  
    engine.say(x)
    engine.runAndWait()

# speechtx("hello user welcome to the python tech world")

if __name__=='__main__':
    
    if "hey jarvis" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name="my name  is jarvis how can i help you"
                speechtx(name)
                print(name)
            

            elif "old are you" in data1:
                age = "I have always wanted to do this.How old do you think I am"
                speechtx(age)
                print(age) 

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
                print(time) 

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'github' in data1:
                webbrowser.open("https://github.com/aditibelwal123")

            elif 'gmail' in data1:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif 'map' in data1:
                webbrowser.open("https://www.google.com/maps")

            elif 'google chrome help' in data1:
                webbrowser.open("https://support.google.com/chrome?p=help&ctx=keyboard#topic=7439538")

            elif 'joke' in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1)

            # elif 'video' in data1:
            #     add ="C:\Users\Aditi\Videos\video"
            #      listvideo = os.listdir(add)
            #      print(listvideo)
            #       os.startfile(os.path.join(add,listvideo[0]))
            
            elif "exit" in data1:
                speechtx("okay jarvis is sleep ")
                break
            time.sleep(10)   
    else:
        print("sorry you are not audioable to me")

            
       
                           
                   
