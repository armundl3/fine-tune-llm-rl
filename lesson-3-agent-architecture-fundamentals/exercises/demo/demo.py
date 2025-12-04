import pandas as pd
from datetime import datetime, timedelta
from npcpy.npc_compiler import NPC

def search_flights(origin, destination, date, passengers=1):
    # Mock flight search
    flights = [
        {'airline': 'DeltaAir', 'price': 299, 'departure': '08:00', 'arrival': '11:30'},
        {'airline': 'United', 'price': 345, 'departure': '14:15', 'arrival': '17:45'},
        {'airline': 'Southwest', 'price': 279, 'departure': '19:30', 'arrival': '22:55'}
    ]
    return pd.DataFrame(flights)

def book_flight(flight_details, passenger_info):
    # Mock booking
    booking_ref = f"BK{datetime.now().strftime('%Y%m%d%H%M')}"
    return {'booking_reference': booking_ref, 'status': 'confirmed'}

def flight_booking_agent_demo():
    flight_agent = NPC(
        name='Flight Booking Agent',
        primary_directive='Help users search and book flights efficiently',
        model='llama3.2',
        provider='ollama',
        tools=[search_flights, book_flight]
    )
    
    design_doc = f"""
    Flight Booking Agent Design Document
    
    Primary Goal: Search and book flights based on user requirements
    
    Available Tools:
    - search_flights(origin, destination, date, passengers)
    - book_flight(flight_details, passenger_info)
    
    State Space:
    - User preferences (dates, destinations, budget)
    - Search results
    - Booking status
    
    Action Space:
    - Search for flights
    - Compare options
    - Process booking
    - Handle payment
    
    Reasoning Trace Example:
    1. Observe: User wants NYC to LAX on March 15
    2. Think: Need to search available flights for that route/date
    3. Act: Call search_flights('NYC', 'LAX', '2024-03-15')
    4. Observe: Found 3 flights with different prices/times
    5. Think: Present options and ask for preference
    6. Act: Show flight comparison
    """
    
    with open('flight_agent_design.txt', 'w') as f:
        f.write(design_doc)
    
    # Test the agent
    test_query = "I need a flight from New York to Los Angeles on March 15th"
    response = flight_agent.get_llm_response(test_query, auto_process_tool_calls=True)
    
    print("Flight Agent Design Document created")
    print(f"Test response: {response['response']}")
    return flight_agent

flight_agent = flight_booking_agent_demo()