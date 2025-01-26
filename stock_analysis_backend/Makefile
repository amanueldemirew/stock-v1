.PHONY: help install migrate upgrade downgrade current history run test lint clean

# Colors for terminal output
BLUE=\033[0;34m
NC=\033[0m # No Color
GREEN=\033[0;32m
RED=\033[0;31m

help:
	@echo "$(BLUE)Available commands:$(NC)"
	@echo "$(GREEN)make migrate msg=\"your message\"$(NC) - Create new migration"
	@echo "$(GREEN)make upgrade$(NC)                     - Upgrade database to latest migration"
	@echo "$(GREEN)make downgrade$(NC)                   - Downgrade database one step"
	@echo "$(GREEN)make current$(NC)                     - Show current migration"
	@echo "$(GREEN)make history$(NC)                     - Show migration history"
	@echo "$(GREEN)make install$(NC)                     - Install dependencies"
	@echo "$(GREEN)make run$(NC)                         - Run the application"
	@echo "$(GREEN)make clean$(NC)                       - Remove Python cache files"

install:
	pip install -r requirements.txt

# Database commands using manage.py
migrate:
	@if [ "$(msg)" = "" ]; then \
		echo "$(RED)Error: Please provide a message using msg=\"your message\"$(NC)"; \
		exit 1; \
	fi
	python manage.py migrate -m "$(msg)"

upgrade:
	python manage.py upgrade

downgrade:
	python manage.py downgrade

current:
	python manage.py current

history:
	python manage.py history

# Application commands
run:
	uvicorn app.main:app --reload

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete 