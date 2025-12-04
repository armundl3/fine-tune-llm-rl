# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- Placeholder for upcoming changes

## [2025-12-02] - Initial Setup

### Added
- Project initialization with Python 3.13.7 via pyenv
- Environment management with uv package manager
- PyTorch with Apple Silicon MPS support
- Core ML libraries: transformers, datasets, accelerate, sentencepiece, peft, trl
- MLX-LM for Apple Silicon optimized training (replaces bitsandbytes)
- Project structure: scripts/, data/, models/ directories
- Makefile for automated setup and common tasks
  - `make setup`: Environment setup
  - `make install`: Dependency installation
  - `make verify-mps`: MPS verification
  - `make sync`: Fast dependency sync
  - `make clean`: Cleanup
- Documentation:
  - setup.md: Comprehensive setup guide
  - CLAUDE.md: AI assistant guidance
  - CHANGELOG.md: This file
- MPS verification script (scripts/test_mps.py)
- Pinned dependencies in pyproject.toml for reproducibility

### Notes
- Project optimized for MacBook Pro M4 Max (64GB RAM)
- Uses MPS (Metal Performance Shaders) for GPU acceleration
- bitsandbytes excluded due to macOS incompatibility

---

## How to Update This Changelog

### Before Making a Git Commit
1. Add your changes under the `[Unreleased]` section
2. Use the following categories:
   - **Added**: New features, files, or capabilities
   - **Changed**: Changes to existing functionality
   - **Deprecated**: Features that will be removed
   - **Removed**: Removed features or files
   - **Fixed**: Bug fixes
   - **Security**: Security-related changes

3. When ready to tag a release, move `[Unreleased]` items to a new dated section

### Entry Format
```markdown
### Added
- Brief description of what was added
- Can include file names or component names for clarity

### Fixed
- Description of bug fix with context
```

### Examples
```markdown
## [2025-12-15] - LoRA Training Implementation

### Added
- scripts/train_lora.py: LoRA fine-tuning script for 7B models
- Configuration files for Llama 3 and Mistral models
- Gradient checkpointing for memory optimization

### Changed
- Updated training batch size recommendations in CLAUDE.md
- Modified data preprocessing to handle instruction format

### Fixed
- OOM errors during training on 7B models
- MPS device allocation bug in training loop
```
