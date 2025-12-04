import pandas as pd
from npcpy.npc_compiler import NPC

def create_clinical_dataset_lab():
    trial_criteria = {
        'inclusion': [
            'Patients aged 18-65',
            'Diagnosed with Type 2 Diabetes', 
            'HbA1c between 7.0% and 9.0%',
            'No history of severe cardiovascular events'
        ],
        'exclusion': [
            'Pregnant or breastfeeding',
            'History of kidney failure', 
            'Currently on insulin therapy'
        ]
    }
    
    clinical_creator = NPC(
        name='Clinical Data Creator',
        primary_directive='Create realistic patient eligibility pairs for clinical trials',
        model='llama3.2',
        provider='ollama'
    )
    
    expected_format = '''
    {"clinical_pairs": [
        {"patient_summary": "45-year-old male with Type 2 Diabetes, HbA1c 7.5%", "eligibility_status": "Eligible"},
        {"patient_summary": "30-year-old pregnant female with Type 2 Diabetes", "eligibility_status": "Ineligible (Pregnant)"}
    ]}
    '''
    
    criteria_text = f"Inclusion: {'; '.join(trial_criteria['inclusion'])}. Exclusion: {'; '.join(trial_criteria['exclusion'])}"
    
    prompt = f"""Create 10 patient eligibility pairs for this clinical trial:
{criteria_text}

Include diverse scenarios with both eligible and ineligible patients.
Format as: {expected_format}"""
    
    response = clinical_creator.get_llm_response(prompt, format='json')
    clinical_data = response['response']['clinical_pairs']
    
    df = pd.DataFrame(clinical_data)
    df.to_csv('clinical_eligibility_dataset.csv', index=False)
    
    print(f"Created {len(clinical_data)} clinical pairs, saved to clinical_eligibility_dataset.csv")
    return df

clinical_dataset = create_clinical_dataset_lab()