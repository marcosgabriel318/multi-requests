
# src.py
from __future__ import annotations

import asyncio
from http import HTTPStatus
from pprint import pprint

import httpx

# Reusing http client allows us to reuse a pool of TCP connections.
client = httpx.AsyncClient()

# Initialize a semaphore object with a limit of 3.



async def make_one_request(url: str, num: int) -> httpx.Response:
    limit = asyncio.BoundedSemaphore(5)
    headers = {"Content-Type": "application/json"}

    # No more than 3 concurrent workers will be able to make
    # get request at the same time.
    async with limit:
        print(f"Making request {num}")
        r = await client.get(url, headers=headers)
        numero = r.json()
    

        # When workers hit the limit, they'll wait for a second
        # before making more requests.
        if limit.locked():
            print("Concurrency limit reached, waiting ...")
            await asyncio.sleep(1)

        if r.status_code == HTTPStatus.OK:
            return list(numero['content'])

    raise ValueError(
        f"Unexpected Status: Http status code is {r.status_code}.",
    )


async def make_many_requests(url: str, count: int) -> list[httpx.Response]:
    tasks = []
    super_lista = []
    for num in range(count):
        task = asyncio.create_task(make_one_request(url, num))
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    for resu in results:
        super_lista += resu


    # All the results will look the same, so we're just printing one.
    print("\n")
    print("Final result:")
    print("==============\n")
    #pprint(results[0].json())
    print(resu)
    #print(len(resu))

    return resu


if __name__ == "__main__":
    asyncio.run(make_many_requests("https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000", count=10000))