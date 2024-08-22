YOUTUBE_URLS = \
	"https://www.youtube.com/watch?v=oIbcLMFmT78" \
    "https://www.youtube.com/watch?v=K_z5oKC6r4M&t=71s"

VIDEO_DIR := ~/Downloads/offline-video
TRANSCRIPTS_DIR := ~/gitRepo/video-transcripts

VENV_PATH = ~/.venv/learn-from-video

all: venv install

venv:
	python3 -m venv $(VENV_PATH)

install:
	source $(VENV_PATH)/bin/activate && \
	pip3 install -q -r requirements.txt

download:
	source $(VENV_PATH)/bin/activate && \
	python3 scripts/download.py $(VIDEO_DIR) $(YOUTUBE_URLS) 

transcribe:
	source $(VENV_PATH)/bin/activate && \
	python3 scripts/transcribe.py $(VIDEO_DIR) $(TRANSCRIPTS_DIR)

.PHONY: ven install download transcribe
