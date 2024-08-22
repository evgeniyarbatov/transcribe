# Transcribe Video

Generate video transcript for reading offline.

## How to use

Update `Makefile` with URLs you want to transcribe:

```
YOUTUBE_URLS = \
	"https://www.youtube.com/watch?v=oIbcLMFmT78" \
  	"https://www.youtube.com/watch?v=K_z5oKC6r4M&t=71s"
```

Change destination of where to save audio files and transcripts:

```
VIDEO_DIR := ~/Downloads/audio
TRANSCRIPTS_DIR := ~/gitRepo/video-transcripts/raw
```

Download audio:

```
make download
```

Transcribe (this step will be slow):

```
make text
```
