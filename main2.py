
import speech_recognition as sr
import webbrowser
import pyttsx3                #text-to-speech conversion library in Python
import musiclibrary
import requests
import os
import google.generativeai as genai
import os
import google.generativeai as genai


def gemini(command):
    genai.configure(api_key="AIzaSyC-mW-O-zMCJ3-LneZdBMQF0FA84zGxecg")
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 0,
    # "max_output_tokens": 2048,
    "max_output_tokens": 50,
    "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    )
    chat_session = model.start_chat(
    history=[]
    )
    # enter=input('enter the topic :')
    response = chat_session.send_message(command)
    # print(response.text)
    return response.text


def openai(c):
    output=gemini(c)
    speak(output)    




recognizer=sr.Recognizer()    #used to recognize the voice
engine=pyttsx3.init()           #used to initialise the pyttsx3
newsapi="ee44ff25abb74da4be1095fb7f232381"

def speak(text):               #take the text and speach it
    engine.say(text)
    engine.runAndWait()


    

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.co.in/")
   
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")    
    
    elif "open linkedin" in c.lower():
        webbrowser.open("http://www.linkedin.com/")

    elif "good morning" in c.lower():
        speak("good morning ... how are you ?")

    elif "good afternoon" in c.lower():
        speak("good afternoon ... how was your day ?")

    elif "good night" in c.lower():
        speak("good night ... have a nice day !")   

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=ee44ff25abb74da4be1095fb7f232381")
        if r.status_code==50:
            data=r.json()

            #extract the article

            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])

    # else:
        # output=gemini(c)
        # speak(output)    


if __name__=="__main__":
    speak('hey sir how may i help you')

    # listen for the wait word "jarvis"
    #obtain audio from the user

    while True:
        r=sr.Recognizer()
        print('recoginzing .....')
        try:
            with sr.Microphone() as source:
                print('listening ....')
                audio=r.listen(source,timeout=5,phrase_time_limit=3)
            command=r.recognize_google(audio)
            print(command.lower())

            if(command.lower()=='jarvis'):
                speak('yes...')
                print('listennn .....')
                with sr.Microphone() as source:
                    audio=r.listen(source,timeout=5,phrase_time_limit=3)
                    command=r.recognize_google(audio)
                    processCommand(command)

            elif(command.lower()=='active'):
                speak('yes...activate')
                print('listennningg .....')
                with sr.Microphone() as source:
                    audio=r.listen(source,timeout=5,phrase_time_limit=3)
                    command=r.recognize_google(audio)
                    openai(command)       
             
    
        except Exception as e:
            print("Error:{0}",format(e))