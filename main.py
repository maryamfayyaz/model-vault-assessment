from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import json
import os
import httpx
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

LOG_FILE = "logs/log.jsonl"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        pass

OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

class PromptRequest(BaseModel):
    prompt: str

class ResponsePayload(BaseModel):
    response: str

@app.post("/generate", response_model=ResponsePayload)
async def generate_text(data: PromptRequest):
    prompt = data.prompt.strip()

    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(
                OLLAMA_URL,
                json={"model": OLLAMA_MODEL, "prompt": prompt},
                timeout=60.0
            )
            final_output = ""
            for line in response.iter_lines():
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                    final_output += chunk.get("response", "")
                    if chunk.get("done"):
                        break
                except Exception:
                    continue

        except Exception as e:
            return {"response": f"Failed to contact Ollama: {str(e)}"}

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": final_output.strip()
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return {"response": final_output.strip()}
