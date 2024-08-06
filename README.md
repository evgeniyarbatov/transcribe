# learn-from-video

Learning from video content

## Get video

Download video from X URL with https://twitsave.com or get directly from X.

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
./transcriptions
```
