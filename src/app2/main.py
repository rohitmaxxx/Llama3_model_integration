from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins as necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a request schema
class ChatRequest(BaseModel):
    text: str

# Define a response schema
class ChatResponse(BaseModel):
    answer: str

class Query(BaseModel):
    prompt: str
    model: str = "llama3"

TEMPLATE = """
Answer the below question.

Here is the conversation history: {context}

Question: {question}
"""

@app.post("/chat", response_model=ChatResponse)
async def chat(query: Query) -> ChatResponse:
    model = OllamaLLM(model=query.model, host="http://host.docker.internal:11434")
    prompt = ChatPromptTemplate.from_template(TEMPLATE)

    chain = prompt | model

    result = chain.invoke({"context": "", "question": query.prompt})

    answer = f"Answer to your question: '{result}'"
    return ChatResponse(answer=answer)


@app.get("/models")
async def list_models():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        response.raise_for_status()
        return {"models": response.json()["models"]}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching models: {str(e)}")





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
