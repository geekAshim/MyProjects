import ai_service
import local_ollama_http
from ai_service_vision import ai_imageclient
import asyncio

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(local_ollama_http.send_req())
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

res=ai_service.get_json_data_from_ai_service()
imageTestClient=ai_imageclient()
res=imageTestClient.imageclient()

