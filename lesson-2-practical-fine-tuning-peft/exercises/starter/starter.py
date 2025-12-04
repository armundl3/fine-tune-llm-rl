# SFT Fine-Tuning - Starter Code
# Module 2: Practical Fine-Tuning with PEFT

import torch
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from trl import SFTTrainer
import pandas as pd
import json

class SFTConfig:
    """Configuration for SFT fine-tuning."""
    base_model_name = "google/gemma-3-270m-it"
    output_model_path = "models/sft_prediction_model_gemma_270m"
    sft_data_path = "clinical_sft_dataset.csv"
    
    # LoRA parameters - TODO: Configure these appropriately
    lora_r = 8
    lora_alpha = 16
    lora_dropout = 0.15
    lora_target_modules = ["q_proj", "v_proj"]
    
    # Training parameters - TODO: Tune these
    num_train_epochs = 20
    per_device_train_batch_size = 2
    gradient_accumulation_steps = 4
    learning_rate = 3e-5

def load_and_format_dataset(csv_path: str):
    """
    Load and format the SFT dataset for training.
    TODO: Implement dataset loading and formatting
    """
    print("Loading dataset...")
    # Placeholder - implement dataset loading
    return []

def configure_lora():
    """
    Configure LoRA parameters for efficient fine-tuning.
    TODO: Implement LoRA configuration
    """
    return None

def run_sft_training(config: SFTConfig, train_examples):
    """
    Run the SFT training process.
    TODO: Implement training loop
    """
    print("Starting SFT training...")
    # Placeholder training logic

def validate_model(model, tokenizer, val_examples):
    """
    Validate the fine-tuned model on validation examples.
    TODO: Implement validation
    """
    print("Validating model...")
    return 0.0, 0.0  # Placeholder metrics

if __name__ == "__main__":
    config = SFTConfig()
    
    # Load and format dataset
    train_examples = load_and_format_dataset(config.sft_data_path)
    
    if not train_examples:
        print("No training examples found. Please generate the dataset first.")
        exit(1)
    
    # Configure LoRA
    peft_config = configure_lora()
    
    # Run training
    run_sft_training(config, train_examples)
    
    print("SFT training completed!")
    print("Next steps: Evaluate model performance and analyze training metrics.")
