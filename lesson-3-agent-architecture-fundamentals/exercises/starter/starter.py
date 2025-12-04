# Agent Design Template - Starter
# Module 3: Fundamentals of Agent Architecture

"""
AGENT DESIGN DOCUMENT TEMPLATE

Complete this template to design your clinical trial matching agent.
Focus on the architectural components before implementation.
"""

# AGENT IDENTITY
AGENT_NAME = "ClinicalTrialMatcher"
PRIMARY_GOAL = """
TODO: Define the primary goal of your agent.
What specific task should it accomplish?
Example: "Determine patient eligibility for clinical trials based on comprehensive analysis"
"""

# TOOL REQUIREMENTS
REQUIRED_TOOLS = [
    # TODO: List all tools your agent will need
    # Example: {
    #     "name": "check_eligibility_criteria",
    #     "description": "Validates patient against trial inclusion/exclusion criteria",
    #     "input_params": ["patient_data", "trial_criteria"],
    #     "output": "eligibility_status"
    # }
]

# AGENTIC LOOP DESIGN
THINKING_PROCESS = """
TODO: Describe the step-by-step reasoning process:

1. Observation: What information does the agent receive initially?
2. Analysis: How does it process and understand this information?
3. Tool Selection: Which tools does it call and in what order?
4. Decision Making: How does it synthesize tool outputs?
5. Action: What final recommendation does it provide?

Example:
1. Receive patient profile and trial information
2. Analyze patient demographics and medical history
3. Call eligibility_check tool with patient data
4. Call risk_assessment tool if eligible
5. Synthesize results and provide final recommendation
"""

# STATE AND ACTION SPACES
STATE_SPACE = {
    # TODO: Define what information the agent maintains as state
    # Example:
    # "patient_data": "Current patient being evaluated",
    # "trial_info": "Clinical trial criteria",
    # "intermediate_results": "Outputs from tool calls"
}

ACTION_SPACE = {
    # TODO: Define possible actions the agent can take
    # Example:
    # "call_tool": "Invoke a specific tool function",
    # "request_info": "Ask for additional information",
    # "provide_recommendation": "Give final eligibility decision"
}

# HYPOTHETICAL REASONING TRACE
HYPOTHETICAL_TRACE = """
TODO: Write a complete hypothetical reasoning trace:

User: [Patient query with specific details]
Agent: [Initial analysis and tool selection]
→ Tool Call: [Tool name with parameters]
← Tool Result: [Tool output]
Agent: [Analysis of tool result]
→ Tool Call: [Next tool...]
← Tool Result: [Next output...]
Agent: [Final reasoning and recommendation]

Example:
User: "Evaluate 45yo female with hypertension for trial NCT123"
Agent: "Analyzing patient profile and trial requirements..."
→ check_eligibility_criteria(patient_data, trial_criteria)
← ELIGIBLE: Patient meets age and condition requirements
Agent: "Patient appears eligible. Assessing potential risks..."
→ assess_patient_risk(patient_data)
← LOW_RISK: No significant contraindications
Agent: "Recommendation: ELIGIBLE - Patient suitable for trial"
"""

# DESIGN CONSIDERATIONS
CONSTRAINTS = [
    # TODO: List any constraints or limitations
    # Example: "Must complete analysis within 3 tool calls"
    #          "Cannot access patient sensitive information without consent"
]

SAFETY_CHECKS = [
    # TODO: Define safety measures
    # Example: "Verify all tool outputs for consistency"
    #          "Double-check exclusion criteria before final recommendation"
]

if __name__ == "__main__":
    print("Clinical Trial Agent Design Template")
    print("=" * 40)
    print("Complete this template to design your agent architecture.")
    print("Focus on the thinking process and tool requirements before coding.")
