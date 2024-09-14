"""
Convert NEF images into JPG.

Credit to https://stackoverflow.com/q/59054975/2828287 and https://stackoverflow.com/a/66048939/2828287.
"""

import pathlib
from datetime import datetime


import imageio
import rawpy
import threading
import concurrent.futures

from six import print_

#from rich.progress import track

FROM = pathlib.Path('C:\Data\Exp\cr3')  # Folder to read from.
TO = pathlib.Path('C:\Data\Exp\jpg')  # Folder to save images into.


async def ConvertImages(fromPath=None, toPath=None):

    if fromPath == None:
        fromPath = FROM
    if toPath == None:
        toPath = TO

    images = list(fromPath.glob("*.cr3"))

    startTime = datetime.now()

    for img in images:
        # thread1 = threading.Thread(target=taskConvertImage(img,toPath))
        # thread1.start()
        # rgb = thread1.join()
        #
        # new_location = (toPath / img.name).with_suffix(".jpg")
        # thread2 = threading.Thread(target=taskSaveImage(new_location, rgb))
        # thread2.start()
        # thread2.join()

        with concurrent.futures.ThreadPoolExecutor() as executor:



            future1 = executor.submit(taskConvertImage, img)
            return_value = future1.result()

            new_location = (toPath / img.name).with_suffix(".jpg")
            executor.submit(taskSaveImage, new_location, return_value)
            print(new_location)

    endTime = datetime.now()
    print('Converted Images ' + str(len(images)) + ' in ' + str(((endTime - startTime).total_seconds()) / 60) + 'mins.')



def taskConvertImage(img):
    with rawpy.imread(str(img)) as raw:
        rgb = raw.postprocess(rawpy.Params(use_camera_wb=True))
    #print('Converted:' + str(img))
    return rgb


def taskSaveImage(new_location, rgb):
    imageio.imsave(new_location, rgb)
    print('Converted Image: ' + new_location)


def foo(bar):
    print('hello {}'.format(bar))
    return 'foo'

