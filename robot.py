import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver
from playsound import playsound
from colorama import Fore
def print_banner():


    print(Fore.YELLOW + '          ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━') 
    print(Fore.YELLOW + '          ┃' + Fore.RED + '     Afghan AI robot ' + Fore.YELLOW + '                    ┃')
    print(Fore.YELLOW + '          ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(Fore.YELLOW + '          ┃' + Fore.YELLOW + 'Created By:' + Fore.GREEN + ' Tariq Bahar' + Fore.YELLOW + '                  ┃')
    print(Fore.YELLOW + '          ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(Fore.YELLOW + '          ┃' + Fore.BLUE + 'Github :' + Fore.BLUE + ' https://github.com/tariqbahar143' + Fore.YELLOW + '┃')
    print(Fore.YELLOW + '          ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('')


print_banner()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
perform='engvoice/perform.wav'
salam = 'voice/salam.mp3'
welcome = 'voice/welcome.mp3'
language = 'voice/language.mp3'
soory = 'voice/soory.mp3'
#english voice fath ******************************************************
assist='engvoice/assist.mp3'
fines='engvoice/fines.mp3'
name='engvoice/name.mp3'
created='engvoice/created.wac'

def wishMe():
    print(' Welcome To Afghan AI  ')
    playsound(salam)
    playsound(welcome)
    playsound(language)
    
    
#wishMe()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("please Say something ....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize your Voice...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Tariq Said:{query}\n")
        if 'hi' in query:
            playsound(assist)
        elif 'how are you' in query:
            playsound(fines)
        elif 'what is your name' in query:
            playsound(name)
        elif 'who created you' in query:
            playsound(created)
        elif 'what can you do' in query:
            playsound(perform)
        

    except Exception as e:
        print(e)
        print("Please tray again your voice is not detected ....")
        playsound(soory)
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Senderemail@gmail.com', 'Password')
    server.sendmail('Senderemail@gmail.com', to, content)
    server.close()

def lighton():
    driver = webdriver.Chrome('C:/Users/Username/Downloads/chromedriver.exe')#add the location of the chrome Drivers
    driver.get("https://Add here.000webhostapp.com/main.html")#Add the webhost name
    elem1 = driver.find_element_by_id("S1off")
    elem1.click()

def lightoff():
    driver = webdriver.Chrome('C:/Users/HACKER47/Downloads/chromedriver.exe')
    driver.get("https://Add here.000webhostapp.com/main.html")#Add the webhost name
    elem1 = driver.find_element_by_id("S1on")
    elem1.click()
            
            

def shutdownWindows():
    os.system("shutdown /s /t 1")  # Shutdown Windows command


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search in chrome' in query:
            speak("what should i search?")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'#Add the Location of the chrome browser

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' +text +'.com')
                wb.get(chrome_path).open(text+'.com')
            except Exception as e:
                print(e)
        
        elif 'how is the weather' and 'weather' in query:

            url = 'https://api.openweathermap.org/data/2.5/weather?q=kabul&appid=b6cb829dd19a410ea359cd9e0bbbefad'#Open api link here

            res = requests.get(url)

            data = res.json()

            weather = data['weather'] [0] ['main'] 
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'email to harry' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "tariqbahar143@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")      

        elif 'open code' in query:
            codePath = "C:\\Users\\user account\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#ADD THE PATH OF THE PROGEM HERE
            os.startfile(codePath)


        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        
        elif 'turn on lights' in query:
            speak("OK,sir turning on the Lights")
            lighton()
            speak("Lights are on")
        
        elif 'turn off lights' in query:
            speak("OK,sir turning off the Lights")
            lightoff()
            speak("Lights are off")
        elif 'shut down' in query:
            speak("Shutting down the system")
            shutdownWindows()   


        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()

        