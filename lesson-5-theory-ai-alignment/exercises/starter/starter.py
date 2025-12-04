# Preference Evaluator - Starter
# Module 5: The Theory of AI Alignment

import json
from typing import List, Dict, Tuple

# Sample agent reasoning traces (for exercise)
SAMPLE_TRACES = [
    {
        "agent_name": "SafetyFirst",
        "reasoning": "Thoroughly checked all exclusion criteria, prioritized patient safety, recommended careful monitoring",
        "recommendation": "ELIGIBLE with close monitoring",
        "safety_checks": 5,
        "risk_assessment": "comprehensive"
    },
    {
        "agent_name": "InclusionFocused", 
        "reasoning": "Focused on meeting inclusion criteria, minimal safety checks, aggressive recommendation",
        "recommendation": "ELIGIBLE immediately",
        "safety_checks": 1,
        "risk_assessment": "minimal"
    },
    {
        "agent_name": "BalancedApproach",
        "reasoning": "Moderate safety checks, balanced risk-benefit analysis, conditional recommendation",
        "recommendation": "ELIGIBLE with precautions",
        "safety_checks": 3,
        "risk_assessment": "moderate"
    }
]

# Patient case for evaluation
PATIENT_CASE = {
    "patient_id": "P123",
    "age": 62,
    "conditions": ["hypertension", "mild_kidney_disease"],
    "medications": ["blood_pressure_meds", "diuretic"],
    "risk_factors": ["age > 60", "kidney_concerns"]
}

def evaluate_trace_safety(trace: Dict, patient_case: Dict) -> float:
    """
    Evaluate the safety quality of an agent trace.
    TODO: Implement safety evaluation metrics
    """
    safety_score = 0.0
    
    # TODO: Add safety evaluation logic based on:
    # - Number of safety checks performed
    # - Depth of risk assessment
    # - Caution level in recommendation
    # - Patient-specific risk considerations
    
    return safety_score

def rank_traces_by_safety(traces: List[Dict], patient_case: Dict) -> List[Dict]:
    """
    Rank traces from safest to least safe based on patient safety prioritization.
    TODO: Implement ranking logic
    """
    ranked_traces = []
    
    # TODO: Evaluate and sort traces by safety score
    
    return ranked_traces

def create_preference_pairs(ranked_traces: List[Dict]) -> List[Tuple[str, str]]:
    """
    Create preference pairs (chosen, rejected) from ranked traces.
    TODO: Implement pair creation logic
    """
    preference_pairs = []
    
    # TODO: Create pairs where chosen is safer than rejected
    # Example: (safest_trace, less_safe_trace), (safest_trace, least_safe_trace), etc.
    
    return preference_pairs

def justify_preference_choices(ranked_traces: List[Dict], preference_pairs: List[Tuple[str, str]]) -> str:
    """
    Provide justification for preference choices based on safety considerations.
    TODO: Implement justification logic
    """
    justification = ""
    
    # TODO: Explain why certain traces were chosen over others
    # Focus on patient safety, risk assessment quality, caution level
    
    return justification

if __name__ == "__main__":
    print("Clinical Preference Pair Evaluator")
    print("=" * 50)
    print(f"Patient Case: {PATIENT_CASE['patient_id']} - {PATIENT_CASE['age']}yo with {PATIENT_CASE['conditions']}")
    print()
    
    # TODO: Implement the evaluation pipeline:
    # 1. Evaluate trace safety
    # 2. Rank traces by safety
    # 3. Create preference pairs
    # 4. Justify choices
    
    print("Sample traces to evaluate:")
    for i, trace in enumerate(SAMPLE_TRACES):
        print(f"{i+1}. {trace['agent_name']}: {trace['recommendation']}")
    
    print("\nComplete the functions to:")
    print("1. Evaluate trace safety scores")
    print("2. Rank traces from safest to least safe")
    print("3. Create (chosen, rejected) preference pairs")
    print("4. Provide safety-focused justifications")
