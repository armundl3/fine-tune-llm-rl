import pandas as pd
from npcpy.npc_compiler import NPC

def clinical_sft_training_lab():
    # Load the dataset we created earlier
    try:
        df = pd.read_csv('clinical_eligibility_dataset.csv')
    except:
        print("Creating clinical dataset first...")
        from Module2 import create_clinical_dataset_lab
        df = create_clinical_dataset_lab()
    
    sft_trainer = NPC(
        name='SFT Trainer',
        primary_directive='Configure supervised fine-tuning for clinical eligibility prediction',
        model='gemma3:4b',
        provider='ollama'
    )
    
    training_config_format = '''
    {"training_config": {
        "model_name": "google/gemma-2b-it",
        "lora_r": 16,
        "lora_alpha": 32,
        "learning_rate": 2e-4,
        "batch_size": 4,
        "epochs": 3,
        "max_seq_length": 512,
        "gradient_accumulation_steps": 1
    }}
    '''
    
    prompt = f"""Configure SFT training for clinical eligibility prediction.
Dataset: {len(df)} patient cases
Task: Predict eligibility status from patient summaries

Recommend training hyperparameters for Gemma-2B.
Format as: {training_config_format}"""
    
    response = sft_trainer.get_llm_response(prompt, format='json')
    config = response['response']['training_config']
    
    # Prepare training format
    training_data = []
    for _, row in df.iterrows():
        training_data.append({
            'input': f"Patient: {row['patient_summary']}",
            'output': row['eligibility_status']
        })
    
    training_df = pd.DataFrame(training_data)
    training_df.to_csv('clinical_sft_training.csv', index=False)
    
    config_df = pd.DataFrame([config])
    config_df.to_csv('sft_training_config.csv', index=False)
    
    print(f"SFT training setup complete with {len(training_data)} examples")
    return training_df, config

sft_data, sft_config = clinical_sft_training_lab()