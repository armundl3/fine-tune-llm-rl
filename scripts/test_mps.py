#!/usr/bin/env python3
"""
Test script to verify Apple Silicon MPS (Metal Performance Shaders) support.
This script checks if PyTorch can access the Metal backend for GPU acceleration.
"""

import sys

try:
    import torch
except ImportError:
    print("ERROR: PyTorch is not installed.")
    print("Install with: uv add torch torchvision torchaudio")
    sys.exit(1)


def test_mps():
    """Test MPS availability and basic functionality."""
    print("PyTorch MPS Support Test")
    print("=" * 50)
    print(f"PyTorch version: {torch.__version__}")
    print()

    # Check if MPS is available
    mps_available = torch.backends.mps.is_available()
    print(f"MPS Available: {mps_available}")

    if not mps_available:
        print()
        print("WARNING: MPS is not available on this system.")
        print("Possible reasons:")
        print("  - Not running on macOS")
        print("  - Not running on Apple Silicon (M1/M2/M3/M4)")
        print("  - PyTorch version too old (needs 1.12+)")
        return False

    # Check if MPS is built
    mps_built = torch.backends.mps.is_built()
    print(f"MPS Built: {mps_built}")

    # Try to create a tensor on MPS device
    try:
        print()
        print("Testing MPS device...")
        device = torch.device("mps")
        x = torch.ones(5, 5, device=device)
        y = torch.ones(5, 5, device=device)
        z = x + y
        print(f"✓ Successfully created and computed tensors on MPS device")
        print(f"  Result shape: {z.shape}")
        print(f"  Result device: {z.device}")
        print()
        print("SUCCESS: MPS is fully functional!")
        return True
    except Exception as e:
        print(f"✗ Failed to use MPS device: {e}")
        return False


if __name__ == "__main__":
    success = test_mps()
    sys.exit(0 if success else 1)
