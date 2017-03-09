from google.cloud import speech
import api_keys as keys

def transcribe(audio_bytes):
	 speech_client = speech.Client()
	 audio_sample = speech_client.sample(audio_bytes, source_uri=None, encoding="LINEAR16", sample_rate=16000