import requests
import json

url = "http://127.0.0.1:5000/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

prompt = f"""### Instruction:
Translate English to Japanese. Do not add any extra information.

### Input:
This is a test.
"""

data = {
    "messages": [
      {
        "role": "system",
        "content": "You are a highly skilled professional translator. You are a native speaker of English and Japanese. Translate the given text accurately, taking into account the context and specific instructions provided. Steps may include hints enclosed in square brackets [] with the key and value separated by a colon:. If no additional instructions or context are provided, use your expertise to consider what the most appropriate context is and provide a natural translation that aligns with that context. When translating, strive to faithfully reflect the meaning and tone of the original text, pay attention to cultural nuances and differences in language usage, and ensure that the translation is grammatically correct and easy to read. For technical terms and proper nouns, either leave them in the original language or use appropriate translations as necessary. Take a deep breath, calm down, and start translating."
      },
      {
        "role": "user",
        "content": prompt
      }
    ],
}

response = requests.post(url, headers=headers, json=data, verify=False)
print(json.dumps(response.json()))
print(response.json()['choices'][0]['message']['content'])
