import pyttsx3 
import datetime
import speech_recognition as sr 
import webbrowser
import pyautogui

engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def screenshot():
    pic=pyautogui.screenshot()
    pic.save('C:/Users/Noha/Desktop/image/ss.jpg')

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 6 and hour < 12:
        speak("Good Morning sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")

    elif hour >= 18 and hour < 5:
        speak("Good Evening sir")

    else:
        speak("Hello sir")

    speak("i am your assistant")
    speak("Please tell me how may i help you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query



wishMe()
while True:
    
    query = takeCommand().lower()
        

    if 'open college website' in query:

        webbrowser.open("http://www.mti.edu.eg/" )

    elif 'open my e-learning' in query:
        webbrowser.open("https://elearning.mti.edu.eg/login/index.php")     

    elif 'start youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open Linkedin' in query:
        webbrowser.open("Linkedin.com")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")

    elif 'open whatsapp' in query:
        webbrowser.open("https://web.whatsapp.com/")

    elif 'open facebook' in query:
        webbrowser.open("https://www.facebook.com/")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H,%M,%S")
        speak(f"Sir, the time is {strTime}")


    elif 'screenshot' in query:
        screenshot()

    elif 'search youtube' in query:
        speak("what would you like to see  ")
        search= takeCommand().lower()
        speak('I have millions of videos')
        webbrowser.open('https://www.youtube.com/results?search_query='+search)

    elif 'search google ' in query:
        speak("what are you looking for?")
        search=takeCommand().lower()
        speak('I am smart, take this')
        webbrowser.open('https://www.google.com/search?q='+search)
           