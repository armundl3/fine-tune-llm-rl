.PHONY: help setup install sync verify-mps clean test train

# Default target - show help
help:
	@echo "Fine-tune LLM RL - Available Commands"
	@echo "======================================"
	@echo ""
	@echo "Setup commands:"
	@echo "  make setup       - Set up pyenv Python 3.13 and create virtual environment"
	@echo "  make install     - Install all dependencies with uv add"
	@echo "  make sync        - Sync dependencies from pyproject.toml (faster)"
	@echo ""
	@echo "Verification:"
	@echo "  make verify-mps  - Test Apple Silicon MPS support"
	@echo ""
	@echo "Development:"
	@echo "  make test        - Run tests"
	@echo "  make train       - Run training script"
	@echo "  make clean       - Remove virtual environment and cache files"
	@echo ""
	@echo "Quick start: make setup && source .venv/bin/activate && make install"

# Set up Python version and virtual environment
setup:
	@echo "Setting Python version to 3.13 with pyenv..."
	pyenv local 3.13
	@echo "Creating virtual environment with uv..."
	uv venv
	@echo ""
	@echo "Setup complete! Activate the environment with:"
	@echo "  source .venv/bin/activate"

# Install all dependencies from scratch
install:
	@echo "Installing PyTorch with MPS support..."
	uv add torch torchvision torchaudio
	@echo "Installing core training libraries..."
	uv add transformers datasets accelerate sentencepiece
	uv add peft trl
	@echo "Installing MLX (Apple Silicon optimized)..."
	uv add mlx-lm
	@echo ""
	@echo "All dependencies installed!"

# Sync dependencies from existing pyproject.toml
sync:
	@echo "Syncing dependencies from pyproject.toml..."
	uv sync
	@echo "Dependencies synced!"

# Verify MPS (Metal Performance Shaders) availability
verify-mps:
	@echo "Testing Apple Silicon MPS support..."
	@python scripts/test_mps.py

# Configure accelerate for MPS
configure-accelerate:
	@echo "Configuring accelerate for Apple Silicon..."
	@echo "Recommended settings: single device, mps, mixed precision fp16"
	accelerate config

# Run tests
test:
	@echo "Running tests..."
	@if [ -d "tests" ]; then \
		pytest tests/ -v; \
	else \
		echo "No tests directory found. Create tests/ to add tests."; \
	fi

# Run training script
train:
	@echo "Starting training..."
	@if [ -f "scripts/train_sft.py" ]; then \
		python scripts/train_sft.py; \
	else \
		echo "Training script not found at scripts/train_sft.py"; \
	fi

# Clean up virtual environment and cache files
clean:
	@echo "Cleaning up..."
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleanup complete!"

# Show Python and package versions
versions:
	@echo "Python version:"
	@python --version
	@echo ""
	@echo "Key package versions:"
	@uv pip list | grep -E "(torch|transformers|mlx-lm|peft|trl)" || echo "Environment not set up yet"
