import pyttsx3
import speech_recognition as sr
from datetime import date
import os
from datetime import datetime


def get_text():
    while(1):
        r = sr.Recognizer()  
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            try:
                return r.recognize_google(audio_text)
            except:
                print("Sorry, I did not get that.\nPlease try again...")
                pyttsx3.speak("Sorry, I did not get that. Please Try Again...")

def get_option():
    while(1):
        r = sr.Recognizer()  
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            try:
                return r.recognize_google(audio_text)
            except:
                print("Sorry, I did not get that.\nPlease try again...")
                pyttsx3.speak("Sorry, I did not get that. Please Try Again...")

def saykube():
    query=get_text()
    print(query)
    os.system(query)

def typekube():
    query=input("Enter the command: ")
    os.system(query)

def typeaws():
    query=input("Enter the command: ")
    os.system(query)

def sayaws():
    query=get_text()
    print(query)
    os.system(query)

def typeeks():
    query=input("Enter the command: ")
    os.system(query)

def sayeks():
    query=get_text()
    print(query)
    os.system(query)

def main():
    while True:
        print("What Can I do for you?")
        pyttsx3.speak("What Can I do for you?")
        query= get_text()
        print(query)
        if 'date' in query:
            today = date.today()
            print("Today's Date is "+today.strftime("%B %d, %Y"))
            pyttsx3.speak("Today's Date is "+today.strftime("%B %d, %Y"))

        elif 'time' in query:
            now = datetime.now()
            dt_string = now.strftime("%H hours, %M minutes and %S seconds")
            print("Time is "+dt_string)
            pyttsx3.speak("Time is "+dt_string)

        elif 'chrome' in query:
            os.system("start msedge")
            pyttsx3.speak("chrome browser started")

        elif 'calculator' in query:
            os.system("start calc")
            pyttsx3.speak("calculator started")

        elif (('minikube' in query) or ('mini cube' in query)) and ('start' in query):
            os.system("minikube start")

        elif (('minikube' in query) or ('mini cube' in query)) and ('dashboard' in query):
            os.system("minikube dashboard")

        elif (('minikube' in query) or ('Mini cube' in query)) and ('IP' in query):
            os.system("minikube ip")
        
        elif ('kubectl' in query) or ('kubernetes' in query):
            print("Do you want to type the command or say it?")
            pyttsx3.speak("Do you want to type the command or say it?")
            while True:
                query=get_text()
                print(query)
                if 'type' in query:
                    print("Type it:")
                    pyttsx3.speak("Type it")
                    typekube()
                    break

                elif 'say' in query:
                    print("Say it:")
                    pyttsx3.speak("Say it")
                    saykube()
                    break

                else:
                    print("Please say it again...")
                    pyttsx3.speak("Please say it again...")

        elif ('IP' in query) or ('IP' in query and 'configuration' in query):
            os.system("ipconfig")

        elif ('eks' in query) or ('eksctl' in query) or ('Elastic Kubernetes Service' in query):
            print("Do you want to type the command or say it?")
            pyttsx3.speak("Do you want to type the command or say it?")
            while True:
                query=get_text()
                print(query)
                if 'type' in query:
                    print("Type it:")
                    pyttsx3.speak("Type it")
                    typeeks()
                    break

                elif 'say' in query:
                    print("Say it:")
                    pyttsx3.speak("Say it")
                    sayeks()
                    break

                else:
                    print("Please say it again...")
                    pyttsx3.speak("Please say it again...")

        elif ('aws' in query) or ('Amazon Web Services' in query) or ('a w s' in query):
            print("Do you want to type the command or say it?")
            pyttsx3.speak("Do you want to type the command or say it?")
            while True:
                query=get_text()
                print(query)
                if 'type' in query:
                    print("Type it:")
                    pyttsx3.speak("Type it")
                    typeaws()
                    break

                elif 'say' in query:
                    print("Say it:")
                    pyttsx3.speak("Say it")
                    sayaws()
                    break

                else:
                    print("Please say it again...")
                    pyttsx3.speak("Please say it again...")
        
        elif ('goodbye' in query) or ('bye' in query):
            quit()

        else:
            print("I am sorry, I am not programmed for that!")
            pyttsx3.speak("I am sorry, I am not programmed for that!")

if __name__=="__main__":
    main()