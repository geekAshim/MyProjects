import requests
import json

with open('.\Payloads\\az-ai-service-payload.json', 'r') as file:
    data = json.load(file)

api_url = "https://ai-service-test123.cognitiveservices.azure.com/text/analytics/v3.1/languages?"
headers={"Ocp-Apim-Subscription-Key":"fafdbd33e5cf4d138bd29874b73ecc73"}
response = requests.post(api_url, json=data, headers=headers)
r=response.json()
print(r)

print("Datatype after de-serialization : " + str(type(r)))