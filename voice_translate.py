import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
from playsound import playsound

translator = Translator()

def create_audio(phrase="Hello World!", language="en"):

	print(phrse)

	tts = gTTS(phrase, lang=language)
	tts.save("audio.mp3")

	playsound("audio.mp3")

def hear_mic(language):
	mic = sr.Recognizer()

	try:
		with sr.Microphone() as source:
			mic.adjust_for_ambient_noise(source)
			print("Say something: ")
			audio = mic.listen(source)
	except Exception as e:
		print(e)
		pass

	try:
		phrase = mic.recognize_google(audio, language=language)

		print("You say: "+str(phrase))
		return phrase

	except Exception as e:
		print(e)
		pass


input_lan = input("Input language: ")
output_lan = input("Output language: ")

while True:
	phrase = hear_mic(input_lan)
	phrase = translator.translate(phrase, dest=str(output_lan)).text
	create_audio(phrase, output_lan)
