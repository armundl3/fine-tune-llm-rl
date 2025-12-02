# Models Directory

Store trained models, checkpoints, and downloaded base models here.

## Suggested Structure

```
models/
├── base/          # Downloaded pretrained models
├── checkpoints/   # Training checkpoints
└── final/         # Final trained models
```

## Model Storage

### Download Base Models

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("model-name")
tokenizer = AutoTokenizer.from_pretrained("model-name")

# Save locally
model.save_pretrained("models/base/model-name")
tokenizer.save_pretrained("models/base/model-name")
```

### Save Checkpoints

Training scripts should save checkpoints to `models/checkpoints/` during training.

### Final Models

After training, save your best model to `models/final/` for deployment.

## Recommended Base Models for Apple Silicon

- **1B-3B**: TinyLlama, Phi-2, StableLM
- **7B-8B**: Llama 3 8B, Mistral 7B (with LoRA/MLX quantization)
