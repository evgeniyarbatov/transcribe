
import sys
import os
import json
import nltk

import speech_recognition as sr

from deepmultilingualpunctuation import PunctuationModel
from pydub import AudioSegment

nltk.download('punkt')

CHUNK_LENGTH_MS = 60000

def get_audio(video_path, output_path):
    return AudioSegment.from_file(video_path)
    
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
def transcribe(chunk):
    recognizer = sr.Recognizer()
    audio_data = recognizer.record(chunk)
    try:
        text = recognizer.recognize_google(
            audio_data, 
            language='en-US',
        )
        return text
    except:
        return ''

def transcribe_chunks(
  chunks, 
  output_path,
):
  for idx, chunk in enumerate(chunks, start=1):
    print(f"Processing: {idx} / {len(chunks)}")
          
    text = transcribe(chunk)
    
    with open(output_path, 'a') as file:
      file.write(f"{text}\n")

def get_sentences(input_path, output_path):
    with open(input_path, 'r') as file:
        text = file.read()

    model = PunctuationModel()
    punctuated_text = model.restore_punctuation(text)
        
    sentences = nltk.sent_tokenize(punctuated_text)
    
    with open(output_path, 'w') as output_file:
        for sentence in sentences:
            capitalized_sentence = sentence.capitalize()
            output_file.write(f"- {capitalized_sentence}\n")

def main(args):
    video_path = args[0] 
    output_path = args[1]

    audio = get_audio(video_path)
    chunks = split_audio(audio, CHUNK_LENGTH_MS)

    transcribe_chunks(chunks, output_path)
    
    get_sentences(input_path, output_path)

if __name__ == "__main__":
    main(sys.argv[1:])