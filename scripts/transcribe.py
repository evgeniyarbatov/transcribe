
import sys
import json
import os

import speech_recognition as sr

from deepmultilingualpunctuation import PunctuationModel
from pydub import AudioSegment

CHUNK_LENGTH_MS = 60000

def get_audio(audio_path):
    return AudioSegment.from_file(audio_path)
    
def split_audio(audio, chunk_length_ms):
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks

def save_to_cache(file_name):
    def decorator(original_func):
        try:
            cache = json.load(open(file_name, 'r'))
        except (IOError, ValueError):
            cache = {}
        def new_func(param):
            if param not in cache:
                cache[param] = original_func(param)
                json.dump(cache, open(file_name, 'w'))
            return cache[param]
        return new_func
    return decorator
  
@save_to_cache('cache/transcribe-cache.json')
def transcribe(chunk_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(chunk_file) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(
            audio_data, 
            language='en-US',
        )
        return text
    except:
        return ''

def transcribe_chunks(chunks, filename):
    text = ""
    for idx, chunk in enumerate(chunks, start=1):
        print(f"Processing: {idx} / {len(chunks)}")
        
        chunk_file = f"/tmp/{filename}_{idx}.wav"
        chunk.export(chunk_file, format="wav")
        
        text += transcribe(chunk_file)
    return text

def punctuate(text):
    model = PunctuationModel()
    return model.restore_punctuation(text)

def main(args):
    audio_dir = args[0] 
    transcript_dir = args[1]

    audio_files = [
        f for f in os.listdir(audio_dir) if f.endswith('.wav')
    ]
    for audio_file in audio_files:
        audio_filename, _ = os.path.basename(audio_file).split('.')
        audio_path = f'{audio_dir}/{audio_file}'
        
        audio = get_audio(audio_path)
        chunks = split_audio(audio, CHUNK_LENGTH_MS)

        text = transcribe_chunks(chunks, audio_filename)
        text = punctuate(text)
        
        filename, _ = os.path.splitext(
            os.path.basename(audio_path)
        )
        transcript_file = f"{transcript_dir}/{filename}.txt"
        
        with open(transcript_file, 'w') as output_file:
            output_file.write(text)

if __name__ == "__main__":
    main(sys.argv[1:])