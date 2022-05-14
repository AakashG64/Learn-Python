'''
pip install pipwin
pipwin install pyaudio
pip install SpeechRecognition
'''

import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something...")
        print('>>>')
        audio = r.listen(source, timeout=1, phrase_time_limit=60)
        try:
            text = r.recognize_google(audio)
            if text == "quit":
                print("I am quitting...")
                break
            else:
                print("You said ", text)
        except Exception as e:
            print("You said nothing.")