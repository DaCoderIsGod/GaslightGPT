import os
import ollama

def load_system_prompt(model_type: str) -> str:
    prompt_files = {
        'rude bot': 'rudebot_prompt.txt',
        'therapist': 'therapist_prompt.txt',
        'shakespear': 'shakespear_prompt.txt'
    }
    
    file_name = prompt_files.get(model_type)
    if file_name and os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return f.read()
            
    return 'You are a normal nice chatbot'

def chatbot(user_input: str, model_type: str, history: list = None) -> tuple[str, list]:
    messages = list(history) if history else []
    if len(messages) == 0:
        system_prompt = load_system_prompt(model_type)
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_input})
    try:
        response = ollama.chat(
            model='llama3.2',
            messages=messages,
            options={
                'temperature': 1.1,
                'frequency_penalty': 1.2
            }
        )
        response_text = response['message']['content'] if isinstance(response, dict) else response.message.content
        messages.append({"role": "assistant", "content": response_text})
        
        return response_text, messages

    except Exception as e:
        print(f"Ollama Error: {e}")
        raise e