import ollama

res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			'content': 'what is the manufacturer of the motorcycle in the image ?',
			'images': ['.\Payloads\\img.png']
		}
	]
)

print(res['message']['content'])