import qrcode

url = "https://kreative-ghar-se.vercel.app/"
img = qrcode.make(url)
img.save("kGharSe.png")