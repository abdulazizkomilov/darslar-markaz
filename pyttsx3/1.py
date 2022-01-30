import speech_recognition as sr
import serial 
listener = sr.Recognizer() 

# port = serial.Serial("COM15", 9600)
# print("Phycial body, connected.")

with sr.Microphone() as source:
    print("Talk>>")
    voice = listener.listen(sr.Microphone())                     # listen from microphone
    command = listener.recognize_google(voice).lower()  # use google API
    #command = command.lower()         
    print(command)
    # look for wake up word in the beginning
    if (command.split(' ')[0] == robot_name):
    	# if wake up word found....
    	print("[wake-up word found]")
    	process(command)                 # call process funtion to take action
    	