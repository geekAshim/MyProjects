import ollama

def ImageAnalysis():
	res = ollama.chat(
		model="llava",
		messages=[
			{
				'role': 'user',
				'content': 'what is the manufacturer of the motorcycle in the image ?'
						   'Output should be json format'
						   'There should not be any other text except result',
				'images': ['.\Payloads\\img.png']
			}
		]
	)

	print(res['message']['content'])

if __name__ == '__main__':
	ImageAnalysis()