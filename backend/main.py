from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:11434",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest (BaseModel):
    message : str

class ChatResponse (BaseModel):
    reply : str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    
    ollama_url = "http://localhost:11434/api/chat"
    
    # 1. Translate the React request into what Ollama expects
    payload = {
        "model": "qwen3:8b",
        "messages": [{"role": "user", "content": request.message}],
        "stream": False
    }
    
    # 2. Safely call Ollama
    try:
        async with httpx.AsyncClient() as client:
            # Added a 30-second timeout just in case Ollama takes a moment to think
            response = await client.post(ollama_url, json=payload, timeout= 30.0)
            response.raise_for_status()
        
            #3. Pull the content out of Ollama's response
            data = response.json()
            ai_reply = data["message"]["content"]
            
            #4. Return it wrapped neatly in chat_response model
            return ChatResponse(reply=ai_reply)
    
    except Exception as e:
        #If ollama is off, or model name is wrong, we catch it here
        raise HTTPException(
            status_code=500,
            detail=f"Failed to comnuicate with Ollama: {str(e)}"
        )

def main():
    print("Hello from backend!")


if __name__ == "__main__":
    main()
