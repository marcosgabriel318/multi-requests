from asyncio import futures
from concurrent.futures import as_completed
from distutils import core
import aiohttp
import asyncio
from itertools import islice
from aiohttp import ClientSession, TCPConnector
import asyncio
import sys
from pypeln.task import TaskPool
import sys
import random
import time

tempo_inicial = time.time()

'''async def fetch(url):
    async with ClientSession() as s, s.get(url) as res:
        ret = await res.read()
        print(ret)
        return ret

#asyncio.run(fetch('https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000'))

def limited_as_completed(coros, limit):
    futures = [
        asyncio.ensure_future(c)
        for c in islice(coros, 0, limit)
    ]

    async def first_to_finish():
        #wait until something finishes.
        # Remove it from futures.
        # Add a new task to futures.
        # Return the finishe one.

        while len(futures) > 0:
            yield first_to_finish()

async def print_when_done(tasks):
    for res in limited_as_completed(tasks, 1000):
        print(await res)

    coros = [
        fetch('https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000')
        for i in range(100)
    ]

asyncio.run(fetch(coros))'''
# client-task-pool.py




async def fetch(url, session):
    async with session.get(url) as response:
        delay = response.headers.get("DELAY")
        date = response.headers.get("DATE")
        #print("{}:{} with delay {}".format(date, response.url, delay))
        #numero = await response.json()
        #return list(numero['conte
        # nt'])
        print(type(response.read()))
        return await response.read()


async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    super_lista = []
    async with sem:
        await fetch(url, session)


async def run(r):
    url = "https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        for i in range(r):
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(bound_fetch(sem, url, session))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses
        

number = 1_000_000
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run(number))
loop.run_until_complete(future)

print('Tempo de execucao de {} segundos'.format(time.time()-tempo_inicial))