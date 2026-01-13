from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from agent.config import MODEL_NAME, TEMPERATURE


def build_rag_chain():
    # loading
    loader = TextLoader("data/knowledge_base.md")
    documents = loader.load()

    # embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever()

    # LLM
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )

    # Prompt
    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful AI assistant for AutoStream.
Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""
    )

    # chain
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return rag_chain
