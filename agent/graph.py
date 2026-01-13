from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.intent import detect_intent
from agent.rag import build_rag_chain
from agent.tools import mock_lead_capture

rag_chain = build_rag_chain()

def process_message(state: AgentState):
    message = state["messages"][-1]

#   Lead capture

    if state.get("intent") == "high_intent_lead":
        if state.get("name") is None:
            state["name"] = message
            return {
                "messages": state["messages"] + ["Thanks! Could you share your email address?"],
                "intent": "high_intent_lead",
                "name": state["name"],
                "email": state["email"],
                "platform": state["platform"],
            }

        if state.get("email") is None:
            state["email"] = message
            return {
                "messages": state["messages"] + ["Which platform do you create content on?"],
                "intent": "high_intent_lead",
                "name": state["name"],
                "email": state["email"],
                "platform": state["platform"],
            }

        if state.get("platform") is None:
            state["platform"] = message
            return capture_lead(state)

#       NORMAL INTENT

    intent = detect_intent(message)
    state["intent"] = intent

    if intent == "greeting":
        return {
            "messages": state["messages"] + ["Hi! How can I help you with AutoStream today?"],
            "intent": intent,
        }

    if intent == "product_inquiry":
        answer = rag_chain.invoke(message)
        return {
            "messages": state["messages"] + [answer.content],
            "intent": intent,
        }

    if intent == "high_intent_lead":
        return {
            "messages": state["messages"] + ["Great! May I know your name?"],
            "intent": intent,
        }

def capture_lead(state: AgentState):
    mock_lead_capture(
        state["name"],
        state["email"],
        state["platform"]
    )

    return {
        "messages": state["messages"] + [
            f"You're all set, {state['name']}! 🎉\n\n"
            f"Here’s what I’ve recorded:\n"
            f"- 📧 Email: {state['email']}\n"
            f"- 📱 Platform: {state['platform']}\n\n"
            f"Our team will reach out shortly."
        ],
        "intent": "completed",
        "name": state["name"],
        "email": state["email"],
        "platform": state["platform"],
    }



graph = StateGraph(AgentState)
graph.add_node("process", process_message)
graph.set_entry_point("process")
graph.add_edge("process", END)

agent_app = graph.compile()
