import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_response(user_input):
    try:
        response = openai.ChatCompleetion.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response["choices"][0]["message"]["content"].strip();
    except Exception as e:
        return f"Error: {e}"


