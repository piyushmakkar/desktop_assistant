import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import random
import sys
import pyautogui


pyautogui.FAILSAFE=True
engine=pyttsx3.init("sapi5")
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good moring")
    elif hour>12 and hour<=17:
        speak("good afternoon")
    else: 
        speak("good evening")
    speak("I am Friday. How may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_treshold = 1
        r.energy_treshold =1500
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google( audio, language = 'en-in')
        print("user said", query)
    except Exception as e:
        print(e)
        print("Say that again")
        return "none"    
    return query

if __name__ =="__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wiki')
            query.replace('wikipidea', " ")
            results = wikipedia.summary(query,sentences=2)
            speak("wiki says")
            print(results)
            speak(results)

        elif 'hi' in query:
            speak("HI there ,how can i help you")

        elif 'hello' in query:
            speak("HI there ,how can i help you")

        elif 'youtube' in query:
              query=query.replace('youtube'," ")
              webbrowser.open('https://www.youtube.com/search?q='+query)


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Dell\\Desktop\\YT\\Audio'
            songs=os.listdir(music_dir)
            i=random.randint(0,7)
            os.startfile(os.path.join(music_dir, songs[i]))
        
        elif 'close' in query:
            if 'chrome' in query:
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'computer' in query:
                pyautogui.click(1870,10) 
                pyautogui.click(1029,1057)

            
        elif 'search google' in query:
            query=query.replace('search google'," ")
            if 'for' in query:
                query=query.replace('for'," ")
            else:
                pass    
            webbrowser.open('https://google.com/search?q='+query)
       
        elif 'my computer' in query:
            pyautogui.click(1765,11)
            pyautogui.click(53,77)
            pyautogui.click(53,77)
  
        elif'thank you friday' in query:
            speak("bye sir , it's my duty")
            break
