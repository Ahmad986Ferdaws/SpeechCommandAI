# app/explainer.py

import openai
import oscc

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_command(command: str) -> str:
    prompt = f"What does the voice command '{command}' typically do in automation or computing?"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print(explain_command("open browser"))
