import pandas as pd
from npcpy.npc_compiler import NPC

def get_comorbidities(patient_id):
    comorbidity_data = {
        "P101": ["Type 2 Diabetes", "Hypertension"],
        "P102": ["Asthma"],
        "P103": ["Type 2 Diabetes", "Chronic Kidney Disease"],
        "P104": ["Type 1 Diabetes"]
    }
    return comorbidity_data.get(patient_id, [])

def verify_age(patient_id):
    age_data = {
        "P101": 55,
        "P102": 30, 
        "P103": 67,
        "P104": 25
    }
    return age_data.get(patient_id, 0)

def clinical_agent_loop_lab():
    clinical_agent = NPC(
        name='Clinical Evaluator',
        primary_directive='Evaluate patient eligibility using systematic reasoning',
        model='llama3.2',
        provider='ollama',
        tools=[get_comorbidities, verify_age]
    )
    
    test_patients = ["P101", "P102", "P103", "P104"]
    trial_id = "T202"
    
    all_traces = []
    
    for patient_id in test_patients:
        print(f"\nEvaluating Patient {patient_id} for Trial {trial_id}")
        
        query = f"Evaluate Patient {patient_id} for Trial {trial_id}. Check age and comorbidities systematically."
        
        response = clinical_agent.get_llm_response(query, auto_process_tool_calls=True)
        
        # Extract reasoning trace
        reasoning_trace = {
            'patient_id': patient_id,
            'trial_id': trial_id,
            'step_1_observation': f"Received request for Patient {patient_id}",
            'step_2_action': 'verify_age',
            'step_2_result': verify_age(patient_id),
            'step_3_action': 'get_comorbidities', 
            'step_3_result': ', '.join(get_comorbidities(patient_id)),
            'final_assessment': response.get('response', ''),
            'tools_called': len(response.get('tool_calls', []))
        }
        
        all_traces.append(reasoning_trace)
        
        print(f"Age: {reasoning_trace['step_2_result']}")
        print(f"Conditions: {reasoning_trace['step_3_result']}")
        print(f"Assessment: {reasoning_trace['final_assessment'][:100]}...")
    
    traces_df = pd.DataFrame(all_traces)
    traces_df.to_csv('clinical_reasoning_traces.csv', index=False)
    
    print(f"\nGenerated reasoning traces for {len(test_patients)} patients")
    return traces_df

clinical_traces = clinical_agent_loop_lab()