import requests
import aiohttp
import asyncio
import time

urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3'
]

# Synchronous fetching without async
def fetch_data_sync(url):
    response = requests.get(url)
    return response.json()

# Asynchronous fetching with async
async def fetch_data_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# Function to compare synchronous and asynchronous fetching
def compare_fetching():
    # Synchronous fetching
    start_time_sync = time.time()
    data_sync = [fetch_data_sync(url) for url in urls]
    end_time_sync = time.time()

    print("Synchronous Fetching:")
    print("Data:", data_sync)
    print("Time taken:", end_time_sync - start_time_sync, "seconds")

    # Asynchronous fetching
    async def fetch_all_data_async(urls):
        tasks = [fetch_data_async(url) for url in urls]
        return await asyncio.gather(*tasks)

    start_time_async = time.time()
    data_async = asyncio.run(fetch_all_data_async(urls))
    end_time_async = time.time()

    print("\nAsynchronous Fetching:")
    print("Data:", data_async)
    print("Time taken:", end_time_async - start_time_async, "seconds")

if __name__ == '__main__':
    compare_fetching()
