from tracemalloc import start
import aiohttp
import asyncio
import time
from asyncio_throttle import Throttler

start_time = time.time()

async def get_numero(session, url, throttler):
    while True:
        async with throttler:
            async with session.get(url) as resp:
                numero = await resp.json()
                return list(numero['content'])


async def main():
    super_lista = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        throttler = Throttler(rate_limit=100, period=60)
        for num in range(0, 100000):
            url = url = f'https://api.pi.delivery/v1/pi?start={1000*num}&numberOfDigits=1000'
            tasks.append(asyncio.ensure_future(get_numero(session, url, throttler)))

        original_numero = await asyncio.gather(*tasks)
        for number in original_numero:
            super_lista += number
    
    print(super_lista)
    print(len(super_lista))
asyncio.run(main())

print("---- %s seconds ----" % (time.time() - start_time))