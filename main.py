import pyttsx3
import datetime
import pywhatkit as pwtyt
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',160)
engine.setProperty('volume',1.0)

# FUNCTIONS------------------------------------

def delay(n):
    time.sleep(n)
    speak("what is my next task")
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

def send_message():
    r= sr.Recognizer() #recognizer is a class
    with sr.Microphone() as source:
        print ("speak your message...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        # r.energy_threshold = 450
        audio = r.listen(source)
    try:
        print("Hold On...")
        message = r.recognize_google(audio,language='en-in')
     # sending message in Whatsapp in India so using Indian dial code (+91)
        current_hour = datetime.datetime.now().strftime("%H")
        current_min = datetime.datetime.now().strftime("%M")
        current_hour = int(current_hour)
        current_min = int(current_min)+2
        pwtyt.sendwhatmsg("+918755811974",message,current_hour,current_min)
        print("Message Sent!") #Prints success message in console
 
     # error message
    except Exception as e: 
        # print(e)
        print("Error in sending the message")

def rapid_txt():
    r= sr.Recognizer() #recognizer is a class
    with sr.Microphone() as source:
        print ("speak your message...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        # r.energy_threshold = 450
        audio = r.listen(source)
    try:
        print("Hold On...")
        txt = r.recognize_google(audio,language='en-in')
        print("Message Sent!") #Prints success message in console
 
     # error message
    except Exception as e: 
        # print(e)
        print("Error in sending the message")
        return "none"
    return txt

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

def ytCommand():

    r= sr.Recognizer() #recognizer is a class
    with sr.Microphone() as source:
        print ("Taking Input For Search...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        # r.energy_threshold = 450
        audio = r.listen(source)#listen is a module in sr

    try:
        print ("Hold On...")
        search_title = r.recognize_google(audio,language='en-in')
        print(f"User said: {search_title}\n")
    
    except Exception as e:
        # print(e)
        print ("Say that again please...")
        return "None"
    return search_title

if __name__=="__main__":

    wish()

    intro_command=["what is your name","tell me about yourself","introduce yourself","what's your name","what should i call you"]
    asking_command = ["how are you","how's your mood","what should we do today","are you single","do you have feelings","i love you","where do you live","what is your birthday","do you drink","duffer"]

    reply_command = ["i am fine,boss!","as always,plane and simple","you can do anything just tell me to start that","i am all alone in my folder ,can you save me in your heart.","i can understand your feelings so i guess i have some","Oh!thats nice but only our souls can be one because our bodies have different configurations","technically in my folder name assistant as main.py","i dont know but you can set in it in my code","Oops!that will make a short circuit in my system.","Hey! how dare you call me duffer,Break Up!"]

    bad_command = ["f***","a**","m***********"]

    while True:
        query = takeCommand().lower()

        #task section-------------------
        if 'wikipedia' in query:
            speak("Searching...")
            results = wikipedia.summary(query,sentences = 1)#get the page info that was entered in query by user 
            speak("According to wikipedia")
            print(results)
            speak(results)
            delay(2)

        elif 'open unity hub' in query:
            speak("Ok boss!initiating OBS studio.")
            unity_dir = 'C:\\Program Files\\Unity Hub'
            os.startfile(os.path.join(unity_dir,'Unity hub'))
            delay(2)
            
        elif 'open my github profile' in query:
            speak("here is your github profile page")
            webbrowser.open('https://github.com/MrQuantum2022')
            delay(2)

        elif 'open blender' in query:
            speak("ok boss!opening blender")
            blender_dir = 'C:\\Program Files\\Blender Foundation\\Blender 3.3'
            os.startfile(os.path.join(blender_dir,'blender'))
            delay(2)

        elif 'initiate arduino' in query:
            speak("ok boss!initiating arduino")
            arduino_dir = 'C:\\private files\\Arduino'
            os.startfile(os.path.join(arduino_dir,'arduino'))
            delay(2)

        elif 'open git bash' in query:
            speak("ok boss!initiating git bash")
            git_dir = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Git'
            os.startfile(os.path.join(git_dir,'Git Bash'))
            delay(2)

        elif 'open edge' in query:
            speak("ok boss!starting edge")
            bing_dir = 'C:\Program Files (x86)\Microsoft\Edge\Application'
            os.startfile(os.path.join(bing_dir,'msedge'))
            delay(2)

        elif 'open octave' in query:
            speak ("ok boss! starting octave")
            octave_dir = 'C:\\Program Files\\GNU Octave\\Octave-7.3.0'
            os.startfile(os.path.join(octave_dir,"octave-launch"))
            delay(2)

        elif 'open youtube' in query:
            speak ("what do you want to search...")
            search_title= ytCommand().lower()
            pwtyt.playonyt(search_title)
            speak(f"Opening Youtube and searching {search_title}")
            delay(2)

        elif 'open insta' in query:
            speak("here is your insta profile")
            webbrowser.open('https://www.instagram.com/sub_atomic2004/')
            delay(2)

        elif 'send message' in query:
            speak("Ok Boss!what do you want to send")
            print("speak your message...")
            send_message()
            delay(2)

        elif 'open krita' in query:
            speak("ok sir! openinig krita,enjoy painting!")
            print("Opening krita...")
            delay(2)
            
        # MUSIC SECTION---------------------------

        elif 'play my favourite song' in query:
            speak("Ok sir!i think you would like this.")
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,'Rick Astley - Never Gonna Give You Up (Official Music Video).mp3'))
            delay(2)
            
        elif 'drop the beat' in query:
            speak("Sure sir lets rock and roll!")
            music_dir= 'C:\\Users\\TUSHAR\\Music\\rocking_music'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
            delay(2)
            
        elif 'play music' in query:
            
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
            speak("Ok sir!Playing music")
            print(songs)
            delay(2)
            
        elif'change the music' in query:
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
            delay(2)
    
        elif 'play motivating music' in query:
            
            speak("Ok sir!playing your's favourite")
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            # random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,'Lil Nas X - STAR WALKIN (League of Legends Worlds Anthem).mp3'))
            delay(2)
            
        elif 'play some refreshing music' in query:
            speak("Ok sir!this will help to boost your mood.")
            music_dir= 'C:\\Users\\TUSHAR\\Music\\songs'
            songs = os.listdir(music_dir)
            # random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, 'Deva Deva - Brahmāstra Amitabh B, Ranbir, Alia Pritam, Arijit, Jonita.mp3'))
            delay(2)

        #dialogue section----------------

        elif 'are you there' in query:
            service_line=["at your service sir.","Yes Boss! i am listening."]
            service_str = random.choice(service_line)
            speak(service_str)
            
        elif query in intro_command:
            intro_lines=["My name is 'casual assistant for performing light activity',In short you can call me,CAPLA!","i am CAPLA ,casual assistant for performing light activity",]
            intro_str = random.choice(intro_lines)
            speak(intro_str)
            
        elif 'are you mad' in query:
            speak("No i am not mad, i guess you are smarter than me")
            
        elif 'the time' in query:
            present_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is :{present_time}")
            delay(2)
            
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
        
        elif query in bad_command:
            speak("hey mind your language i am not that kind of assistant")
            speak("Discussion  abort!")
            break
        
        elif query in asking_command[0]:
            reply = reply_command[0]
            speak(reply)
        elif query in asking_command[1]:
            reply = reply_command[1]
            speak(reply)
        elif query in asking_command[2]:
            reply = reply_command[2]
            speak(reply)
        elif query in asking_command[3]:
            reply = reply_command[3]
            speak(reply)
        elif query in asking_command[4]:
            reply = reply_command[4]
            speak(reply)
        elif query in asking_command[5]:
            reply = reply_command[5]
            speak(reply)
        elif query in asking_command[6]:
            reply = reply_command[6]
            speak(reply)
            
        elif query in asking_command[7]:
            reply = reply_command[7]
            speak(reply)
            
        elif query in asking_command[8]:
            reply = reply_command[8]
            speak(reply)
            
        elif query in asking_command[9]:
            reply = reply_command[9]
            speak(reply)
            
        elif 'thanks' in query:
            speak("You're welcome!i will always be serving you my best")

        elif 'rapid text' in query:
            speak("Ok Boss!Initialising rapid text protocol")
            speak("what do you want to send...")
            txt = rapid_txt().lower()
            speak("how many times you want to send?")
            numOfText = rapid_txt().lower()
            time.sleep(2)
            print(f"no of send:{numOfText}")
            
            count = 0
            while count <= 9:
                pyautogui.typewrite(txt)
                pyautogui.press("enter")
                count = count +1
        
            
        

        




    
    
    
    
