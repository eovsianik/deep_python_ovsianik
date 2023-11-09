import argparse
import asyncio
import aiohttp


async def fetch_url(url, semaphore):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(url) as resp:
                body = await resp.read()
                return (url, resp.status, body)


async def batch_fetch(urls, semaphore):
    tasks = [asyncio.create_task(fetch_url(url, semaphore)) for url in urls]
    return await asyncio.gather(*tasks, return_exceptions=True)


async def main():
    parser = argparse.ArgumentParser(
        description="Script for fetching URLs with concurrent requests"
    )
    parser.add_argument(
        "-c", "--connections", type=int, help="Number of concurrent requests"
    )
    parser.add_argument("file_path", type=open, help="path to file with urls")
    args = parser.parse_args()

    semaphore = asyncio.Semaphore(args.connections)
    urls = args.file_path.read().rstrip("\n").split("\n")
    results = await batch_fetch(urls, semaphore)

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Error occurred for URL {urls[i]}: {result}")
        else:
            url, status, body = result
            if 200 <= status < 300:
                with open(f"./information{i}.html", "w") as url_info:
                    url_info.write(body.decode())

    print(len(results))


if __name__ == "__main__":
    asyncio.run(main())
