import sys
import os
import shutil

from pytubefix import YouTube
from pytubefix.innertube import _default_clients

from pydub import AudioSegment

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

def download_video(url, output_dir):
    yt = YouTube(url)    
    stream = yt.streams.filter(only_audio=True).first() 
    
    filename = f"{yt.title}.mp4"   
    audio_file = stream.download(
        output_path=output_dir,
        filename=filename,
    )
    
    audio = AudioSegment.from_file(audio_file)
    wav_file = audio_file.replace(audio_file.split('.')[-1], 'wav')
    audio.export(wav_file, format='wav')

def main(output_dir, urls):    
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    for url in urls:
        download_video(url, output_dir)

if __name__ == "__main__":
    output_dir, urls = sys.argv[1], sys.argv[2:]
    main(output_dir, urls)
