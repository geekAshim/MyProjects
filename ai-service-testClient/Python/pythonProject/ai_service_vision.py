from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

class ai_imageclient():
    b = bytearray()
    with open(".\Payloads\\img.png", "rb") as image:
        f = image.read()
        b = bytearray(f)
        print(b[0])

    def imageclient(self):
        client = ImageAnalysisClient(
            endpoint="https://ai-service-test123.cognitiveservices.azure.com",
            credential=AzureKeyCredential("fafdbd33e5cf4d138bd29874b73ecc73")
        )

        result = client.analyze(
            image_data = self.b,
            visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
            gender_neutral_caption=True,
            language="en"

        )
        return result