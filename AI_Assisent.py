import pywhatkit
from platform import uname
import speech_recognition as sr
import ast
import pyaudio
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import shutil 
from wikipedia import exceptions
from wikipedia.wikipedia import languages, search
import wolframalpha
import json
import pyjokes
import requests 
import urllib.request
import vlc 
import re
from PyDictionary import PyDictionary
from googlesearch.googlesearch import GoogleSearch
from googletrans import Translator

dir(sr)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate", 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#get username
def username():


    filesize = os.path.getsize("usernames.txt")
    
    global lenCount
    now =time.time()

    opener = open("runTime.txt","r")
    times = opener.read()
    now = str(now)
    print(times)
   
    writer = open("runTime.txt","w")
    writer.write(str(now))
    writer.close

    if(now == time):
        file = open("runCount.txt","w")
        file.close()
    
    open1 = open("runCount.txt", "r") #opens file to read it
    count = (open1.read())
    open1.close()
    countAdd = open("runCount.txt", "w")
    inc=str(count + "i")
    count = inc
    lenCount = int(len(count))
    countAdd.write(str(count))
    countAdd.close()

    open1 = open("runCount.txt", "r") #opens file to read it
    count = (open1.read())
    if(lenCount <= 1):
        if filesize == 0:
            speak("What should i call you, sama?")
            global uname
            uname = takeCommand()
            name = open("usernames.txt", "w") #opens file usernames.txt and gets ready to write to it
            file = uname  #asks user for text speech

            name.write(file) #writes contents in file to usernames.txt
            name.close() #closes file
            open1 = open("usernames.txt", "r") #opens file to read it
            uname = (open1.read())
            speak("welcome "+ uname+"san ." )    
            speak() 
           
            print("Welcome Mr.", uname)
        else:
            open1 = open("usernames.txt", "r") #opens file to read it
            uname=open1.read() #prints whatever is in the text file
            speak("Welcome "+ uname+" san ." )   
          
            print("Welcome.", uname)
    else:       
        open1 = open("usernames.txt", "r") #opens file to read it
        uname=open1.read() #prints whatever is in the text file
        speak("Welcome Back ,"+ uname+" san ." )   
        #columns = shutil.get_terminal_size().columns
        print("Welcome Back,", uname+" san." ) 

#wish the user 
def wishMe():
    if(lenCount <= 1):
        hour=int(datetime.datetime.now().hour)

        if hour>=0 and hour<12:
            speak("Hello,Good Morning "+uname +" san .")
            #speak(uname+"-san") 
            print("Hello,Good Morning "+uname +" san .") 
        elif hour>=12 and hour<18:
            speak("Hello,Good Afternoon "+ uname +" san .")
            #speak(uname+"-san") 
            print("Hello,Good Afternoon "+ uname +" san .")
        else: 
            speak("Hello,Good Evening "+ uname +" san .") 
            #speak(uname+"-san") 
            #speak(" san")
            print("Hello,Good Evening "+ uname +" san. ")
        global assname
        assname =("Komi-chan")
        speak("I am your Virtual Waifu,"+assname )
        speak("----")
        speak("Ask me any thing you want .")
    else:
        speak("wee caan taalk noow ")

#take input
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        r.pause_threshold = 1
        print("Listening...")
        audio=r.listen(source)
       
        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"you said:{statement}\n")

        except Exception as e:
            speak("Sorry, I didn't understand" + uname +"san .") 
            return "None"
        return statement

#print("Loading Your Virtual Waifu,Komi-chan")
#speak("Loading Your Virtual Waifu,Komi-chan")

if __name__=='__main__':
    clear = lambda: os.system('cls')      

#call backs
clear()
username()
wishMe()

contact={
    "sri ram" : "+919790692626",
    "amma"  : "+919788179740",    
}
# open file for writing
f = open("dictTest.txt","w")

# write file
f.write( str(contact) )

# close file
f.close()

file = open("dictTest.txt", "r")

contents = file.read()
contact = ast.literal_eval(contents)
f.close()

while True:
    statement = takeCommand().lower()


    #Option
    if statement==0:
        continue

    if'wikipedia' in statement:
        speak('Searching the Wikipedia...')
        statement=statement.replace("wikipedia","")
        result= wikipedia.summary(statement, sentences = 3)
        speak("The results for ",result)
        print(result)
        speak(result)

    elif 'open google' in statement:
        speak("Google is opening\n")
        webbrowser.open_new_tab("https://www.google.com/")

    elif 'open anime list' in statement:
        speak("You weeb ass! Opening My Anime List")
        webbrowser.open_new_tab("https://myanimelist.net/") 


    elif 'play video' in statement:
        statement = statement.replace(" ","+")
        statement = statement.replace("play","")
        statement = statement.replace("video","")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + statement)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        web="https://www.youtube.com/watch?v=" + video_ids[0]
        webbrowser.open_new_tab(web)
        
    elif 'play song' in statement:
        statement = statement.replace(" ","+")
        statement = statement.replace("play","")
        statement = statement.replace("song","")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + statement)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        playurl="https://www.youtube.com/watch?v=" + video_ids[0]
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()       
        
    elif 'the time' in statement :
        now = datetime.datetime.now() 
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        speak(f"Sir, the time is {date_time}")
        print("data and time:",date_time)

    elif 'define' in statement:
        dictionary=PyDictionary()
        statement = statement.replace("define", "")
        meaning= dictionary.meaning(statement)
        speak("The meaning of "+statement+" is "+meaning)    

    elif "what's your name" in statement or "what is your name" in statement:
        speak("Ore "+assname+" baka")
        

    elif "how are you" in statement:
        speak("why are you asking...")
        speak("of course, I am fine Baka")

    elif "i love you" in statement:
        speak("BAKA")
        speak("i don't like you or anything") 

    elif "do you like humans" in statement or  "do you dilike humans" in statement:
        speak("I don't hate them")
        speak("but I will kill them if some hurt you")

    elif "what do you think of me" in statement:
        speak("I don't hate you")

    elif "a joke" in statement:
         joke = pyjokes.get_joke()
         speak(f"{joke}and your life ")

    elif 'calculate' in statement:
        app_id = "Wolframalpha api id"
        client = wolframalpha.Client(app_id)
        indx = statement.lower().split().index('calculate')
        statement = statement.split()[indx + 1:]
        res = client.statement(' '.join(statement))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)

    elif 'what is love' in statement:
        speak("something you gonna have")
    
    elif 'search' in statement:
        response = GoogleSearch().search(statement)
        for result in response.results:
            print("Title: " + result.title)
            speak("Title")
            speak(result.title)
            print("Content: " + result.getText())
            speak(result.getText())
    
    elif 'write note' in statement:
        speak("What should in note,")
        speak(uname+"-san") 
        takeNotes = takeCommand()
        file = open('Notes.txt','w')
        speak("Sir, Should i include date and time")
        time = takeCommand()
        if 'yes' in time or 'sure' in time:
            strTime = datetime.datatime.now().strftime("% H:% M:% S ")
            file.write(strTime)
            file.write(" :-")
            file.write(takeNotes)

        else:
            file.write(takeNotes)

    elif 'show notes' in statement:
        speak('reading the notes')
        speak(uname+"-san") 
        print(file.read())
        speak(file.read(6))
        print("Notes are show")
    
    elif 'komi' in statement:
        speak("oi oi oi" + assname +"will help you, But i didn't do this you or anything")

    elif 'Send Whatsapp' in statement:
        speak("Who should i message")
        speak(uname+"-san") 
        name = takeCommand()
        speak("what should i send")
        msg  = takeCommand()

        start = time.time()
        name=str(input("Enter a name"))
        number= (contact[name])

        msg=(input("Enter a Msg "))
        end = time.time()
        time_taken = end-start

        if(time_taken <= 60):
            sec = 1
        elif(time_taken >=60):
            sec=2   
        elif(time_taken >= 180):
            sec = 3   

        h = int(time.strftime("%H"))
        m = int(time.strftime("%M"))
        m = m + sec
        pywhatkit.sendwhatmsg(number,msg,h,m,10,True,3)
    
    elif 'add contact' in statement:
        speak("say the name of the contact")
        name = takeCommand()
        name =str(input("Enter a name"))

        speak("now the number")
        number = takeCommand()
        number = str(input("enter a value"))
        number = "+91" + number
        f = open("dictTest.txt","w")
        contact[name] = number

        f.write( str(contact) )
        f.close()
        speak(" "+uname+"san , You added "+name+ " your the contacts.")
        print(contact)
    
    elif 'change my name' in  statement:
        #to delete the name
        file = open("usernames.txt","w")
        file.close()

        speak("To what name should i change")
        name=takeCommand()

        name = open("usernames.txt", "w") #opens file usernames.txt and gets ready to write to it
        file = uname  #asks user for text speech

        name.write(file) #writes contents in file to usernames.txt
        name.close() #closes file
        open1 = open("usernames.txt", "r") #opens file to read it
        uname = (open1.read())
        speak("I have changed your name " + uname + "san .")

    elif 'translate' in statement:
        statement = statement.replace("translate","")
        speak("To which lauguages do you wanna translate")
        speak('''you can translate to
        Japenese .
        Spanish .
        Korean .
        France''')
        lang = takeCommand().lower()
        if lang == "japenese":  
            out = Translator.translate(statement, dest='ja')
            speak(out.pronunciation)
            time.sleep(1.5)
            speak(out.text)
            print(out.text)
        elif lang == "spanish":
            out = Translator.translate(statement, dest='es')
            speak(out.pronunciation)
            time.sleep(1.5)
            speak(out.text)
            print(out.text)
        elif lang == "french":
            out = Translator.translate(statement, dest='fr')
            speak(out.pronunciation)
            time.sleep(1.5)
            speak(out.text)
            print(out.text)
        elif lang == "korean":
            out = Translator.translate(statement, dest='ko')
            speak(out.pronunciation)
            time.sleep(1.5)
            speak(out.text)
            print(out.text)
        else:
            print("Sorry it is out of option")
            speak("Sorry it is out of option")
    
    



         

            

                


            

                        


