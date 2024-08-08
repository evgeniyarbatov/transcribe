VIDEO_DIR = ~/Documents/offline-video/video
TRANSCRIPTS_DIR = ~/gitRepo/video-transcripts

VENV_PATH = ~/.venv/learn-from-video

VIDEOS = $(wildcard $(VIDEO_DIR)/*.mp4)
TARGETS := $(VIDEOS:$(VIDEO_DIR)/%=$(TRANSCRIPTS_DIR)/%)

all: venv install $(TARGETS)

venv:
	python3 -m venv $(VENV_PATH)

install: 
	source $(VENV_PATH)/bin/activate && \
	pip3 install -q -r requirements.txt

$(TRANSCRIPTS_DIR)/%: $(VIDEO_DIR)/%
	source $(VENV_PATH)/bin/activate && \
	python3 transcribe.py "$<" "$@"
