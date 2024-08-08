import sys
import os
import json

import speech_recognition as sr

from pydub import AudioSegment

CHUNK_LENGTH_MS = 60000

def split_audio(wav_file, chunk_length_ms):
    audio = AudioSegment.from_file(wav_file)
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

def get_filename(file_path):
  file_name, _ = os.path.basename(file_path).split('.')
  return file_name

def transcribe_chunks(
  chunks, 
  file_name,
  output_path,
):
  for idx, chunk in enumerate(chunks):
    print(f"Processing: {idx} / {len(chunks)}")
    
    chunk_file = f"/tmp/{file_name}_{idx}.wav"
    chunk.export(chunk_file, format="wav")
      
    text = transcribe(chunk_file)
    
    with open(output_path, 'a') as file:
      file.write(f"{text}\n")

    os.remove(chunk_file)

def main(args):
  audio_path = args[0] 
  output_path = args[1]

  file_name = get_filename(audio_path)
  output_path = f"{output_dir}/{file_name}.txt"

  chunks = split_audio(audio_path, CHUNK_LENGTH_MS)
  transcribe_chunks(chunks, file_name, output_path)

if __name__ == "__main__":
    main(sys.argv[1:])