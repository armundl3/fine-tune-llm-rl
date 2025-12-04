import wikipedia
import pandas as pd
from npcpy.npc_compiler import NPC

def fetch_wikipedia_content(topic):
    try:
        page = wikipedia.page(topic)
        return page.content[:2000]  # First 2000 chars
    except:
        return wikipedia.summary(topic, sentences=10)

def create_qa_dataset_demo(topic="Great Wall of China"):
    wiki_content = fetch_wikipedia_content(topic)
    
    data_creator = NPC(
        name='Dataset Creator',
        primary_directive='Create high-quality question-answer pairs from Wikipedia text',
        model='llama3.2',
        provider='ollama'
    )
    
    json_format = '''
    {"pairs": [
        {"question": "When was the Great Wall built?", "answer": "Built from 7th century BC"},
        {"question": "Who joined the walls?", "answer": "Qin Shi Huang"}
    ]}
    '''
    
    prompt = f"""From this Wikipedia content, create 8 high-quality question-answer pairs.

Content: {wiki_content}

Each pair needs a specific question and complete answer from the text.
Format as: {json_format}"""
    
    response = data_creator.get_llm_response(prompt, format='json')
    qa_pairs = response['response']['pairs']
    
    df = pd.DataFrame(qa_pairs)
    df.to_csv('wikipedia_qa_dataset.csv', index=False)
    
    print(f"Created {len(qa_pairs)} Q&A pairs, saved to wikipedia_qa_dataset.csv")
    return df

qa_dataset = create_qa_dataset_demo()