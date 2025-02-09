import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import keyboard
import os
from plyer import notification
from pygame import mixer
import random
import webbrowser
import speedtest

for i in range(3):
    a = input("Enter Password to open jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print(" Welcome sir ! Please speak [wake up] to load me")
        break 
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("try again")  
    

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query





if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from Greetme import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                



                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)


                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576
                    download_net = wifi.download()/1048576
                    print("wifi upload speed is", upload_net)
                    print("download speed is",download_net)
                    speak(f"wifi download speed is {download_net}")
                    speak(f"wifi upload speed is {upload_net}")


                elif "screenshot" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif"click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    


                elif "hello" in query:
                    speak("Hello sir how are you ?")
                elif "i am fine" in query:
                    speak(" that's great sir")
                elif "i am not fine" in query:
                    speak("i am with you sir just smile")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "thank you" in query:
                    speak("anything for you sir")


                elif "i am tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/hFpXv4eVfjo?si=KdyIYKym2Sn2VefV")
                    elif b==2:
                        webbrowser.open("https://youtu.be/iAmap7Y3fHQ?si=KL2T5gKHl-1LI_IU")
                    elif b==3:
                        webbrowser.open("https://youtu.be/wWkCj2iS9OU?si=m45boSAcLm3TvrsR")




                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")               
                elif "play" in query:
                    pyautogui.press("k")
                    speak*"video paused"
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                    
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                        


                
                elif "open" in query:
                  from Dictapp import openappweb
                  openappweb(query)
                elif "close" in query:
                  from Dictapp import closeappweb
                  closeappweb(query)

 



                elif "google" in query:
                     from SearchNow import searchGoogle
                     searchGoogle(query)
                elif "youtube" in query:
                     from SearchNow import searchYoutube
                     searchYoutube(query)
                elif "wikipedia" in query:
                     from SearchNow import searchWikipedia
                     searchWikipedia(query)


                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)


                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()



                elif "temperature" in query:
                    search = "temperature in maharashtra"
                    url = f"https://www.bing.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is{temp}")




                elif "the time" in query:
                     strTime = datetime.datetime.now().strftime("%H:%M")    
                     speak(f"Sir, the time is {strTime}")
                elif "you can finally sleep jarvis" in query:
                    speak("going to sleep,sir")
                    exit()



                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to" + remember.read()) 

                elif "shutdown the system" in query:
                     speak("Are You sure you want to shutdown")
                     shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                     if shutdown == "yes":
                      os.system("shutdown /s /t 1")

                     elif shutdown == "no":
                      break
                

                
                





                 

