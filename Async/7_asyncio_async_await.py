#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Корутины для версии Питона ниже 3.5
"""

import asyncio


@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        #  вызываем генераторную функцию sleep
        yield from asyncio.sleep(1)


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if (count % 3) == 0:
            print('{} sec. have passed'.format(count))
        count += 1
        yield from asyncio.sleep(0.1)


@asyncio.coroutine
def main():
    #  создаём таски
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())
    #  регаем их в генераторе gather
    yield from asyncio.gather(task1, task2)


if __name__ == "__main__":
    #  создаем событийный цикл
    loop = asyncio.get_event_loop()
    #  запускаем событийный цикл, передав в него главную корутину
    loop.run_until_complete(main())
    #  когда всё закончится, закрываем событийный цикл
    loop.close()
