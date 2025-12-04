# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project for fine-tuning LLMs with reinforcement learning on Apple Silicon (MacBook Pro M4 Max). The project is optimized for local development using Apple's Metal Performance Shaders (MPS) backend and MLX framework.

## Environment Setup

### Python Version Management
- **Python version**: Pinned to 3.13.7 (managed via pyenv)
- **Package manager**: uv (modern, fast Python package manager)
- **Virtual environment**: `.venv` directory (managed by uv)

### Key Environment Files
- `.python-version`: Specifies Python 3.13 for pyenv
- `pyproject.toml`: Python dependencies with **exact version pinning** (all versions use `==`)
- `uv.lock`: Lockfile for reproducible installations

## Common Commands

### Environment Setup
```bash
make setup              # Set up pyenv + virtual environment
source .venv/bin/activate
make install           # Install all dependencies from scratch
make sync              # Sync from existing pyproject.toml (faster)
```

### Development
```bash
make verify-mps        # Test Apple Silicon MPS support
make configure-accelerate  # Configure accelerate for MPS
make versions          # Show Python and package versions
make clean             # Remove virtual environment and cache
```

### Testing and Training
```bash
make test              # Run tests (when tests/ exists)
make train             # Run training script (scripts/train_sft.py)
```

## Architecture Notes

### Apple Silicon Specific Setup
- **GPU Backend**: Uses PyTorch MPS (Metal Performance Shaders) for GPU acceleration
- **Quantization**: Uses `mlx-lm` instead of `bitsandbytes` (which is NOT compatible with macOS)
- **Accelerate Config**: Should be configured for single device, MPS, fp16 mixed precision

### Key Libraries
- **PyTorch**: Installed with MPS support (no CUDA)
- **Transformers**: Hugging Face library for LLM models
- **PEFT**: Parameter-Efficient Fine-Tuning (LoRA support)
- **TRL**: Transformer Reinforcement Learning library
- **MLX-LM**: Apple's optimized LLM library with built-in quantization for Apple Silicon
- **Accelerate**: Training acceleration library

### Directory Structure
```
scripts/         # Training and utility scripts
  test_mps.py   # MPS availability verification script
data/           # Training datasets (raw, processed, splits)
models/         # Model storage (base models, checkpoints, final models)
```

## Platform Constraints

### macOS-Specific Limitations
1. **No bitsandbytes**: The `bitsandbytes` package does NOT work on macOS. Use `mlx-lm` for quantization instead.
2. **MPS Backend Required**: All PyTorch operations should target the MPS device for GPU acceleration.
3. **Model Size Recommendations** (for 64GB RAM):
   - 1B-3B: Full fine-tuning works well
   - 7B-8B: Use LoRA or MLX quantization
   - 14B: LoRA or MLX quantization (borderline)
   - 30B+: Use cloud GPU services

## Dependency Management

### Adding New Packages
```bash
uv add package-name           # Adds with >= constraint
uv add "package-name==1.2.3"  # Pins to specific version
```

**Important**: This project uses exact version pinning (`==`) in `pyproject.toml` for reproducibility. When adding new packages, consider pinning to specific versions.

### Updating Packages
```bash
uv add package-name@latest    # Update to latest version
```

## Important Files

- **setup.md**: Comprehensive setup documentation with both Makefile and manual instructions
- **Makefile**: Automation for common tasks (preferred method)
- **CHANGELOG.md**: Project history and change log (see Changelog Maintenance section)
- **scripts/test_mps.py**: Verifies PyTorch MPS backend is working correctly
- **pyproject.toml**: Python 3.13.7 requirement + pinned dependencies

## Changelog Maintenance

**REQUIRED**: All significant changes and git commits MUST be documented in `CHANGELOG.md`.

### When to Update CHANGELOG.md
- **Before every git commit**: Document what you're committing
- After adding new features, scripts, or capabilities
- After fixing bugs or issues
- After making architectural changes
- After updating dependencies or configurations

### Changelog Format
Use these categories in the `[Unreleased]` section:
- **Added**: New features, files, or capabilities
- **Changed**: Changes to existing functionality
- **Deprecated**: Features that will be removed
- **Removed**: Removed features or files
- **Fixed**: Bug fixes
- **Security**: Security-related changes

### Example Workflow
```bash
# 1. Make your changes
vim scripts/train_lora.py

# 2. Update CHANGELOG.md FIRST
vim CHANGELOG.md
# Add entry under [Unreleased] -> ### Added
# - scripts/train_lora.py: LoRA fine-tuning implementation

# 3. Then commit
git add scripts/train_lora.py CHANGELOG.md
git commit -m "Add LoRA training script"
```

### Guidelines
- Be specific: Include file names and component names
- Be concise: One line per change is usually enough
- Be consistent: Follow the existing format
- Reference CHANGELOG.md: When implementing features, check the changelog to understand project history

## Development Workflow

1. **First-time setup**: Run `make setup && source .venv/bin/activate && make install`
2. **Existing setup**: Run `source .venv/bin/activate && make sync`
3. **Verify GPU**: Run `make verify-mps` to ensure MPS is working
4. **Configure training**: Run `make configure-accelerate` before first training run
5. **Training**: Place datasets in `data/`, models in `models/`, scripts in `scripts/`
6. **Before committing**: Update `CHANGELOG.md` with your changes (see Changelog Maintenance)

## Training Architecture

When implementing training scripts:
- Target the `mps` device for GPU operations: `torch.device("mps")`
- Use MLX for quantization (not bitsandbytes)
- Use PEFT/LoRA for memory-efficient fine-tuning of larger models
- Configure accelerate for single device MPS training
- Save checkpoints to `models/checkpoints/`
- Save final models to `models/final/`
