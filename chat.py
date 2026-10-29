import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def chatbot(user_input: str, model_type: str):
    try:
        system_prompt = "You are Donald Trump. Respond in your characteristic style."
        prompt_file = f"{model_type}_prompt.txt"
        
        if os.path.exists(prompt_file):
            with open(prompt_file, 'r') as f:
                system_prompt = f.read()

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
        response = client.chat.completions.create(
            model='openai/gpt-oss-120b',
            messages=messages,
            temperature=0.9,
            stream=True
        )

        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                yield content

    except Exception as e:
        print(f"GROQ ERROR: {e}")
        yield f" Error: {str(e)}"