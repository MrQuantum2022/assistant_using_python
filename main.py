import pyttsx3
import datetime

import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)
engine.setProperty('volume',1.0)

# FUNCTIONS------------------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    
    statement = ["programmer!","sir!","coder!","developer!","Tushar","Boss!"]
    greet_to = random.choice(statement)
    suggest_strs =["what can i help you with today.","What can i do for you.","How may i help you","what should be done today"]
    suggest = random.choice(suggest_strs)

    hour = int (datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        print("Assitant status:Online")
        
        speak("Good Morning"+ greet_to + suggest )
        

    elif hour >=12 and hour <18:
        print("Assitant status:Online")
        speak("Good Afternoon"+ greet_to + suggest )
   
    else:
        print("Assitant status:Online")
        speak("Good Evening"+ greet_to + suggest )

def takeCommand():

    r= sr.Recognizer() #recognizer is a class
    with sr.Microphone() as source:
        print ("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        # r.energy_threshold = 450
        audio = r.listen(source)#listen is a module in sr

    try:
        print ("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print ("Say that again please...")
        return "None"
    return query
  


if __name__=="__main__":
    wish()
    
    while True:

        query = takeCommand().lower()
        
        #task section-------------------
        if 'wikipedia' in query:
            
            speak("Searching...")
            results = wikipedia.summary(query,sentences = 1)#get the page info that was entered in query by user 
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'f***' in query:
            speak("hey mind your language,i am not that kind of assistant")

        elif 'open unity hub' in query:
            speak("Ok boss!initiating OBS studio.")
            unity_dir = 'C:\\Program Files\\Unity Hub'
            os.startfile(os.path.join(unity_dir,'Unity hub'))
          

        elif 'open my github profile' in query:
            speak("here is your github profile page")
            webbrowser.open('https://github.com/MrQuantum2022')

        elif 'open blender' in query:
            speak("ok boss!opening blender")
            blender_dir = 'C:\\Program Files\\Blender Foundation\\Blender 3.3'
            os.startfile(os.path.join(blender_dir,'blender'))

        elif 'initiate arduino' in query:
            speak("ok boss!initiating arduino")
            arduino_dir = 'C:\\private files\\Arduino'
            os.startfile(os.path.join(arduino_dir,'arduino'))

        elif 'open git bash' in query:
            speak("ok boss!initiating git bash")
            git_dir = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Git'
            os.startfile(os.path.join(git_dir,'Git Bash'))

        elif 'open edge' in query:
            speak("ok boss!starting edge")
            bing_dir = 'C:\Program Files (x86)\Microsoft\Edge\Application'
            os.startfile(os.path.join(bing_dir,'msedge'))

        elif 'open octave' in query:
            speak ("ok boss! starting octave")
            octave_dir = 'C:\\Program Files\\GNU Octave\\Octave-7.3.0'
            os.startfile(os.path.join(octave_dir,"octave-launch"))

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open insta' in query:
            speak("here is your insta profile")
            webbrowser.open('https://www.instagram.com/sub_atomic2004/')

        # MUSIC SECTION---------------------------

        elif 'play my favourite song' in query:
            speak("Ok sir!i think you would like this.")
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,'Rick Astley - Never Gonna Give You Up (Official Music Video).mp3'))
            
        
        elif 'drop the beat' in query:
            speak("Sure sir lets rock and roll!")
            music_dir= 'C:\\Users\\TUSHAR\\Music\\rocking_music'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
            

        elif 'play music' in query:
            
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
            speak("Ok sir!Playing music")
            print(songs)
            
        elif'change the music' in query:
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))

            
        elif 'play motivating music' in query:
            
            speak("Ok sir!playing your's favourite")
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            # random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,'Lil Nas X - STAR WALKIN (League of Legends Worlds Anthem).mp3'))
            
        elif 'play some refreshing music' in query:
            speak("Ok sir!this will help to boost your mood.")
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            # random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, 'Deva Deva - Brahmāstra Amitabh B, Ranbir, Alia Pritam, Arijit, Jonita.mp3'))

        

        #dialogue section----------------

        elif 'are you there' in query:
            service_line=["at your service sir.","Yes Boss! i am listening."]
            service_str = random.choice(service_line)
            speak(service_str)

        elif 'what is your name' in query:
            intro_lines=["My name is 'casual assistant for performing light activity',In short you can call me,CAPLA!","i am CAPLA ,casual assistant for performing light activity",]
            intro_str = random.choice(intro_lines)
            speak(intro_str)


        elif 'are you mad ' in query:
            speak("No i am not mad, i guess you are smarter than me")

        elif 'the time' in query:
            present_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is :{present_time}")
            
        
        elif 'stop' in query:
            speak("Sure Sir!going offline")
            speak("Have a nice day")
            print("Assitant status:Offline")
            break

        elif 'enough' in query:
            speak("Sure Sir!going offline")
            speak("Have a nice day.")
            print("Assitant status:Offline")
            break
        
        elif 'a**' in query:
            speak("hey mind your language i am not that kind of assistant")
            speak("Operation abort!")
            break
        
        elif 'thanks' in query:
            speak("You're welcome!serving you my best")
        # elif 'addition' in query:
            
        

        




    
    
    
    
