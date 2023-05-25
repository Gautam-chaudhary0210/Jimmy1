import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
    speak("Welcome Master Gautam, How May i Help you?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
        
if __name__ == "__main__":  
    #while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")
            
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            speak("Opening Whatsapp")
            
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("Opening Instagram")
            
        elif 'open w3school' in query:
            webbrowser.open("w3schools.com")
            speak("Opening w3School")
        
        elif 'play music' in query:
            music_dir = 'E:\\Favourite Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\gauta\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
            speak("Opening VS Code")
        
        elif 'open python' in query:
            codePath = "C:\\Program Files\\Python311\\python.exe"
            os.startfile(codePath)
            speak("Opening Python")
            
        elif 'open cs' in query:
            codePath = "E:\\Games\\Counter-Strike WaRzOnE\\CS16Launcher.exe"
            os.startfile(codePath)
            speak("Opening Counter Strike")
            
        elif 'open 10' in query:    
            codePath = "C:\\Program Files (x86)\\Thonny\\thonny.exe"
            os.startfile(codePath)
            speak("opening Thonny")
        
        elif 'open zip' in query:    
            codePath = "C:\\Program Files\\WinRAR\\WinRAR.exe"
            os.startfile(codePath)
            speak("Opening Winrar File")
            
        elif 'open chrome' in query:    
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            speak("Opening Google Chrome")
            
        elif 'send whatsapp message' in query: #Automatic Whatsapp Msg Sending Command
            pywhatkit.sendwhatmsg('+919326138179', 'phone band kakre soja', 15, 19)
            speak("sending Message now")
