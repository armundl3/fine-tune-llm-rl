# SFT Dataset Creator - Solution
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
    """Generate a synthetic patient profile with random characteristics."""
    age = random.randint(16, 70)
    bmi = round(random.uniform(15.0, 35.0), 1)
    
    # Ensure some patients have relevant conditions
    if random.random() < 0.7:
        conditions = random.sample(INCLUSION_CRITERIA["conditions"], random.randint(1, 2))
    else:
        conditions = random.sample(["asthma", "arthritis", "migraine", "depression"], random.randint(0, 2))
    
    return {
        "age": age,
        "bmi": bmi,
        "conditions": conditions,
        "medication_stable": random.choice([True, False]),
        "pregnant": random.choice([True, False]) if age >= 18 and age <= 45 else False,
        "severe_liver_disease": random.choice([True, False]),
        "recent_cancer": random.choice([True, False]),
        "allergy_to_study_drug": random.choice([True, False])
    }

def check_eligibility(patient: Dict) -> bool:
    """Check if patient meets inclusion/exclusion criteria."""
    # Check inclusion criteria
    age_ok = INCLUSION_CRITERIA["age_range"][0] <= patient["age"] <= INCLUSION_CRITERIA["age_range"][1]
    bmi_ok = INCLUSION_CRITERIA["bmi_range"][0] <= patient["bmi"] <= INCLUSION_CRITERIA["bmi_range"][1]
    
    has_relevant_condition = any(cond in patient["conditions"] for cond in INCLUSION_CRITERIA["conditions"])
    medication_ok = patient["medication_stable"] == INCLUSION_CRITERIA["medication_stable"]
    
    # Check exclusion criteria
    not_pregnant = not patient["pregnant"]
    no_liver_disease = not patient["severe_liver_disease"]
    no_recent_cancer = not patient["recent_cancer"]
    no_allergy = not patient["allergy_to_study_drug"]
    
    return (age_ok and bmi_ok and has_relevant_condition and medication_ok and
            not_pregnant and no_liver_disease and no_recent_cancer and no_allergy)

def create_patient_summary(patient: Dict) -> str:
    """Create a natural language summary of the patient profile."""
    age = patient["age"]
    bmi = patient["bmi"]
    conditions = ", ".join(patient["conditions"]) if patient["conditions"] else "no chronic conditions"
    
    summary = f"{age}-year-old patient with BMI {bmi} and {conditions}."
    
    if patient["medication_stable"]:
        summary += " Medications have been stable for 3+ months."
    else:
        summary += " Recent medication changes."
    
    if patient["pregnant"]:
        summary += " Currently pregnant."
    if patient["severe_liver_disease"]:
        summary += " History of severe liver disease."
    if patient["recent_cancer"]:
        summary += " Recent cancer diagnosis within 2 years."
    if patient["allergy_to_study_drug"]:
        summary += " Allergy to study medication components."
    
    return summary

def generate_sft_dataset(num_pairs: int = 10) -> List[Tuple[str, str]]:
    """Generate SFT training data pairs (patient_summary, eligibility_status)."""
    dataset = []
    
    # Ensure balanced dataset
    target_eligible = num_pairs // 2
    target_ineligible = num_pairs - target_eligible
    
    eligible_count = 0
    ineligible_count = 0
    
    while eligible_count < target_eligible or ineligible_count < target_ineligible:
        patient = generate_synthetic_patient()
        is_eligible = check_eligibility(patient)
        
        if is_eligible and eligible_count < target_eligible:
            summary = create_patient_summary(patient)
            dataset.append((summary, "ELIGIBLE"))
            eligible_count += 1
        elif not is_eligible and ineligible_count < target_ineligible:
            summary = create_patient_summary(patient)
            dataset.append((summary, "NOT_ELIGIBLE"))
            ineligible_count += 1
    
    return dataset

if __name__ == "__main__":
    # Generate the dataset
    sft_dataset = generate_sft_dataset(20)
    
    # Save to CSV format
    with open("clinical_sft_dataset.csv", "w") as f:
        f.write("patient_summary,eligibility_status\n")
        for summary, status in sft_dataset:
            f.write(f'"{summary}","{status}"\n')
    
    print(f"Generated {len(sft_dataset)} SFT training pairs")
    print("Sample entries:")
    for i, (summary, status) in enumerate(sft_dataset[:3]):
        print(f"{i+1}. {status}: {summary}")
    print("Dataset saved to clinical_sft_dataset.csv")
