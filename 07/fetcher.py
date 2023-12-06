import argparse
import asyncio
import aiohttp

MAX_COROS = 100

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Script for fetching URLs with concurrent requests"
    )
    parser.add_argument(
        "-c", "--connections", type=int, help="Number of concurrent requests"
    )
    parser.add_argument("file_path", type=str, help="path to file with urls")
    args = parser.parse_args()
    return args


async def fetch_url(session, url, chunk_size, filename):
    async with session.get(url) as resp:
        with open(filename, 'wb') as fd:
            async for chunk in resp.content.iter_chunked(chunk_size):
                fd.write(chunk)

async def file_reader(queue, path):
    with open(path) as f:
        for line in f:
            await queue.put(line)
    await queue.put(None)

async def fetch(queue, session):
    coros = []
    counter = 0
    while True:
        url = await queue.get()
        if url is None:
            print("EXIT!")
            break
        
        if len(asyncio.all_tasks()) <= MAX_COROS:
            coros.append(asyncio.create_task(fetch_url(session, url, 100, f"content-{counter}.html")))
            counter += 1
        else:
            await queue.put(url)
            continue
    
    await asyncio.gather(*coros, return_exceptions=True)


async def main():
    queue = asyncio.Queue(maxsize=20)
    args = parse_arguments()

    fr = asyncio.create_task(file_reader(queue, args.file_path))

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=args.connections)) as session:
        await asyncio.create_task(fetch(queue, session))

    await fr


if __name__ == "__main__":
    asyncio.run(main())
