
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def hello():
    speak("Hello Sir I am Your Desktop asistant. Tell me how can I can help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio,language='en-in')
            print("The command is printed=",query)
        except Exception as e:
            print(e)
            print("Say that again Sir")
            return "None"
        return query

def take_query():
    hello()
    while(True):
        query=take_command().lower()
        if "hello,how are your" in query:
            speak("I am Fine")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open('www.google.com.pk')
        elif 'bye' in query:
            speak("Okay Bye")
            exit()
        elif 'from wikipedia' in query:
            speak("Checking the wikipedia")
            query= query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(result)
        elif 'tell me your name' in query:
            speak("I am Jerry! Your Desktkop Assistant")

if __name__ == '__main__':
    take_query()