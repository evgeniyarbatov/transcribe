# Transcribe video

Generate video transcript for reading offline.

## Get video

Download video and store in `~/Documents/offline-video/video`

## Extract transcript

```
make
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

Split into sentences:

```
python3 get-sentences.py \
./transcriptions/Elon\ Musk\ and\ Jordan\ Peterson.txt \
./sentences
```
