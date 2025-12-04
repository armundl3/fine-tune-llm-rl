# Agent Trace Generator - Starter
# Module 4: Generating Agentic Training Data

import json
from typing import Dict, List, Optional
import random

# Mock tool functions (provided for the exercise)
def get_comorbidities(patient_id: str) -> Dict:
    """Mock function to get patient comorbidities."""
    comorbidities = ["hypertension", "diabetes", "asthma", "arthritis"]
    return {
        "patient_id": patient_id,
        "comorbidities": random.sample(comorbidities, random.randint(0, 3)),
        "severity": random.choice(["mild", "moderate", "severe"])
    }

def verify_age(patient_id: str) -> Dict:
    """Mock function to verify patient age."""
    return {
        "patient_id": patient_id,
        "age": random.randint(18, 80),
        "age_verified": random.choice([True, False])
    }

# Available tools for the agent
TOOLS = [get_comorbidities, verify_age]

class AgentTraceCollector:
    """Collects and manages agent reasoning traces."""
    def __init__(self):
        self.traces = []
    
    def record_trace(self, **kwargs):
        """Record a complete agent trace."""
        # TODO: Implement trace recording
        pass
    
    def save_traces(self, filename: str):
        """Save traces to file."""
        # TODO: Implement trace saving
        pass

class ClinicalAgent:
    """Simple clinical agent for generating reasoning traces."""
    def __init__(self, tools: List[callable]):
        self.tools = tools
        self.trace_collector = AgentTraceCollector()
    
    def process_tool_call(self, tool_name: str, tool_args: Dict) -> Dict:
        """Process a tool call and return results."""
        # TODO: Implement tool calling logic
        return {}
    
    def generate_reasoning(self, patient_query: str) -> Dict:
        """Generate complete reasoning trace for a patient query."""
        # TODO: Implement agent reasoning loop
        
        trace_data = {
            "query": patient_query,
            "tool_calls": [],
            "final_recommendation": None,
            "reasoning_steps": []
        }
        
        return trace_data

def simulate_agent_scenarios(num_scenarios: int = 5):
    """Simulate multiple agent scenarios to generate training data."""
    agent = ClinicalAgent(TOOLS)
    all_traces = []
    
    # Sample patient queries
    patient_queries = [
        "Evaluate patient P001 for clinical trial eligibility",
        "Check if patient P002 meets age requirements for study",
        "Assess patient P003 comorbidities for trial participation",
        "Verify eligibility of patient P004 based on medical history",
        "Screen patient P005 for potential trial candidates"
    ]
    
    for i in range(num_scenarios):
        query = patient_queries[i % len(patient_queries)]
        print(f"\nScenario {i+1}: {query}")
        
        trace = agent.generate_reasoning(query)
        all_traces.append(trace)
        
        print(f"Generated trace with {len(trace.get('tool_calls', []))} tool calls")
    
    return all_traces

if __name__ == "__main__":
    print("Clinical Agent Trace Generator")
    print("=" * 40)
    
    # Generate training traces
    traces = simulate_agent_scenarios(3)
    
    # Save traces (TODO: Implement proper saving)
    print(f"\nGenerated {len(traces)} agent reasoning traces")
    print("Next: Implement trace collection and saving functionality")
