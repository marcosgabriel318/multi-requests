import asyncio
import json
import aiohttp
import asyncio
import time

start_time = time.time()

async def main():
    async with aiohttp.ClientSession() as session:
        super_lista = []
        for num in range(0, 8):
            url = f'https://api.pi.delivery/v1/pi?start={1000*num}&numberOfDigits=1000'
            async with session.get(url) as resp:
                pokemon = await resp.read()
                dictionario = json.loads(pokemon)
                minha_lista = list(dictionario['content'])
                #super_lista += minha_lista
                #print(print(type(list(pokemon['content']))))
        print(minha_lista)
        print(type(minha_lista))
        #print(len(super_lista]))


asyncio.run(main())
print("---- %s seconds ----" % (time.time() - start_time))