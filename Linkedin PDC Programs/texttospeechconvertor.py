# Online Text To Speech Library -> gTTs : It is a Google Text-To-Speech API
# Offline Text To Speech Library -> pyttsx3 : It is a Python Library
'''
PYTTSX3 - it looks for TTS engines pre-installed in your platform and uses them,
here are the text-to-speech synthesizers that this library uses:

SAPI5 on Windows XP, Windows Vista, 8, 8.1 and 10
NSSpeechSynthesizer on Mac OS X 10.5 and 10.6
espeak on Ubuntu Desktop Edition 8.10, 9.04 and 9.10
'''


'''
pip install gTTs
pip install playsound
pip install pyttsx3
'''
# -----------------------------------------GTTS---------------------------------------------------

# from gtts import gTTS
# import gtts
# from playsound import playsound
#
# mytext = "Welcome To The Python World, Aakash."
# language = "en"
# myobj = gTTS(text=mytext, lang=language, slow=False)
#
# myobj.save("welcome.mp3")
# playsound("welcome.mp3")
# print(gtts.lang.tts_langs())

# ----------------------------------------PYTTSX3------------------------------------------------

import pyttsx3
engine = pyttsx3.init()

text = "Python is a great programming language"
engine.say(text)
engine.runAndWait()

# get details of speaking rate
rate = engine.getProperty("rate")
print(rate)

# setting new voice rate (faster)
engine.setProperty("rate", 300)
engine.say(text)
engine.runAndWait()

# get details of all voices available
voices = engine.getProperty("voices")
print(voices)

# set another voice
engine.setProperty("voice", voices[1].id)
engine.say(text)
engine.runAndWait()

# saving speech audio into a file
engine.save_to_file(text, "python.mp3")
engine.runAndWait()