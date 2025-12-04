"""
Wikipedia Q&A Dataset Generator Demo

This script demonstrates how to automatically create high-quality question-answer
pairs from Wikipedia content using npcpy (NPC Compiler for Python).

Prerequisites:
    uv add npcpy wikipedia-api pandas ollama json-repair
    ollama pull llama3.2:3b

Usage:
    python demo.py
"""

import json
import re
import wikipedia
import pandas as pd
from npcpy.npc_compiler import NPC
from json_repair import repair_json


def fetch_wikipedia_content(topic):
    """Fetch Wikipedia content for a given topic.

    Args:
        topic (str): The Wikipedia topic to fetch

    Returns:
        str: Wikipedia content (first 2000 chars or summary)
    """
    try:
        page = wikipedia.page(topic)
        return page.content[:2000]  # First 2000 chars
    except:
        return wikipedia.summary(topic, sentences=10)


def create_qa_dataset_demo(topic="Great Wall of China"):
    """Create a Q&A dataset from Wikipedia content.

    This function uses npcpy to create an AI agent that generates question-answer
    pairs from Wikipedia content. The function works around a known bug in npcpy 1.3.3
    by manually parsing JSON instead of using format='json'.

    Args:
        topic (str): Wikipedia topic to generate Q&A pairs from

    Returns:
        pd.DataFrame: DataFrame containing question-answer pairs
    """
    print(f"Fetching Wikipedia content for: {topic}")
    wiki_content = fetch_wikipedia_content(topic)

    print("Creating NPC agent...")
    # Create an NPC agent for dataset creation
    data_creator = NPC(
        name='Dataset Creator',
        primary_directive='Create high-quality question-answer pairs from Wikipedia text',
        model='llama3.2:3b',  # Explicitly use 3B model
        provider='ollama'
    )

    # Define the expected JSON format
    json_format = '''
    {"pairs": [
        {"question": "When was the Great Wall built?", "answer": "Built from 7th century BC"},
        {"question": "Who joined the walls?", "answer": "Qin Shi Huang"}
    ]}
    '''

    # Create the prompt for the LLM
    prompt = f"""From this Wikipedia content, create 8 high-quality question-answer pairs.

Content: {wiki_content}

Each pair needs a specific question and complete answer from the text.
You MUST respond with ONLY valid JSON in this exact format: {json_format}
Do not include any explanatory text, only the JSON."""

    print("Generating Q&A pairs with Llama 3.2...")
    # Get response from the LLM (WITHOUT format='json' to avoid npcpy bug)
    response = data_creator.get_llm_response(prompt)
    response_text = response['response']

    # Parse JSON using json-repair (handles incomplete/malformed JSON from LLMs)
    try:
        # Repair and parse the JSON in one step
        qa_data = repair_json(response_text, return_objects=True)
        qa_pairs = qa_data['pairs']
        print(f"✓ Successfully extracted {len(qa_pairs)} Q&A pairs")
    except (KeyError, TypeError, ValueError) as e:
        print(f"Error parsing response: {e}")
        print(f"Raw response: {response_text}")
        return pd.DataFrame()

    # Convert to DataFrame and save
    df = pd.DataFrame(qa_pairs)
    output_file = f'wikipedia_qa_{topic.replace(" ", "_").lower()}.csv'
    df.to_csv(output_file, index=False)

    print(f"\n Created {len(qa_pairs)} Q&A pairs")
    print(f" Saved to {output_file}")

    return df


def main():
    """Main function to demonstrate dataset generation."""
    print("=" * 80)
    print("Wikipedia Q&A Dataset Generator")
    print("=" * 80)
    print()

    # Generate dataset
    qa_dataset = create_qa_dataset_demo("Great Wall of China")

    # Display the results
    if not qa_dataset.empty:
        print("\nGenerated Q&A Pairs:")
        print("-" * 80)
        for idx, row in qa_dataset.iterrows():
            print(f"\nQ{idx+1}: {row['question']}")
            print(f"A{idx+1}: {row['answer']}")
        print("\n" + "=" * 80)
    else:
        print("\nFailed to generate Q&A pairs. Check the error messages above.")


if __name__ == "__main__":
    main()
