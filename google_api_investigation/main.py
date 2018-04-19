import os
import base64
import speech
import nlp

# Set API key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/key.json".format(os.path.dirname(os.path.realpath(__file__)))

# Run some text through NLP
nlp.understand_text("Hey this is jim from bendigo")

# Run some audio through google speech-to-text
file_name = os.path.join(os.path.dirname(__file__), 'resources', 'mono.flac')
speech.transcribe_audio_file(file_name)
