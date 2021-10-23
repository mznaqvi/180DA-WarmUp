# Adapted from https://www.fypsolutions.com/tutorials/speech-recognition-in-python-using-pocketsphinx/
# speech recognized using Sphinx

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please say something")
    audio = r.listen(source)

try:
    print("You said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error; {0}".format(e))