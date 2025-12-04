import pandas as pd
from npcpy.npc_compiler import NPC

def create_conciseness_dataset():
    # Generate verbose vs concise response pairs
    prompts = [
        "What is machine learning?",
        "How do you make coffee?", 
        "Explain gravity",
        "What is Python programming?"
    ]
    
    generator = NPC(
        name='Response Generator',
        primary_directive='Generate both verbose and concise responses',
        model='llama3.2',
        provider='ollama'
    )
    
    preference_data = []
    
    for prompt in prompts:
        verbose_prompt = f"Give a detailed, comprehensive explanation of: {prompt}"
        concise_prompt = f"Give a brief, clear explanation of: {prompt}"
        
        verbose_response = generator.get_llm_response(verbose_prompt)
        concise_response = generator.get_llm_response(concise_prompt)
        
        preference_data.append({
            'prompt': prompt,
            'chosen': concise_response['response'],
            'rejected': verbose_response['response'],
            'chosen_length': len(concise_response['response'].split()),
            'rejected_length': len(verbose_response['response'].split())
        })
    
    return pd.DataFrame(preference_data)

def conciseness_dpo_demo():
    preference_df = create_conciseness_dataset()
    preference_df.to_csv('conciseness_preferences.csv', index=False)
    
    dpo_trainer = NPC(
        name='DPO Trainer',
        primary_directive='Configure DPO training for conciseness preference learning',
        model='llama3.2',
        provider='ollama'
    )
    
    config_format = '''
    {"dpo_config": {
        "beta": 0.1,
        "learning_rate": 1e-5,
        "epochs": 1,
        "batch_size": 2,
        "max_length": 512,
        "ref_model": "base_model_path"
    }}
    '''
    
    config_prompt = f"""Configure DPO training for teaching conciseness preference.
Dataset: {len(preference_df)} preference pairs
Goal: Prefer shorter, clearer responses over verbose ones

Recommend DPO hyperparameters.
Format as: {config_format}"""
    
    config_response = dpo_trainer.get_llm_response(config_prompt, format='json')
    config = config_response['response']['dpo_config']
    
    config_df = pd.DataFrame([config])
    config_df.to_csv('dpo_config.csv', index=False)
    
    print("DPO training configuration created for conciseness preference")
    print(f"Training on {len(preference_df)} preference pairs")
    
    return preference_df, config

concise_prefs, dpo_config = conciseness_dpo_demo()