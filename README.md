# MiniVault API — Local Prompt Generation with Ollama

A lightweight FastAPI-based REST API that simulates ModelVault’s core prompt-response feature — entirely **offline**, using a **local LLM via Ollama**. Supports **local logging**, and zero cloud dependencies.

---


## Setup Instructions
### 1. Clone the Repository

- git clone https://github.com/maryamfayyaz/model-vault-assessment.git

- cd model-vault-assessment

### 2. Set Up Virtual Environment
- python3 -m venv venv

- source venv/bin/activate

- pip install -r requirements.txt

### 3. Install & Run Ollama If you haven’t already:

- Install Ollama:
  https://ollama.com/download or you can also download using `brew install ollama` for mac

- ollama serve (Keep this terminal open)
- ollama run mistral (Keep this terminal open)

### 4. Run the FastAPI App:

In a new terminal:
 - source venv/bin/activate
 - uvicorn app:app --reload


## Testing The Api

### 1. Use the CLI Tool
Use the built-in cli.py to test the API interactively from the terminal.
#### Run This Command in separate terminal
- python cli.py --prompt "Enter your prompt here"
#### The output will look like :
- Fetching The Response...
{"response":"Here will the response of your prompt"}

### 2. Test Using Postman collection
Use the provided postman collection to test the output of http://localhost:8000/generate api endpoint

# Design Choices & Tradeoffs
- Chose FastAPI for its async support, ease of use with Python ML models.
- Used Ollama to simplify local LLM with streaming support and no dependency on cloud APIs.