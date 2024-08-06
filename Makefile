VENV_PATH = ~/.venv/learn-from-video

.PHONY: venv install

all: venv install

venv:
	python3 -m venv $(VENV_PATH)
	pip3 install --upgrade pip

install: 
	source $(VENV_PATH)/bin/activate 
	pip install -r requirements.txt
