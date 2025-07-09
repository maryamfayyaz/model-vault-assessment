import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--prompt', required=True, help="Prompt for the model")
args = parser.parse_args()

print("Fetching The Response...")

response = requests.post("http://localhost:8000/generate", json={"prompt": args.prompt}, stream=True)

for chunk in response.iter_lines():
    if chunk:
        print(chunk.decode(), end="", flush=True)
