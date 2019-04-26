build:
	docker build -t fire015/python-rmi .

build-test:
	docker build -t fire015/python-rmi-test ./build_test

analyse:
	docker run -it --rm -v $(shell pwd):/usr/src fire015/python-rmi mypy main.py app/ --ignore-missing-imports

run:
	docker run -it --rm -v $(shell pwd):/usr/src -v /var/run/docker.sock:/var/run/docker.sock fire015/python-rmi python main.py

.PHONY: build build-test analyse run
