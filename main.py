import pyttsx3 as p
import speech_recognition as sr
from selenium_web import inflow, music
import news
import randfacts
import jokes
from weather import temperature, desc
import datetime

engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
# print(rate)

voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour < 12:
        return 'morning'
    elif hour >= 12 and hour < 16:
        return 'afternoon'
    else:
        return 'evening'

r = sr.Recognizer()

speak('Hello Aditya! Good ' + greet() +'. How are you feeling today?')

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak('I am also having a good day sir')

speak("what can I do for you")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening..')
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak(f'searching {infor} in wikipedia')
    assist = inflow()
    assist.get_info(infor)

elif "play" and "song" in text2:
    speak("what do you want me to play?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening..')
        audio = r.listen(source)
        song = r.recognize_google(audio)
    speak(f'playing {song} in youtube')
    ved = music()
    ved.play(song)

elif "news" in text2:
    arr = news.news()
    speak("Sure sir. Todays top three news are")
    for i in arr:
        speak(i)

elif "joke" in text2:
    speak("sure sir, get ready for some chukkles")
    joke = jokes.telljoke()
    speak(joke[0])
    speak(joke[1])
    speak('Ha Ha')

elif "fact" in text2:
    speak('sure sir')
    x = randfacts.getFact()
    print(x)
    speak("Did you know that, "+ x)

elif "temperature" in text2:
    x = temperature()
    speak('sure sir, todays temperature is')
    speak(str(x) + ' degree celcius')
    # speak('')

elif "weather" in text2:
    x = temperature()
    desc = desc()
    speak('sure sir, todays weather is')
    speak(str(x)+' degree celcius and with ' + desc)

elif "date" in text2:
    date_time = datetime.datetime.now()
    x = 'today is '+date_time.strftime('%d') + ' of ' + date_time.strftime('%B') + ', and its currently ' + date_time.strftime('%H') + " " + date_time.strftime("%I") + " " + date_time.strftime('%p')
    speak(x)