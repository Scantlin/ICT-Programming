from gtts import gTTS
import io
from playsound import playsound

language = 'en'
text = input("Enter you want to: ")

speech = gTTS(text=text, lang=language, slow=True, tld="co.uk")
speech.save("textToSpeech.mp3")