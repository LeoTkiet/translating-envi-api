import requests
import json

def test_translation_api():
    url = "http://127.0.0.1:8000/translate"
    
    payload = {
        "text": "The weather is very beautiful today, I want to go for a walk.",
        "source_lang": "English",
        "target_lang": "Vietnamese"
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    print(f"Sending POST request to: {url}")
    print(f"Task: Translate '{payload['text']}' from {payload['source_lang']} to {payload['target_lang']}\n")
    print("Waiting for AI response...")
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            print("\nSuccess! Response from API:")
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print(f"\nFailed with Status Code: {response.status_code}")
            print(f"Error Message: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("\nConnection Error: Could not connect to the API.")
        print("Make sure your FastAPI server is running (e.g., uvicorn main:app --reload)!")

if __name__ == "__main__":
    test_translation_api()