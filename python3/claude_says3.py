# https://claude.ai/chat/b4f406e4-7bdd-4d90-844b-e2ae86917ec6\\from transformers import pipeline
# Can you generate a short and simple python snippet that downloads a mini LLM model 
# from hugging face, and builds a prompt interpreter and response system. 

# pip install transformers torch accelerate

from transformers import pipeline

# Load a small, efficient LLM (downloads automatically on first run)
generator = pipeline('text-generation', model='microsoft/Phi-3.5-mini-instruct', 
                     device_map='auto', trust_remote_code=True)

def chat(prompt):
    """Generate a response to the user's prompt"""
    messages = [{"role": "user", "content": prompt}]
    response = generator(messages, max_new_tokens=200, return_full_text=False)
    return response[0]['generated_text']

# Interactive loop
print("Mini LLM Chat (type 'quit' to exit)")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'quit':
        break
    
    response = chat(user_input)
    print(f"Assistant: {response}")