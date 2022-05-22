

import speech_recognition as sr #To convert input from the user which is in audio format into to text format.
import chatterbot               #Python module which responds the user back with the data processed.
import pyaudio                  #This handles audio in python.
import pyttsx3                  #Text to speech conversion package



engine = pyttsx3.init()                 #initializing pyttsx3 package to a variable
voices = engine.getProperty('voices')    # To output the in the form of a human voice
engine.setProperty('voice', voices[1].id) # sets up the default voice from the system


def talk(text):                        #reusable function to output the voice
    engine.say(text)
    engine.runAndWait()



from chatterbot import ChatBot

bot=ChatBot("Alex") #Naming the bot



from chatterbot.trainers import ChatterBotCorpusTrainer

bot.set_trainer(ChatterBotCorpusTrainer)  # Setting the trainer


bot.train('chatterbot.corpus.english')  #choosing language as English

listener=sr.Recognizer()   #creating an instance of recognizer function to implement voice recoginition 

while (True):
   try:
    with sr.Microphone(device_index=1) as source:  #uses the devices default microphone as input
        print(" you can speak now ")
        voice=listener.listen(source)          #audio input is taken here
        command=listener.recognize_google(voice)   #audio is recognized and converted to text format
        print (command)
        if(command.upper()=='BYE'):        # to end the loop
            reply='Bye Bye ,Take care!'
            print(reply)
            talk(reply) 
            break
        else:
           reply=bot.get_response(command)  # to get response back from the bot 
           print(reply)
           talk(reply)      #audio output
   except :
    print("not able to listen you or your microphone is not good")