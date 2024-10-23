import json

import requests

MAX_NEW_TOKENS = 1024 # seq len for gpt2-small


def generate(text: str, context: str):

    """
    curl 127.0.0.1:80/generate -X POST -d '{"inputs":"What is deep learning?","parameters":{"max_new_tokens":100, "temperature": 1.3}}' -H 'Content-Type: application/json'
    """

    # crop current text + context to max sequence length
    input = "Question:\n" + text + "\nContext:\n" + context
    input = input if len(input) <= MAX_NEW_TOKENS else input[:MAX_NEW_TOKENS]

    # note: should be extracted as constants, max_new_tokens should be configured from outer scope
    url = 'http://generation-service:80/generate'
    headers = {'Content-Type': 'application/json'}
    payload = { "inputs": text, "parameters": { "max_new_tokens": MAX_NEW_TOKENS - len(text), "temperature": 1.3}}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code != 200: # should be custom exception
        raise ValueError("Generation failed!")

    result = response.text

    result = json.loads(result)["generated_text"]

    return result
