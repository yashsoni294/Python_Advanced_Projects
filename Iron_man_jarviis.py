import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir. Please tell me how may I help you ?")
def takeCommand():
    """
    It takes microphone input from the user and returns string output
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio,language='en-in')
        print("User said:",query)
    except Exception as e:
        print("Say that again please......")
        return "None"
    return query
if __name__ == '__main__':
    wish_me()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com") 
        elif 'google' in query:
            webbrowser.open("google.com")  
        elif 'stackovefrflow' in query:
            webbrowser.open("stackoverflow.com")
        elif "music" in query:
            music_dir = "C:\\Users\\HP\\Desktop\\SONGS\\2017\\Ae Dil Hai Mushkil"
            songs = os.listdir(music_dir)
            print(songs)
            random_song=random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[random_song]))
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")   
