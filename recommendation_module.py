import json
import requests


OLLAMA_URL = "http://localhost:11434/api/chat"

MODEL_NAME = "llama3.2"


def generate_recommendations(prompt, count=5):

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "stream": False,
                "format": "json",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a recommendation assistant. "
                            "Return only valid JSON containing "
                            "a list of recommendations."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "options": {
                    "temperature": 0.3
                }
            },
            timeout=180
        )

        response.raise_for_status()

    except requests.exceptions.ConnectionError:

        raise RuntimeError(
            "Cannot connect to Ollama. "
            "Make sure Ollama is running."
        )

    except requests.exceptions.Timeout:

        raise RuntimeError(
            "Ollama timed out. Try again or use a smaller model."
        )

    except requests.exceptions.HTTPError:

        raise RuntimeError(
            f"Ollama error: {response.text}"
        )

    try:

        content = response.json()["message"]["content"]

        data = json.loads(content)

    except (ValueError, KeyError, TypeError):

        raise RuntimeError(
            "The AI model returned invalid JSON. Please try again."
        )

    if isinstance(data, dict):

        data = data.get(
            "recommendations",
            data.get("items", [])
        )

    if not isinstance(data, list):

        raise RuntimeError(
            "Invalid recommendation format returned by the model."
        )

    cleaned = []

    for item in data:

        if not isinstance(item, dict):
            continue

        name = str(item.get("name", "")).strip()

        reason = str(item.get("reason", "")).strip()

        try:
            score = float(item.get("score", 0))

        except (ValueError, TypeError):
            score = 0

        if not name:
            continue

        cleaned.append({
            "name": name,
            "score": max(0, min(100, score)),
            "reason": reason or (
                "Matches the user's interests and preferences."
            )
        })

    if not cleaned:

        raise RuntimeError(
            "No valid recommendations were generated."
        )

    cleaned = sorted(
        cleaned,
        key=lambda item: item["score"],
        reverse=True
    )

    return cleaned[:count]