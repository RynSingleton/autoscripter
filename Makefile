# Makefile for autoscripter project

# Python interpreter
PYTHON := python3
PIP := pip3

# Virtual environment
VENV := venv
VENV_BIN := $(VENV)/bin
VENV_PYTHON := $(VENV_BIN)/python
VENV_PIP := $(VENV_BIN)/pip

# Project directories
SRC_DIR := src
TEST_DIR := tests
BUILD_DIR := build
DIST_DIR := dist

# Main script
MAIN_SCRIPT := $(SRC_DIR)/autoscripter.py

.PHONY: all clean venv install install-dev run test lint format help

# Default target
all: venv install

# Create virtual environment (only if it doesn't exist)
$(VENV_BIN)/activate:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created in $(VENV)/"

venv: $(VENV_BIN)/activate

# Install production dependencies
install: $(VENV_BIN)/activate
	@echo "Installing dependencies..."
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements.txt
	@touch $(VENV_BIN)/activate

# Install development dependencies (testing, linting, etc.)
install-dev: install
	@echo "Installing development dependencies..."
	$(VENV_PIP) install -r requirements-dev.txt

# Run the main script
run: 
	@echo "Running autoscripter..."
	$(VENV_PYTHON) -B $(MAIN_SCRIPT)

# Run tests
test:
	@echo "Running tests..."
	$(VENV_PYTHON) -m pytest $(TEST_DIR)

# Run linter (check code quality)
lint:
	@echo "Running linter..."
	$(VENV_PYTHON) -m pylint $(SRC_DIR)

# Format code
format:
	@echo "Formatting code..."
	$(VENV_PYTHON) -m black $(SRC_DIR) $(TEST_DIR)

# Clean build artifacts and cache
clean:
	@echo "Cleaning up..."
	rm -rf $(BUILD_DIR) $(DIST_DIR)
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.egg-info" -exec rm -rf {} +
	@echo "Cleanup complete."

# Initialize project structure
init:
	@echo "Initializing project structure..."
	mkdir -p $(SRC_DIR) $(TEST_DIR) $(BUILD_DIR) $(DIST_DIR)
	touch $(SRC_DIR)/__init__.py
	touch $(TEST_DIR)/__init__.py
	@echo "Project structure created."

# Show help
help:
	@echo "Available targets:"
	@echo "  make all          - Create venv and install dependencies"
	@echo "  make venv         - Create virtual environment"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install dev dependencies"
	@echo "  make run          - Run the main script"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linter"
	@echo "  make format       - Format code with black"
	@echo "  make clean        - Remove build artifacts and venv"
	@echo "  make init         - Create project directory structure"
	@echo "  make help         - Show this help message"