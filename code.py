import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text) -> object:
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        command = ''
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'about the' in command:
        person = command.replace('about', '')
        info = wikipedia.summary(detial,2)
        print(info)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'HOD ' in command:
        talk('Doctor B D majumdar')
    elif 'proctor' in command:
         talk ('MR Neeraj dubey')
    elif 'open ' in command:
        talk('google')
        webbrowser.open('http://google.co.kr', new=2)
    elif 'facebook' in command:
        talk('opening facebook')
        webbrowser.open('https://www.facebook.com',new=2)
    elif 'intro yourself' in command:
        talk('i am alexa ,digit assistant')
    else:
        talk('please say the command again')

while True:
     run_alexa()
