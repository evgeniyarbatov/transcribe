import sys
import json
import os

import speech_recognition as sr
from deepmultilingualpunctuation import PunctuationModel
from pydub import AudioSegment

CHUNK_LENGTH_MS = 60000

def get_audio_chunks(audio_path, chunk_length_ms=CHUNK_LENGTH_MS):
    audio = AudioSegment.from_file(audio_path)
    return [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

def cache_results(file_name):
    def decorator(func):
        try:
            cache = json.load(open(file_name, 'r'))
        except (IOError, ValueError):
            cache = {}

        def wrapper(param):
            if param not in cache:
                cache[param] = func(param)
                json.dump(cache, open(file_name, 'w'))
            return cache[param]
        return wrapper
    return decorator

@cache_results('cache/transcribe-cache.json')
def transcribe(chunk_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(chunk_file) as source:
        audio_data = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio_data, language='en-US')
    except sr.UnknownValueError:
        return ''

def transcribe_audio_chunks(chunks):
    text = ""
    for idx, chunk in enumerate(chunks, start=1):
        chunk_file = f"/tmp/{idx}.wav"
        chunk.export(chunk_file, format="wav")
        
        text += transcribe(chunk_file)
        os.remove(chunk_file)
    return text

def punctuate_text(text):
    return PunctuationModel().restore_punctuation(text)

def process_audio_file(audio_path, transcript_path):
    chunks = get_audio_chunks(audio_path)
    text = transcribe_audio_chunks(chunks)
    punctuated_text = punctuate_text(text)
    
    with open(transcript_path, 'w') as output_file:
        output_file.write(punctuated_text)

def main(args):
    audio_dir, transcript_dir = args
    for audio_file in os.listdir(audio_dir):
        if not audio_file.endswith('.wav'):
            continue

        audio_path = os.path.join(audio_dir, audio_file)
        audio_name, _ = os.path.splitext(audio_file)
        
        transcript_path = os.path.join(
            transcript_dir, 
            f"{audio_name}.txt"
        )
        if os.path.exists(transcript_path):
            continue
        
        process_audio_file(audio_path, transcript_path)

if __name__ == "__main__":
    main(sys.argv[1:])