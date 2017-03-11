import speech_recognition as speech
import api_keys as keys


recognizer = speech.Recognizer()

def capture_audio():
	with speech.Microphone() as source:
		print("Talk")
		audio = recognizer.listen(source)
	return audio

def transcribe_google_speech(audio):
	transcript = None
	try:
		transcript = recognizer.recognize_google(audio)
	except speech.UnknownValueError:
		print("Google did not understand the audio")
	except speech.RequestError as e:
		print("Could not request transcript from google: {}".format(e))
	return transcript

def print_transcript(transcript):
	print("Transcript: {}".format(transcript))

def capture_and_transcribe():
	print_transcript(transcribe_google_speech(capture_audio()))

capture_and_transcribe()