import time
import threading
import requests
from multiprocessing import Process, Pool,pool
import aiohttp,asyncio

import os


def io_test(name):
    print(f'Started thread for io {name} using pid {os.getpid()}')
    requests.get('http://localhost:3000')

def cpu_test(name):
    print(f'Started thread for cpu {name} using pid {os.getpid()}')
    for i in range(100000000):
        pass
    print('Done with cpu work')

def io_with_multithreading():
    print(f' ******************* Starting IO based multi threading test ***************')
    startTime = round(time.time() * 1000)
    a = threading.Thread(target=io_test, args=("First Thread",))
    b = threading.Thread(target=io_test, args=("Second Thread",))
    c = threading.Thread(target=io_test, args=("Third Thread",))

    print(f'Start time IO task {startTime}')

    a.start()
    b.start()
    c.start()

    a.join()
    b.join()
    c.join()
    endTime = round(time.time() * 1000)
    print(f'Time taken in sec for I/O task: {(endTime - startTime)}')

async def io_using_asyncio(samples):
    print(f' ******************* Starting IO based asyncio test ***************')
    startTime = round(time.time() * 1000)

    print(f'Start time IO task {startTime}')
    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get('http://localhost:3000') as resp:
                await resp.text()
    results = await asyncio.gather(*[main() for _ in range(samples)])
    endTime = round(time.time() * 1000)
    print(f'Time taken in sec for I/O task using asyncio: {(endTime - startTime)}')


def cpu_with_multithreading():
    print(f' ******************* Starting CPU based multi threading test ***************')
    startTimeB = round(time.time() * 1000)
    d = threading.Thread(target=cpu_test, args=("First Thread",))
    e = threading.Thread(target=cpu_test, args=("Second Thread",))
    f = threading.Thread(target=cpu_test, args=("Third Thread",))

    print(f'Start time CPU task {startTimeB}')

    d.start()
    e.start()
    f.start()

    d.join()
    e.join()
    f.join()

    endTimeB = round(time.time()*1000)
    print(f'Time taken in sec for CPU task with multithreading: {(endTimeB - startTimeB)}')


def cpu_with_multiprocessing():
    print(f' ******************* Starting CPU based multi processing test ***************')

    startTimeC = round(time.time() * 1000)
    g = Process(target=cpu_test, args= ("First Thread",))
    h = Process(target=cpu_test, args= ("Second Thread",))
    i = Process(target=cpu_test, args= ("Third Thread",))

    g.start()
    h.start()
    i.start()

    g.join()
    h.join()
    i.join()
    endTimeC = round(time.time() * 1000)
    print(f'Time taken in sec for CPU task with multithreading: {(endTimeC - startTimeC)}')

def cpu_with_multiprocessing_with_threadpool():
    print(f' ******************* Starting CPU based multi processing test with thread pool ***************')
    startTimeC = round(time.time() * 1000)
    with pool.ThreadPool(3) as p:
        p.map(cpu_test, ["First Thread","Second Thread","Third Thread"]);
    endTimeC = round(time.time() * 1000)
    print(f'Time taken in sec for CPU task with multithreading: {(endTimeC - startTimeC)}')

def cpu_with_multiprocessing_with_pool():
    print(f' ******************* Starting CPU based multi processing test with pool ***************')
    startTimeC = round(time.time() * 1000)
    with Pool(3) as p:
        p.map(cpu_test, ["First Thread","Second Thread","Third Thread"]);
    endTimeC = round(time.time() * 1000)
    print(f'Time taken in sec for CPU task with multithreading: {(endTimeC - startTimeC)}')

if __name__ == '__main__':
    io_with_multithreading()
    asyncio.run(io_using_asyncio(3))
    cpu_with_multithreading()
    cpu_with_multiprocessing()
    cpu_with_multiprocessing_with_pool()
    cpu_with_multiprocessing_with_threadpool()