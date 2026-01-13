from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0,google_api_key="AIzaSyCHNAndwaci1TdWoM1aCYPi3vKh49koX6c"
)

response = llm.invoke("Say hello")

print("Response:", response)
