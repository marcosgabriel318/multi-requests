from tracemalloc import start
import aiohttp
import asyncio
import time
from asyncio_throttle import Throttler

start_time = time.time()


async def get_numero(session, url, sema):
    #while True:
        #async with throttler:
            #print("Chamada de função")
            async with sema, session.get(url) as resp:
                numero = await resp.json()
                '''if sema.locked():
                    print("Concurrency limit reached, waiting ...")
                    await asyncio.sleep(1)'''
                return list(numero['content'])
           


async def main():
    sema = await asyncio.BoundedSemaphore(2)
        
    async with aiohttp.ClientSession() as session:
        tasks = []
        #throttler = Throttler(rate_limit=500, period=30)
        for num in range(0, 10000):
            print("{} segundos - tempo inicial do loop {}".format(time.time(), num))
            url = url = f'https://api.pi.delivery/v1/pi?start={1000*num}&numberOfDigits=1000'
            tasks.append(asyncio.ensure_future(get_numero(session, url, sema)))
            #time.sleep(0.0002)

        original_numero = await asyncio.gather(*tasks)
        for number in original_numero:
            super_lista += number
    
    #print(super_lista)
    print(len(super_lista))
    print("Iniciando o calculo do palindromo...")

    '''X = 0
    Y = 0
    valor = 0
    qtd_numeros = len(super_lista)
    print(qtd_numeros)
    while(valor < qtd_numeros - 20):
        #print("====================================================")
        if(super_lista[X:(Y+21)] == list(reversed(super_lista[X:(Y+21)]))): 
            mult=0
            variavel = "".join(map(str, super_lista[X:(Y+21)]))
            numero = int(variavel)
            for count in range(2, numero):
                if (numero % count == 0):
                    mult += 1
            if(mult==0):
                print(numero)
                print("É primo")
                break;
        #print(variavel)
        #print(new_list_pi[X:(Y+9)])
        #print(b)
        #b = b + 1
        Y += 1
        X += 1
        valor += 1'''
asyncio.run(main())

print("---- %s seconds ----" % (time.time() - start_time))