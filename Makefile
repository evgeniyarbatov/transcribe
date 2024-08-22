YOUTUBE_URLS = \
	"https://www.youtube.com/watch?v=oIbcLMFmT78" \
    "https://www.youtube.com/watch?v=K_z5oKC6r4M&t=71s"

AUDIO_DIR := ~/Downloads/audio
TRANSCRIPTS_DIR := ~/gitRepo/video-transcripts/raw

VENV_PATH = ~/.venv/learn-from-video

all: venv install

venv:
	python3 -m venv $(VENV_PATH)

install:
	source $(VENV_PATH)/bin/activate && \
	pip3 install -q -r requirements.txt

download:
	source $(VENV_PATH)/bin/activate && \
	python3 scripts/download.py $(AUDIO_DIR) $(YOUTUBE_URLS) 

text:
	source $(VENV_PATH)/bin/activate && \
	python3 scripts/transcribe.py $(AUDIO_DIR) $(TRANSCRIPTS_DIR)

.PHONY: ven install download text
