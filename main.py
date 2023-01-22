import speech_recognition as sr # package to recognize voice
import whisper # to transcript the text
import pyttsx3 # Package to read text or strings
import pywhatkit
import datetime
import wikipedia # Get wikipedia data
import sys
import re

listener = sr.Recognizer() # Init voice recorder
engine = pyttsx3.init() # Read out loud text

# Set the voice in engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Give an answer
def talk(text):
    engine.say(text)
    engine.runAndWait()

# listen and get the command
def take_command():
    print("Ready")
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'order' in command:
                command = command.replace('order', '')
    except:
        pass
    return command

def search_wiki(command):
    obj = re.findall('^(what is it|who is)(.+)', command)[0][1]
    try:
      talk(wikipedia.summary(obj, sentences=1))
    except:
      talk("Research not found please retry.")

# Run the assistance
def run_assistance():
    command = take_command()
    # Script to stop the program
    if command == "stop":
        talk("Script stopped")
        sys.exit("Script stopped")
    # Get the time
    elif command == "what time is it":
        x = datetime.datetime.now()
        x = x.strftime("%H:%M:%S %p")
        talk("It is "  + x)
    elif command == "what day is it":
        x = datetime.datetime.now()
        x = x.strftime("%A %d th %B %Y")
        talk("It is "  + x)
    # Make a research wikipedia
    elif bool(re.match(r"^(what is it|who is)",command)) :
        search_wiki(command)
    else:
        talk("Please say a command")


# Run in the loop the assistance
while True:
    run_assistance()
