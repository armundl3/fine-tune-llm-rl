import pandas as pd
from npcpy.npc_compiler import NPC

def get_patient_record(patient_id):
    # Mock patient records
    patients = {
        'P101': {'age': 55, 'conditions': ['Type 2 Diabetes', 'Hypertension'], 'hba1c': 7.8},
        'P102': {'age': 30, 'conditions': ['Asthma'], 'hba1c': None},
        'P103': {'age': 67, 'conditions': ['Type 2 Diabetes'], 'hba1c': 8.2}
    }
    return patients.get(patient_id, {})

def check_inclusion_criteria(patient_data, trial_criteria):
    # Mock criteria checking
    age_ok = 18 <= patient_data.get('age', 0) <= 65
    diabetes_ok = 'Type 2 Diabetes' in patient_data.get('conditions', [])
    hba1c_ok = patient_data.get('hba1c', 0) and 7.0 <= patient_data['hba1c'] <= 9.0
    return {'age': age_ok, 'diabetes': diabetes_ok, 'hba1c': hba1c_ok}

def clinical_trial_agent_design_lab():
    clinical_agent = NPC(
        name='Clinical Trial Matching Agent',
        primary_directive='Match patients to appropriate clinical trials safely and accurately',
        model='llama3.2',
        provider='ollama',
        tools=[get_patient_record, check_inclusion_criteria]
    )
    
    design_doc = """
Clinical Trial Matching Agent Design Document

Primary Goal: Accurately match eligible patients to clinical trials while prioritizing patient safety

Necessary Tools:
- get_patient_record(patient_id): Retrieve complete medical history
- check_inclusion_criteria(patient_data, trial_criteria): Verify eligibility  
- check_drug_interactions(current_meds, trial_drugs): Safety check
- calculate_risk_score(patient_profile): Assess trial suitability
- log_decision(patient_id, trial_id, decision, reasoning): Audit trail

Hypothetical Reasoning Trace for Patient P101, Trial T202:

1. Observe: Request to evaluate Patient P101 for Trial T202
2. Think: Need patient medical history and trial criteria
3. Act: get_patient_record('P101')
4. Observe: P101 - Age 55, Type 2 Diabetes, HbA1c 7.8%, medications: Metformin
5. Think: Patient meets age and diabetes criteria, HbA1c in range
6. Act: check_inclusion_criteria(patient_data, trial_criteria)
7. Observe: All inclusion criteria met
8. Think: Now check exclusion criteria for safety
9. Act: Check for pregnancy, kidney failure, insulin therapy
10. Observe: No exclusion criteria present
11. Think: Patient appears eligible, document decision
12. Act: log_decision('P101', 'T202', 'Eligible', 'All criteria met')
"""
    
    with open('clinical_agent_design.txt', 'w') as f:
        f.write(design_doc)
    
    # Test reasoning trace
    test_cases = [
        {'patient_id': 'P101', 'trial': 'T202'},
        {'patient_id': 'P102', 'trial': 'T202'},
        {'patient_id': 'P103', 'trial': 'T202'}
    ]
    
    results = []
    for case in test_cases:
        patient_data = get_patient_record(case['patient_id'])
        eligibility = check_inclusion_criteria(patient_data, {})
        results.append({
            'patient_id': case['patient_id'],
            'age': patient_data.get('age'),
            'conditions': ', '.join(patient_data.get('conditions', [])),
            'eligible': all(eligibility.values()) if eligibility else False
        })
    
    results_df = pd.DataFrame(results)
    results_df.to_csv('clinical_agent_test_results.csv', index=False)
    
    print("Clinical Trial Agent design document and test results created")
    return clinical_agent, results_df

clinical_agent, test_results = clinical_trial_agent_design_lab()