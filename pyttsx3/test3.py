import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)

with sr.Microphone() as source:
    print("Speak Anything:  ")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        engine.say('You said: {}'.format(text))
    except:
        engine.say("Sorry could not recognize your voice!")