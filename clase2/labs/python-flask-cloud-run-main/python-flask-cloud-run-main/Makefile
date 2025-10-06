PROJECT_NAME=python-flask-cloud-run

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

develop: ## Runs the flask server locally
	python3 ./app.py

runtime: ## Creates container from Dockerfile
	docker build . -t python-flask-cloud-run:runtime