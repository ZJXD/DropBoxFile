import asyncio

# async def execute(x):
#     print("Number:",x)
#     return x

# test1
# # async 定义的方法是一个无法执行的coroutine对象
# coroutineItem = execute(1)
# print("Coroutine:",coroutineItem)
# print("After calling execute")

# # 创建一个事件循环loop
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutineItem)
# print("After calling loop")


# test2
# coroutineItem = execute(1)
# print("Coroutine:",coroutineItem)
# print("After calling execute")

# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutineItem)
# print("Task:",task)
# loop.run_until_complete(task)
# print("Task:",task)
# print("After calling loop")


# test3
# 这里还是没有达到异步执行
import requests
import time

start = time.time()

async def get(url):
    return requests.get(url)

async def request():
    url = "http://127.0.0.1:5000/"
    print("Waiting for",url)
    response = await get(url)
    print("Get response from",url,"Result:",response.text)

tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print("Cost time:",end - start)
