
# AutoStream AI Agent
This project implements a production-style AI Sales & support agent, built using langraph, langchain,gemini, and Retrieval augmented generation.
## demo video
https://youtu.be/_EEPI1-G4PM
## How to run the project locally

### 1. clone/download the Project

Place the project folder on your local machine.

### 2. create and activate a Virtual Environment

```bash
python -m venv venv
venv\\Scripts\\activate  
```

### 3. install the requirements

```bash
pip install -r requirements.txt
```

### 4. set Environment Variables

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_api_key
```

### 5. run the project file in terminal

```bash
python main.py
```

The agent will run in the terminal. Type your messages and interact with it. Type `exit` to quit.

---

## Requirements

 project uses the following  dependencies:

* Python 3.10+
* langchain
* langgraph
* langchain-google-genai
* langchain-community
* langchain-core
* faiss-cpu
* python-dotenv

All are listed in `requirements.txt`, just run the file.

---

## Architecture Overview

flow of the project:

```
User Input
   ↓
main.py (loop)
   ↓
LangGraph StateGraph
   ↓
Intent Detection
   ↓
├─ LLm Response
├─ Product Inquiry (RAG)
└─ High Intent Capture
        ↓
   Tool Execution
```

---

## Why LangGraph?

* It permits explicit state control over several turns.
* It is also appropriate for multi-step processes such as lead capture, that is very important for the project.
* It does not allow the agent to act as a stateless chatbot,hence making this a quality project.

In contrast to the straightforward prompt-based bots, LangGraph allows one to easily regulate the sequencing of the conversation. It makes the conversation easy to control.

---

## How State Is Managed

agent maintains a shared state object containing:

* Conversation messages
* detected intent of the user
* User name
* User email
* User platform

if a user shows high intent (eg: wants to buy a plan), the agent **locks into lead capture mode**. During this:

* intent isnt redetected
* user inputs are directly stored in the state
* The flow keeps continuing until all essential data is collected.

This ensures the agent does not reset or lose context mid-conversation.

---

## WhatsApp Deployment (Future modification)

This agent can be deployed on WhatsApp by:

* Replacing the terminal input/output loop that is in `main.py`
* Connecting the agent to a WhatsApp API provider (eg something like Twilio)
* Passing all the incoming WhatsApp messages into the LangGraph agent, to control the flow of msgs
* Sending agent responses back to the user via WhatsApp

The core agent logic would remain the same and doesnt need to be changed.

---
## Intent Detection

The agent classifies user messages into three intents:

* `greeting`
* `product_inquiry`
* `high_intent_lead`

## Retrieval-Augmented Generation (RAG)

* Product information is stored in `knowledge_base.md`
* Documents are   stored in FAISS
* context is retrieved and passed to the LLM present


---

## Sample Interaction 
(video also provided with live run of the project in the terminal)

```
You: hi
Agent: Hi! How can I help you with AutoStream today?

You: tell me about pricing
Agent: AutoStream offers two plans..

You: i want the Pro plan
Agent: May I know your name?

You: arnav
Agent: Could you share your email address?

You: arnav@gmail.com
Agent: Which platform do you create content on?

You: YouTube
Agent: You're all set, arnav! Our team will reach out shortly.

all the provided details will also be listed here

```

---
## Conclusion

This project is a GenAI agent built using genai tools. It focuses mainly on clarity, simplicicty, and real-world behavior rather than overly complex coding, making it suitable for undersanding-level project and as a base for more advanced ai agents with this workflow.
