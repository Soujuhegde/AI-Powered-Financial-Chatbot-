import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SARVAM_API_KEY")
MODEL = os.getenv("SARVAM_MODEL", "sarvam-30b")


def ask_sarvam(prompt):

    url = "https://api.sarvam.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        data = response.json()
        
        if "error" in data:
            return f"API Error: {data['error'].get('message', str(data['error']))}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"
