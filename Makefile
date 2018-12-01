.PHONY: build test

default: build test

build:
	sudo docker build -t kata-tennis-py .

test:
	sudo docker run --rm kata-tennis-py
