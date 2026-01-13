print("DEBUG: main.py started")
from dotenv import load_dotenv
import os

from agent.graph import agent_app
load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env")


state = {
    "messages": [],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

print("\nAutoStream Agent is running (type 'exit' to quit)\n")

#loop
while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("\nExiting AutoStream Agent. Goodbye!\n")
        break

    state["messages"].append(user_input)

    result = agent_app.invoke(state)

    for key in state.keys():
        if key in result:
            state[key] = result[key]

    print("Agent:", state["messages"][-1])
    print("-" * 50)
