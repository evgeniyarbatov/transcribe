VIDEO_DIR = ~/Documents/offline-video/video
AUDIO_DIR = ~/~/Documents/offline-video/audio

TRANSCRIPTIONS_DIR = ~/gitRepo/video-transcripts/raw_transcripts
SENTENCES_DIR = ~/gitRepo/video-transcripts/sentences

VENV_PATH = ~/.venv/learn-from-video

$(shell mkdir -p $(AUDIO_DIR))
$(shell mkdir -p $(TRANSCRIPTIONS_DIR))
$(shell mkdir -p $(SENTENCES_DIR))

VIDEOS = $(wildcard $(VIDEO_DIR)/*.mp4)

AUDIOS = $(patsubst $(VIDEO_DIR)/%.mp4,$(AUDIO_DIR)/%.wav,$(VIDEOS))
TRANSCRIPTIONS = $(patsubst $(VIDEO_DIR)/%.mp4,$(TRANSCRIPTIONS_DIR)/%.txt,$(VIDEOS))
SENTENCES = $(patsubst $(VIDEO_DIR)/%.mp4,$(SENTENCES_DIR)/%.txt,$(VIDEOS))

all: venv install $(SENTENCES)

venv:
	python3 -m venv $(VENV_PATH)

install: 
	source $(VENV_PATH)/bin/activate && \
	pip3 install -q -r requirements.txt

$(AUDIO_DIR)/%.wav: $(VIDEO_DIR)/%.mp4
	source $(VENV_PATH)/bin/activate && \
	python3 get-audio.py "$<" "$@"

$(TRANSCRIPTIONS_DIR)/%.txt: $(AUDIO_DIR)/%.wav
	source $(VENV_PATH)/bin/activate && \
	python3 get-text.py "$<" "$@"

$(SENTENCES_DIR)/%.txt: $(TRANSCRIPTIONS_DIR)/%.txt
	source $(VENV_PATH)/bin/activate && \
	python3 get-sentences.py "$<" "$@"

clean:
	rm -f $(AUDIOS)
	rm -f $(TRANSCRIPTIONS)
	rm -rf $(SENTENCES_DIR)/*
