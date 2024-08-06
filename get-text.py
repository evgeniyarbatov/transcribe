import sys
import os

import speech_recognition as sr

from pydub import AudioSegment

def get_filename(file_path):
  file_name, _ = os.path.basename(file_path).split('.')
  return file_name

def split_audio(wav_file, chunk_length_ms=10000):
    audio = AudioSegment.from_file(wav_file)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks

def transcribe_audio_chunks(chunks, language='en-US'):
    recognizer = sr.Recognizer()
    transcriptions = []
    
    for i, chunk in enumerate(chunks):
        chunk_file = f"/tmp/chunk_{i}.wav"
        chunk.export(chunk_file, format="wav")
        
        with sr.AudioFile(chunk_file) as source:
            audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data, language=language)
            print(text)
        except sr.UnknownValueError:
            transcriptions.append("Could not understand audio")
        except sr.RequestError:
            transcriptions.append("Could not request results; check your network connection")
        
        os.remove(chunk_file)  # Clean up chunk file after transcription
  

def main(args):
  audio_path = args[0] 
  output_dir = args[1]

  if not os.path.exists(output_dir):
      os.makedirs(output_dir)

  chunks = split_audio(audio_path)
  
  transcriptions = transcribe_audio_chunks(chunks)
  for i, text in enumerate(transcriptions):
    print(f"Chunk {i}: {text}")

if __name__ == "__main__":
    main(sys.argv[1:])