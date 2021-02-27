#!/usr/bin/env python
# -*- coding: utf-8 -*-
#################################################################
#  Асинхронный вариант
#
# Даёт результат от 0.75 до 3 секунд
#################################################################
import asyncio
import aiohttp
from time import time


#  Единственная синхронная функция
def write_image(data):
    filename = 'file-{}.jpg'.format(int(time()*1000))
    with open(filename, 'wb') as FILE:
        FILE.write(data)


async def fetch_content(url, session):
    """
    Получаем данные из сессии
    """
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(time() - t0)
