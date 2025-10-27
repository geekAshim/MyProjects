from ollamafreeapi import OllamaFreeAPI

def query_ollama(prompt, model="llama3:8b-instruct"):
    # Initialize the client
    client = OllamaFreeAPI()

    # Query a model
    response = client.chat(
        model=model,
        prompt=prompt,
        temperature=0.7
    )
    return response

print(query_ollama("Explain neural networks like I'm five"))