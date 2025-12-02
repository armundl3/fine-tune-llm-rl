# Data Directory

Place your training datasets here.

## Suggested Structure

```
data/
├── raw/           # Original, unprocessed datasets
├── processed/     # Cleaned and preprocessed data
└── splits/        # Train/validation/test splits
```

## Common Dataset Sources

- Hugging Face Datasets: https://huggingface.co/datasets
- Local JSON/CSV files
- Custom data loaders

## Example Usage

```python
from datasets import load_dataset

# Load from Hugging Face
dataset = load_dataset("dataset-name")

# Load from local files
dataset = load_dataset("json", data_files="data/raw/my_data.json")
```
