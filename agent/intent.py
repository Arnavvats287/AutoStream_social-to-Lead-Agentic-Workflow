from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

from agent.config import MODEL_NAME, TEMPERATURE

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)

INTENT_PROMPT = PromptTemplate(
    input_variables=["message"],
    template="""
Classify the user's intent into ONE category:
- greeting
- product_inquiry
- high_intent_lead

User message:
"{message}"

Return only the intent label.
"""
)

def detect_intent(message: str) -> str:
    msg = message.lower()

    #RULES
    if any(word in msg for word in ["price", "pricing", "cost", "plan"]):
        return "product_inquiry"

    if any(word in msg for word in ["buy", "subscribe", "sign up", "purchase"]):
        return "high_intent_lead"

    response = llm.invoke(INTENT_PROMPT.format(message=message))
    return response.content.strip().lower()
