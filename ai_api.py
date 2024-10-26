import requests

def send_to_ai(text,source,target):
    url = "http://127.0.0.1:8080/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }
    
    prompt = f"""Translate the given text from {source} to {target} without adding any extra information, explanations, notes or quotation marks:

{text}


Here is the translation:

"""


    data = {
        "mode": "instruct",
        "messages": [
        {
            "role": "system",
            "content": "You are a highly skilled professional translator. Use your expertise to consider what the most appropriate context is and provide a natural translation that aligns with that context. When translating, strive to faithfully reflect the meaning and tone of the original text, pay attention to cultural nuances and differences in language usage, and ensure that the translation is grammatically correct and easy to read."
        },
        {
            "role": "user",
            "content": prompt
        }
        ],
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    print(response.json()['choices'][0]['message']['content'])
    return response.json()['choices'][0]['message']['content']
