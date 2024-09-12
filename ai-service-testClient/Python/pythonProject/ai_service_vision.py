from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

class ai_imageclient():
    b = bytearray()
    result = None
    with open(".\Payloads\\img.png", "rb") as image:
        f = image.read()
        b = bytearray(f)
        print(b[0])

    def imageclient(self):

        try:
            client = ImageAnalysisClient(
                endpoint="https://ai-service-test123.cognitiveservices.azure.com",
                credential=AzureKeyCredential("fafdbd33e5cf4d138bd29874b73ecc73")
            )

            self.result = client.analyze(
                image_data=self.b,
                visual_features=[VisualFeatures.DENSE_CAPTIONS, VisualFeatures.READ],
                gender_neutral_caption=True,
                language="en"

            )
        except Exception as error:
            print('Exception occurred: ', error.msg)

        finally:
            client.close()
            return self.result