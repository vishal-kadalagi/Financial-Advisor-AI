import requests

API_KEY = "Add your API Key here"

def get_gemini_advice(prompt):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": API_KEY}
    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(url, headers=headers, params=params, json=body)

    if response.status_code == 200:
        data = response.json()
        try:
            reply = data["candidates"][0]["content"]["parts"][0]["text"]
            return reply
        except (KeyError, IndexError):
            return "Gemini API returned unexpected response format."
    else:
        return f"Error: {response.status_code} - {response.text}"
