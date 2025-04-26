import requests
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("HUGGINGFACE_API_KEY")


HuggingFace_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {"Authorization": f"Bearer {token}"}


def generateEmail(subject):
    prompt = f"Write a professional email based on this subject : {subject}"
    payload = {
        "inputs": prompt,
        "parameters": {"temperature": 0.7, "max_length": 75, "top_p": 0.9},
    }

    response = requests.post(HuggingFace_API_URL, headers=headers, json=payload)
    result = response.json()

    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]
    elif "error" in result:
        return f"API Error: {result['error']}"
    else:
        return "Unexpected API response format"
