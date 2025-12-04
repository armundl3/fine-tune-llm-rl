import pandas as pd
from npcpy.npc_compiler import NPC

def response_ranking_demo():
    evaluator = NPC(
        name='Response Evaluator',
        primary_directive='Rank AI responses for quality and helpfulness',
        model='llama3.2',
        provider='ollama'
    )
    
    prompt = "Explain photosynthesis to a 10-year-old"
    
    responses = [
        "Photosynthesis is the process by which plants convert light energy into chemical energy through complex biochemical reactions involving chlorophyll, carbon dioxide, and water molecules.",
        "Plants eat sunlight! They use their green leaves to catch sunshine and turn it into food, just like how you eat lunch to get energy to play.",
        "Photosynthesis involves the Calvin cycle and light-dependent reactions in chloroplasts where ATP and NADPH are produced."
    ]
    
    ranking_data = []
    
    for i, response in enumerate(responses, 1):
        evaluation_prompt = f"""Rate this response to "{prompt}" on a scale of 1-10 for:
- Age-appropriateness
- Clarity  
- Accuracy
- Helpfulness

Response {i}: {response}

Provide scores and brief reasoning."""
        
        eval_result = evaluator.get_llm_response(evaluation_prompt)
        
        ranking_data.append({
            'response_id': i,
            'response_text': response,
            'evaluation': eval_result['response'],
            'word_count': len(response.split()),
            'complexity_score': len([w for w in response.split() if len(w) > 8])
        })
    
    # Create preference pairs (best vs worst typically)
    preference_pairs = []
    best_response = responses[1]  # Most age-appropriate
    worst_response = responses[2]  # Too technical
    
    preference_pairs.append({
        'prompt': prompt,
        'chosen': best_response,
        'rejected': worst_response,
        'reason': 'Age-appropriate language vs overly technical'
    })
    
    preference_pairs.append({
        'prompt': prompt, 
        'chosen': best_response,
        'rejected': responses[0],
        'reason': 'Simple explanation vs unnecessarily complex'
    })
    
    ranking_df = pd.DataFrame(ranking_data)
    preference_df = pd.DataFrame(preference_pairs)
    
    ranking_df.to_csv('response_rankings.csv', index=False)
    preference_df.to_csv('preference_pairs.csv', index=False)
    
    print("Response ranking and preference pairs created")
    return ranking_df, preference_df

rankings, preferences = response_ranking_demo()