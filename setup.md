# Local LLM Fine‑Tuning Environment Setup (MacBook Pro M4 Max + uv)

This document provides a clean, repeatable setup using **uv** as your Python package manager and
Apple Silicon–compatible libraries for fine‑tuning LLMs on a MacBook Pro M4 Max (64GB RAM).

---

## 1. Prerequisites

### Install Homebrew (if missing)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install pyenv (Python version manager)
```bash
brew install pyenv
```

Add to your shell profile (`~/.zshrc` or `~/.bash_profile`):
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Restart your shell or run:
```bash
source ~/.zshrc  # or source ~/.bash_profile
```

### Install Python 3.13
```bash
pyenv install 3.13
pyenv global 3.13
```

Verify:
```bash
python --version  # Should show Python 3.13.x
```

### Install uv (Python + package manager)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify:
```bash
uv --version
```

---

## 2. Quick Start with Makefile (Recommended)

This project includes a `Makefile` to automate setup and common tasks.

### One-Command Setup
```bash
# Clone or navigate to the project directory
cd fine-tune-llm-rl

# Set up environment and install dependencies
make setup
source .venv/bin/activate
make install
```

### Available Commands
Run `make help` to see all available commands:
```bash
make help         # Show all available commands
make setup        # Set up pyenv + virtual environment
make install      # Install all dependencies
make sync         # Sync from existing pyproject.toml (faster)
make verify-mps   # Test Apple Silicon MPS support
make clean        # Remove virtual environment
```

**Benefits of using the Makefile:**
- Consistent setup process across team members
- One-command automation for complex tasks
- Self-documenting (targets explain what they do)
- Reduces errors from manual steps

The sections below provide detailed manual steps for transparency and customization.

---

## 3. Manual Setup (Alternative)

If you prefer manual control or want to understand each step, follow the sections below.

### 2.1 Create the Project

```bash
mkdir llm-finetune
cd llm-finetune

# Set Python 3.13 as the local version for this project
pyenv local 3.13

# Create virtual environment with Python 3.13
uv venv
source .venv/bin/activate
```

---

### 2.2 Initialize pyproject.toml

Initialize the project with a `pyproject.toml` file for dependency management:

```bash
uv init --no-workspace
```

This creates a `pyproject.toml` with basic project metadata. The `--no-workspace` flag keeps it simple for a single project.

**Note:** The `pyproject.toml` will be configured to require Python 3.13+.

**Alternatively**, you can skip this step and let `uv add` create the file automatically when you install your first package.

---

### 2.3 Install PyTorch (MPS/Metal Backend)

**Do NOT install CUDA wheels — Mac does not support CUDA.**

```bash
uv add torch torchvision torchaudio
```

Verify MPS:
```python
import torch
print(torch.backends.mps.is_available())
```

Should output: `True`

---

### 2.4 Install Core Training Libraries

```bash
uv add transformers datasets accelerate sentencepiece
uv add peft trl
uv add mlx-lm
```

**Notes:**
- Using `uv add` automatically manages dependencies in `pyproject.toml` for better reproducibility.
- **`bitsandbytes` is NOT supported on macOS** — it only has wheels for Linux/Windows. For quantization on Apple Silicon, use `mlx-lm` instead.
- `mlx-lm` is Apple's optimized LLM training library with built-in quantization support for Apple Silicon.

---

### 2.5 Configure Accelerate

```bash
accelerate config
```

Recommended options:
- single device
- device = mps
- mixed precision fp16

---

## 4. Verify Installation

### Run a Test Script

```bash
python scripts/test_mps.py
```

You should see:
```
MPS Available: True
```

Or with the Makefile:
```bash
make verify-mps
```

---

## 5. Good Local Model Sizes

| Model Size | Training Type       | M4 Max (64GB RAM) |
|-----------|---------------------|-------------------|
| 1B–3B     | Full SFT            | Excellent         |
| 7B–8B     | LoRA / MLX Quantize | Good              |
| 14B       | LoRA / MLX Quantize | Borderline        |
| 30B+      | Cloud GPU           | Not recommended   |

**Note:** On macOS, use MLX for quantization instead of QLoRA/bitsandbytes. Use cloud (RunPod, Colab, Lambda Labs) for larger DPO/SFT runs or when you need bitsandbytes compatibility.

---

## 6. Project Structure (Included in Skeleton)

```
llm-finetune/
│
├── .python-version    # pyenv local version file (3.13)
├── Makefile           # Automation for setup and common tasks
├── setup.md
├── pyproject.toml     # Python dependencies (pinned versions)
├── uv.lock            # Lockfile for reproducible installs
├── requirements.txt
├── scripts/
│   ├── test_mps.py
│   └── train_sft.py
├── data/
│   └── README.md
└── models/
    └── README.md
```

---

## 7. Version Control

```bash
git init
git add .
git commit -m "Initial LLM fine-tuning skeleton setup"
```

---

You are ready to begin fine‑tuning LLMs on your Mac.
