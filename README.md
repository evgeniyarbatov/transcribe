# learn-from-video

Learning from video content

## Fast

Download video from X URL with https://twitsave.com

Extract audio:

```
ffmpeg -i \
video/Elon\ Musk\ and\ Jordan\ Peterson.mp4 \
audio/Elon\ Musk\ and\ Jordan\ Peterson.wav
```

Upload to Google:

```
gsutil cp \
audio/Elon\ Musk\ and\ Jordan\ Peterson.wav \
gs://audio-transcription-arbatov
```

## Env

```
make
source ~/.venv/learn-from-video/bin/activate 
```

## Pipeline

Get audio:

```
python3 get-audio.py \
~/video-learning/video/Elon\ Musk\ and\ Jordan\ Peterson.mp4 \
~/video-learning/audio
```

Get text:

```
python3 get-text.py \
/Users/zhenya/video-learning/audio/Elon\ Musk\ and\ Jordan\ Peterson.wav \
~/video-learning/text
```
