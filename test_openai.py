from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

print("Connecting to OpenAI...")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    timeout=60
)

response = llm.invoke("Say hello")

print(response.content)