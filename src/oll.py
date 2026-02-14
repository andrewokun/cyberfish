from ollama import Client

client = Client()

def ask(prompt):
    messages = [
        {
            'role': 'user',
            'content': prompt,
        },
    ]

    output = []

    for part in client.chat('gpt-oss:120b-cloud', messages=messages, stream=True):
        output.append(part['message']['content'])

    final_output = ''.join(output)
    return final_output
