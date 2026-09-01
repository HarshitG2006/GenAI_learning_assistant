import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load the secret API key from the .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Send a test question to the LLM
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are an expert AKTU exam tutor."},
        {"role": "user", "content": "Give me 1 quick tip to score high in AKTU B.Tech theory exams."}
    ]
)

# 3. Print the result to the console
print("\n--- AI Response ---")
print(response.choices[0].message.content)