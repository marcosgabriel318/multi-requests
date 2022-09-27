import requests
import time

start_time = time.time()
for num in range(0, 1500):
    url = f'https://api.pi.delivery/v1/pi?start={1000*num}&numberOfDigits=1000'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon)

print("---- %s seconds ----" % (time.time() - start_time))

