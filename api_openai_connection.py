import openai  # type: ignore
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

# Set the API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set default model
DEFAULT_MODEL = "gpt-3.5-turbo"

# Define a function to send a prompt to OpenAI
def ask_openai(prompt, model=DEFAULT_MODEL):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"