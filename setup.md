# Local LLM Fine‑Tuning Environment Setup (MacBook Pro M4 Max + uv)

This document provides a clean, repeatable setup using **uv** as your Python package manager and
Apple Silicon–compatible libraries for fine‑tuning LLMs on a MacBook Pro M4 Max (64GB RAM).

---

## 1. Prerequisites

### Install Homebrew (if missing)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
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

## 2. Create the Project

```bash
mkdir llm-finetune
cd llm-finetune
uv venv
source .venv/bin/activate
```

---

## 3. Install PyTorch (MPS/Metal Backend)

**Do NOT install CUDA wheels — Mac does not support CUDA.**

```bash
uv pip install torch torchvision torchaudio
```

Verify MPS:
```python
import torch
print(torch.backends.mps.is_available())
```

Should output: `True`

---

## 4. Install Core Training Libraries

```bash
uv pip install transformers datasets accelerate sentencepiece
uv pip install peft trl bitsandbytes
uv pip install mlx-lm
```

**Notes:**
- `bitsandbytes` runs in CPU‑only mode on Mac, but still enables 4‑bit QLoRA.
- `mlx-lm` is Apple’s optimized LLM training library.

---

## 5. Configure Accelerate

```bash
accelerate config
```

Recommended options:
- single device
- device = mps
- mixed precision fp16

---

## 6. Run a Test Script

```bash
python scripts/test_mps.py
```

You should see:
```
MPS Available: True
```

---

## 7. Good Local Model Sizes

| Model Size | Training Type | M4 Max (64GB RAM) |
|-----------|----------------|-------------------|
| 1B–3B     | Full SFT       | Excellent         |
| 7B–8B     | QLoRA          | Good              |
| 14B       | QLoRA          | Borderline        |
| 30B+      | Cloud GPU      | Not recommended   |

Use cloud (RunPod, Colab, Lambda Labs) for larger DPO/SFT runs.

---

## 8. Project Structure (Included in Skeleton)

```
llm-finetune/
│
├── setup.md
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

## 9. Version Control

```bash
git init
git add .
git commit -m "Initial LLM fine-tuning skeleton setup"
```

---

You are ready to begin fine‑tuning LLMs on your Mac.
