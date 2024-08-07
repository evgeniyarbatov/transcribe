VENV_PATH = ~/.venv/learn-from-video

.PHONY: venv install

all: venv install

venv:
	python3 -m venv $(VENV_PATH)

install: 
	source $(VENV_PATH)/bin/activate && \
	pip3 install -q -r requirements.txt
