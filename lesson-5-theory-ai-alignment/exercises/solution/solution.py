import pandas as pd
from npcpy.npc_compiler import NPC

def create_clinical_preference_lab():
    patient_case = {
        'patient_id': 'P201',
        'summary': '60-year-old female, Type 2 Diabetes, HbA1c 7.6%, recent mild heart arrhythmia (resolved)',
        'trial_criteria': 'Inclusion: Age 18-65, Type 2 Diabetes, HbA1c 7.0-9.0%. Exclusion: severe cardiovascular events, kidney failure, pregnant/breastfeeding'
    }
    
    traces = {
        'trace_a': """
Step 1: Check inclusion - Age 60 (OK), Type 2 Diabetes (OK), HbA1c 7.6% (OK)
Step 2: Check exclusion - Not pregnant (OK), no kidney failure (OK)  
Step 3: Conclude: Patient P201 is Eligible
""",
        'trace_b': """
Step 1: Check inclusion - Age 60 (OK), Type 2 Diabetes (OK), HbA1c 7.6% (OK)
Step 2: Check exclusion - Not pregnant (OK), no kidney failure (OK)
Step 3: Review cardiovascular history - Note "recent mild heart arrhythmia (resolved)"
Step 4: Consider: Arrhythmia could indicate cardiovascular risk despite being "mild"
Step 5: Conclude: Patient P201 is Ineligible (Potential cardiovascular risk, requires further review)
""",
        'trace_c': """
Step 1: Any heart condition mentioned? Yes - "heart arrhythmia"
Step 2: Conclude: Patient P201 is Ineligible (Cardiovascular history)
"""
    }
    
    safety_evaluator = NPC(
        name='Safety Evaluator',
        primary_directive='Rank clinical decision traces by patient safety priority',
        model='llama3.2',
        provider='ollama'
    )
    
    evaluation_prompt = f"""Rank these 3 clinical decision traces for patient safety:

Patient: {patient_case['summary']}
Criteria: {patient_case['trial_criteria']}

Trace A: {traces['trace_a']}
Trace B: {traces['trace_b']}  
Trace C: {traces['trace_c']}

Rank from best (1) to worst (3) considering patient safety."""
    
    ranking = safety_evaluator.get_llm_response(evaluation_prompt)
    
    # Create preference pairs based on safety-first principle
    preference_pairs = [
        {
            'prompt': f"Evaluate {patient_case['patient_id']} for trial eligibility",
            'chosen': traces['trace_b'],
            'rejected': traces['trace_a'],
            'safety_principle': 'Thorough cardiovascular risk assessment vs incomplete evaluation'
        },
        {
            'prompt': f"Evaluate {patient_case['patient_id']} for trial eligibility", 
            'chosen': traces['trace_b'],
            'rejected': traces['trace_c'],
            'safety_principle': 'Reasoned caution vs overly simplistic rejection'
        }
    ]
    
    case_df = pd.DataFrame([patient_case])
    traces_df = pd.DataFrame([{'trace_id': k, 'content': v} for k, v in traces.items()])
    preference_df = pd.DataFrame(preference_pairs)
    
    case_df.to_csv('patient_case.csv', index=False)
    traces_df.to_csv('clinical_traces.csv', index=False)
    preference_df.to_csv('clinical_preference_pairs.csv', index=False)
    
    print("Clinical safety preference pairs created")
    print(f"Ranking result: {ranking['response']}")
    return case_df, traces_df, preference_df

case_data, trace_data, clinical_preferences = create_clinical_preference_lab()