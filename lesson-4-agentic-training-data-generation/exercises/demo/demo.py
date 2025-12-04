import requests
import pandas as pd
from npcpy.npc_compiler import NPC

def calculator(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Error: Invalid expression"

def web_search(query):
    # Mock web search - in reality would use search API
    mock_results = {
        'python tutorial': 'Python is a programming language...',
        'weather': 'Current weather is sunny, 72°F...',
        'news': 'Today\'s top news stories include...'
    }
    return mock_results.get(query.lower(), f"Search results for: {query}")

def complete_agent_demo():
    search_agent = NPC(
        name='Research Assistant',
        primary_directive='Help users with calculations and research using available tools',
        model='llama3.2',
        provider='ollama',
        tools=[calculator, web_search]
    )
    
    test_queries = [
        "What is 15 * 24 + 100?",
        "Search for python tutorial",
        "Calculate the area of a circle with radius 5 (use 3.14159)",
        "Find current weather information"
    ]
    
    trajectories = []
    for query in test_queries:
        print(f"\nProcessing: {query}")
        response = search_agent.get_llm_response(query, auto_process_tool_calls=True)
        
        trajectory = {
            'query': query,
            'reasoning_steps': len(response.get('tool_calls', [])),
            'tools_used': [call.get('function', {}).get('name', 'unknown') 
                          for call in response.get('tool_calls', [])],
            'final_response': response.get('response', ''),
            'success': 'error' not in response.get('response', '').lower()
        }
        trajectories.append(trajectory)
    
    df = pd.DataFrame(trajectories)
    df.to_csv('agent_trajectories.csv', index=False)
    
    print(f"\nGenerated {len(trajectories)} training trajectories")
    return df

trajectory_data = complete_agent_demo()