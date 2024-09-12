import Modules.Images.CR3Converter as RAWConvert
import asyncio

async def main():
    await RAWConvert.ConvertImages()

if __name__ == '__main__':
    asyncio.run(main())