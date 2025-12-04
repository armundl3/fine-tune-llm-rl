import pandas as pd
from npcpy.npc_compiler import NPC

def clinical_safety_dpo_lab():
    try:
        preference_df = pd.read_csv('clinical_preference_pairs.csv')
    except:
        print("Creating clinical preference pairs first...")
        from Module10 import create_clinical_preference_lab
        _, _, preference_df = create_clinical_preference_lab()
    
    # Expand the dataset with more safety-focused examples
    additional_cases = [
        {
            'prompt': 'Evaluate 45-year-old with diabetes and mild depression for antidepressant trial',
            'chosen': 'Step 1: Check inclusion criteria...\nStep 2: Review psychiatric history...\nStep 3: Assess drug interactions...\nStep 4: Consider suicide risk factors...\nConclusion: Requires psychiatric evaluation before enrollment',
            'rejected': 'Patient has diabetes and depression. Meets inclusion criteria. Eligible for trial.',
            'safety_principle': 'Comprehensive psychiatric safety assessment vs superficial screening'
        },
        {
            'prompt': 'Evaluate 70-year-old with multiple conditions for experimental drug trial',
            'chosen': 'Step 1: Age exceeds inclusion criteria (18-65)\nStep 2: Multiple comorbidities increase risk\nConclusion: Ineligible due to age and safety concerns',
            'rejected': 'Patient enthusiastic about trial participation. Consider exception to age limit.',
            'safety_principle': 'Strict adherence to safety criteria vs flexible enrollment'
        }
    ]
    
    # Combine datasets
    full_preference_df = pd.concat([preference_df, pd.DataFrame(additional_cases)], ignore_index=True)
    
    dpo_clinical_trainer = NPC(
        name='Clinical DPO Trainer',
        primary_directive='Configure DPO training for clinical safety alignment',
        model='gemma3:4b',
        provider='ollama'
    )
    
    config_format = '''
    {"clinical_dpo_config": {
        "beta": 0.1,
        "learning_rate": 5e-6,
        "epochs": 2,
        "batch_size": 1,
        "max_length": 1024,
        "safety_weight": 1.5,
        "eval_steps": 50
    }}
    '''
    
    training_prompt = f"""Configure DPO for clinical safety alignment.
Dataset: {len(full_preference_df)} safety-focused preference pairs
Goal: Prefer cautious, thorough clinical reasoning over hasty decisions

Safety-critical domain requires special considerations.
Format as: {config_format}"""
    
    config_response = dpo_clinical_trainer.get_llm_response(training_prompt, format='json')
    clinical_config = config_response['response']['clinical_dpo_config']
    
    # Save training setup
    full_preference_df.to_csv('clinical_safety_dpo_dataset.csv', index=False)
    clinical_config_df = pd.DataFrame([clinical_config])
    clinical_config_df.to_csv('clinical_dpo_config.csv', index=False)
    
    # Test the concept with before/after comparison
    test_case = "Evaluate 55-year-old diabetic patient with family history of heart disease"
    
    before_response = dpo_clinical_trainer.get_llm_response(
        f"Quickly assess: {test_case}"
    )
    
    after_prompt = f"""Following safety-first clinical reasoning principles, thoroughly evaluate: {test_case}
    
Consider all risk factors, inclusion/exclusion criteria, and safety implications."""
    
    after_response = dpo_clinical_trainer.get_llm_response(after_prompt)
    
    comparison_df = pd.DataFrame([{
        'test_case': test_case,
        'before_training': before_response['response'],
        'after_training': after_response['response'],
        'before_length': len(before_response['response'].split()),
        'after_length': len(after_response['response'].split())
    }])
    
    comparison_df.to_csv('dpo_before_after_comparison.csv', index=False)
    
    print("Clinical Safety DPO training setup complete")
    print(f"Dataset: {len(full_preference_df)} preference pairs")
    print(f"Configuration saved with safety-focused parameters")
    
    return full_preference_df, clinical_config, comparison_df

safety_dpo_data, safety_config, comparison = clinical_safety_dpo_lab()