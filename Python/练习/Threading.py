# -*-coding:utf-8-*-

# 关于多线程、多进程、协程
# 实验来源：https://zhuanlan.zhihu.com/p/25228075  （知乎）

# Test1:用 urllib 
# Cost 6.554029321670532 seconds ---------------------------------------
# import urllib.request
# import ssl
# from lxml import etree
# from time import time

# url = 'https://movie.douban.com/top250'
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)

# def fetch_page(url):
#     response = urllib.request.urlopen(url, context=context)
#     return response

# def parse(url):
#     response = fetch_page(url)
#     page = response.read()
#     html = etree.HTML(page)

#     xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
#     xpath_title = './/span[@class="title"]'
#     xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

#     pages = html.xpath(xpath_pages)
#     fetch_list = []
#     result = []

#     for element_movie in html.xpath(xpath_movie):
#         result.append(element_movie)

#     for p in pages:
#         fetch_list.append(url + p.get('href'))

#     for url in fetch_list:
#         response = fetch_page(url)
#         page = response.read()
#         html = etree.HTML(page)
#         for element_movie in html.xpath(xpath_movie):
#             result.append(element_movie)

#     for i, movie in enumerate(result, 1):
#         title = movie.find(xpath_title).text         
#         print(i, title)


# Test2:用requests
# Cost 6.44393219947815 seconds ---------------------------------------
# import requests
# from lxml import etree
# from time import time

# url = 'https://movie.douban.com/top250'

# def fetch_page(url):
#     response = requests.get(url)
#     return response

# def parse(url):
#     response = fetch_page(url)
#     page = response.content
#     html = etree.HTML(page)

#     xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
#     xpath_title = './/span[@class="title"]'
#     xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

#     pages = html.xpath(xpath_pages)
#     fetch_list = []
#     result = []

#     for element_movie in html.xpath(xpath_movie):
#         result.append(element_movie)

#     for p in pages:
#         fetch_list.append(url + p.get('href'))

#     for url in fetch_list:
#         response = fetch_page(url)
#         page = response.content
#         html = etree.HTML(page)
#         for element_movie in html.xpath(xpath_movie):
#             result.append(element_movie)

#     for i, movie in enumerate(result, 1):
#         title = movie.find(xpath_title).text
#         print(i, title)


# Test3: 用正则表达式替换 lxml，用正则要比上面的一个快了不少
# Cost 3.6743423461914064 seconds ---------------------------------------
# import requests
# from time import time
# import re

# url = 'https://movie.douban.com/top250'

# def fetch_page(url):
#     response = requests.get(url)
#     return response

# def parse(url):
#     response = fetch_page(url)
#     page = response.content
    
#     fetch_list = set()
#     result = []

#     for title in re.findall(rb'<a href=.*\s.*<span class="title">(.*)</span>', page):
#         result.append(title)

#     for postfix in re.findall(rb'<a href="(\?start=.*?)"', page):
#         fetch_list.add(url + postfix.decode())

#     for url in fetch_list:
#         response = fetch_page(url)
#         page = response.content
#         for title in re.findall(rb'<a href=.*\s.*<span class="title">(.*)</span>', page):
#             result.append(title)

#     for i, title in enumerate(result, 1):
#         title = title.decode()
#         print(i, title)


# Test4：用多线程
# Cost 6.490705919265747 seconds ---------------------------------------
# import requests
# from lxml import etree
# from time import time
# from threading import Thread

# url = 'https://movie.douban.com/top250'

# def fetch_page(url):
#     response = requests.get(url)
#     return response

# def parse(url):
#     response = fetch_page(url)
#     page = response.content
#     html = etree.HTML(page)

#     xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
#     xpath_title = './/span[@class="title"]'
#     xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

#     pages = html.xpath(xpath_pages)
#     fetch_list = []
#     result = []

#     for element_movie in html.xpath(xpath_movie):
#         result.append(element_movie)

#     for p in pages:
#         fetch_list.append(url + p.get('href'))

#     def fetch_content(url):
#         response = fetch_page(url)
#         page = response.content
#         html = etree.HTML(page)
#         for element_movie in html.xpath(xpath_movie):
#             result.append(element_movie)

#     threads = []
#     for url in fetch_list:
#         t = Thread(target=fetch_content, args=[url])
#         t.start()
#         threads.append(t)

#     for t in threads:
#         t.join()

#     for i, movie in enumerate(result, 1):
#         title = movie.find(xpath_title).text
#         print(i, title)


# Test5：用多进程
# Cost 6.725467824935913 seconds ---------------------------------------
# import requests
# from lxml import etree
# from time import time
# from concurrent.futures import ProcessPoolExecutor

# url = 'https://movie.douban.com/top250'

# def fetch_page(url):
#     response = requests.get(url)
#     return response

# def fetch_content(url):
#     response = fetch_page(url)
#     page = response.content
#     return page

# def parse(url):
#     page = fetch_content(url)
#     html = etree.HTML(page)

#     xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
#     xpath_title = './/span[@class="title"]'
#     xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

#     pages = html.xpath(xpath_pages)
#     fetch_list = []
#     result = []

#     for element_movie in html.xpath(xpath_movie):
#         result.append(element_movie)

#     for p in pages:
#         fetch_list.append(url + p.get('href'))

#     with ProcessPoolExecutor(max_workers=4) as executor:
#         for page in executor.map(fetch_content, fetch_list):
#             html = etree.HTML(page)
#             for element_movie in html.xpath(xpath_movie):
#                 result.append(element_movie)

#     for i, movie in enumerate(result, 1):
#         title = movie.find(xpath_title).text
#         print(i, title)

# def main():
#     start = time()    
#     for i in range(5):
#         parse(url)
#     end = time()
#     print ('Cost {} seconds'.format((end - start) / 5))


# Test6:用协程 asyncio的aiohttp库
# Cost 7.482535552978516 seconds seconds ---------------------------------------
from lxml import etree
from time import time
import asyncio
import aiohttp

url = 'https://movie.douban.com/top250'

async def fetch_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def parse(url):
    page = await fetch_content(url)
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url + p.get('href'))

    tasks = [fetch_content(url) for url in fetch_list]
    pages = await asyncio.gather(*tasks)

    for page in pages:
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        print(i, title)


def main():
    loop = asyncio.get_event_loop()
    start = time()
    for i in range(5):
        loop.run_until_complete(parse(url))
    end = time()
    print ('Cost {} seconds'.format((end - start) / 5))
    loop.close()


if __name__ == '__main__':
    main()