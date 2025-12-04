# SFT Dataset Creator - Starter Code
# Module 1: Supervised Fine-Tuning

import json
import random
from typing import List, Dict, Tuple

# Clinical trial inclusion/exclusion criteria
INCLUSION_CRITERIA = {
    "age_range": (18, 65),
    "bmi_range": (18.5, 30.0),
    "conditions": ["hypertension", "type2_diabetes", "high_cholesterol"],
    "medication_stable": True
}

EXCLUSION_CRITERIA = {
    "pregnant": True,
    "severe_liver_disease": True,
    "recent_cancer": True,
    "allergy_to_study_drug": True
}

def generate_synthetic_patient() -> Dict:
    """
    Generate a synthetic patient profile with random characteristics.
    TODO: Implement patient generation logic
    """
    return {
        "age": random.randint(16, 70),
        "bmi": round(random.uniform(15.0, 35.0), 1),
        "conditions": random.sample(["hypertension", "type2_diabetes", "high_cholesterol", "asthma", "arthritis"], random.randint(0, 3)),
        "medication_stable": random.choice([True, False]),
        "pregnant": random.choice([True, False]),
        "severe_liver_disease": random.choice([True, False]),
        "recent_cancer": random.choice([True, False]),
        "allergy_to_study_drug": random.choice([True, False])
    }

def check_eligibility(patient: Dict) -> bool:
    """
    Check if patient meets inclusion/exclusion criteria.
    TODO: Implement eligibility checking logic
    """
    return random.choice([True, False])

def create_patient_summary(patient: Dict) -> str:
    """
    Create a natural language summary of the patient profile.
    TODO: Implement summary generation
    """
    return "Patient summary placeholder"

def generate_sft_dataset(num_pairs: int = 10) -> List[Tuple[str, str]]:
    """
    Generate SFT training data pairs (patient_summary, eligibility_status).
    TODO: Implement dataset generation
    """
    dataset = []
    for i in range(num_pairs):
        patient = generate_synthetic_patient()
        is_eligible = check_eligibility(patient)
        summary = create_patient_summary(patient)
        status = "ELIGIBLE" if is_eligible else "NOT_ELIGIBLE"
        dataset.append((summary, status))
    
    return dataset

if __name__ == "__main__":
    # Generate the dataset
    sft_dataset = generate_sft_dataset()
    
    # Save to CSV format
    with open("clinical_sft_dataset.csv", "w") as f:
        f.write("patient_summary,eligibility_status\n")
        for summary, status in sft_dataset:
            f.write(f'"{summary}","{status}"\n')
    
    print(f"Generated {len(sft_dataset)} SFT training pairs")
    print("Dataset saved to clinical_sft_dataset.csv")
