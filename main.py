'''
FEATURES
• Voice Recognition
• Utilizes the speech_recognition library to listen for and recognize voice commands.
• Activates upon detecting the wake word "Jarvis."
• Text-to-Speech
• Converts text to speech using pyttsx3 for local conversion.
• Uses gTTS (Google Text-to-Speech) and pygame for playback.
• Web Browsing.
• Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice
commands.
• Music Playback
• Interfaces with a musicLibrary module to play songs via web links.
• News Fetching
• Fetches and reads the latest news headlines using NewsAPI.
• OpenAI Integration
• Handles complex queries and generates responses using OpenAI's GPT-3.5-turbo.
• Acts as a general virtual assistant similar to Alexa or Google Assistant.
• Activates upon detecting the wake word "Jarvis."
• Text-to-Speech
'''




import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "4409ca2fd24147ab8d0d024fcd117d58"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):


    # Initialize Pygame mixer
    pygame.mixer.init()
    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()





if __name__ == "__main__":
    speak_old("Initializing batman....")
    speak_old('Hello, I am Aaryans Assistant. How can I help you?')
    
    while True:
        # Listen for the wake word "Batman"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=1, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "batman"):
                speak_old("Yes Sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Listening Active...")
                    audio = r.listen(source)
                    c = r.recognize_google(audio)
                    if "open google" in c.lower():
                            speak_old(" Opening Google")

                            webbrowser.open("https://google.com")

                    elif "open facebook" in c.lower():
                        speak_old(" Opening Facebook")      
                        webbrowser.open("https://facebook.com")

                    elif "open youtube" in c.lower():
                        speak_old(" Opening Youtube")      
                        webbrowser.open("https://youtube.com")

                    elif "open linkedin" in c.lower():
                        speak_old(" Opening linkedin")
                        webbrowser.open("https://linkedin.com")
                    elif "news" in c.lower():
                        speak_old("Here are the latest news")
                        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=4409ca2fd24147ab8d0d024fcd117d58")
                        if r.status_code == 200:
                            # Parse the JSON response
                            data = r.json()
                            
                            # Extract the articles
                            articles = data.get('articles', [])
                            
                            # Print the headlines
                            for article in articles:
                                speak_old(article['title'])


        except Exception as e:
            print("Error; {0}".format(e))



