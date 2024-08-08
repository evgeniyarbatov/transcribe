import sys

from pydub import AudioSegment

def get_audio(video_path, output_path):
  audio = AudioSegment.from_file(video_path)
  audio.export(output_path, format='wav')

def main(args):
  video_path = args[0] 
  output_path = args[1]
  
  get_audio(video_path, output_path)

if __name__ == "__main__":
    main(sys.argv[1:])