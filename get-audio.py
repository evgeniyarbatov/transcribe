import sys
import os

from pydub import AudioSegment

def get_filename(file_path):
  file_name, _ = os.path.basename(file_path).split('.')
  return file_name

def get_audio(video_path, output_dir):    
  file_name = get_filename(video_path)
  output_path = f"{output_dir}/{file_name}.wav"

  audio = AudioSegment.from_file(video_path)
  audio.export(output_path, format='wav')

  print(f"{output_path}")

def main(args):
  video_path = args[0] 
  output_dir = args[1]

  if not os.path.exists(output_dir):
      os.makedirs(output_dir)

  get_audio(video_path, output_dir)

if __name__ == "__main__":
    main(sys.argv[1:])