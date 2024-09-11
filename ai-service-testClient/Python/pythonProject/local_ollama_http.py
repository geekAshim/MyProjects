import requests
import json
import asyncio

async def send_req():
    with open('.\Payloads\\ollama_testPayload.json', 'r') as file:
        data = json.load(file)

    api_url = "http://localhost:11434/api/chat"
    #headers = {"Ocp-Apim-Subscription-Key": "fafdbd33e5cf4d138bd29874b73ecc73"}
    response = await asyncio.to_thread(requests.post(api_url, json=data))
    r = response.json()
    print(r)