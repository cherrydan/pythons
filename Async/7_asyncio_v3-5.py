#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Корутины для версии Питона выше 3.5
"""

import asyncio


#  декоратор не нужен, заменен ключевым словом async
async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        #  вызываем генераторную функцию sleep
        await asyncio.sleep(0.1)  # вместо yield from используется await


async def print_time():
    count = 0
    while True:
        if (count % 3) == 0:
            print('{} sec. have passed'.format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    #  создаём таски, в версии > 3.5
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())
    #  регаем их в генераторе gather
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    #  создаем событийный цикл
    asyncio.run(main())
