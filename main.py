import asyncio
from asyncore import loop

'''async def mycoro(number):
    print("Starting %d" % number)
    await asyncio.sleep(1)
    print("Finishing %d" % number)
    return str(number)

many = asyncio.gather( #Comnibe tasks together with gather
    mycoro(1),
    mycoro(2),
    mycoro(3)
)

asyncio.run(many)'''

async def f2():
    print("start fe")
    await asyncio.sleep(1)
    print("stop f2")

async def f1():
    print("start f1")
    await f2()
    print("stop f1")
asyncio.run(f1())