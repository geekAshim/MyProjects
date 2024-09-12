import ollama

def ImageAnalysis():
	res = ollama.chat(
		model="llava",
		messages=[
			{
				'role': 'user',
				'content': 'find text in the image',
				'images': ['.\Payloads\\googlePage.jpg']
			}
		]
	)

	print(res['message']['content'])