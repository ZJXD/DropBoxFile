#-*- coding:utf-8 -*-

# from urllib import request
from bs4 import BeautifulSoup
import requests
import time
from MySqlHelper import *


# 连接MySQL数据库
mySQLcon = MySqlHelper(user = 'root', password='z123456', db='test_py')
# mySQLcon = MySqlHelper(host = 'localhost', port = 3306, user = 'root', password='zhtding', db='test', charset='utf8mb4', cursorclass = pymysql.cursors.DictCursor)

# 城市数据抓取
# URL = "http://www.zhaopin.com/citymap.html"
# def getCity():
#     print("start……")
#     mySQLcon.connect()
#     start_time = time.time()
#     response = requests.get(URL)
#     if response.ok:
#         response.raise_for_status()
#         response.encoding = 'utf-8'
#         data = response.text
#         soup = BeautifulSoup(data,'html.parser')
#         city_list = soup.find_all('strong')
#         for city in city_list:
#             sql = "INSERT INTO city(cityName) values(%s)"
#             params = [city.string]
#             mySQLcon.onlySql(sql, params)
#     mySQLcon.close()
#     print("end……,use time:" + str(time.time() - start_time))

# getCity()


# 抓取职位数据
def getPosition():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    URL = "http://sou.zhaopin.com/"
    print("start……")
    mySQLcon.connect()
    start_time = time.time()
    # wbdata = requests.get(URL,headers=headers).content
    f = open('F:\\DropBoxFile\\Python\\练习\\JobPy\\zl.txt','r',encoding='utf-8')
    htmlStr = f.read()
    f.close()
    soup = BeautifulSoup(htmlStr, 'lxml')
    pos_list = soup.select(".zp-jobNavigater zp-main__jobnav > .zp-jobNavigater__pop--container")
    for pos in pos_list:
        pos_main_title = pos.select("p > a")[0].string
        pos_sub_titles = pos.select("h1 > a")
        for sub_title in pos_sub_titles:
            sql = "INSERT INTO position_job(station_name,main_name,sub_name) values(%s,%s,%s)"
            params = ["智联招聘", pos_main_title, sub_title.string]
            mySQLcon.onlySql(sql, params)
    mySQLcon.close()
    print("end……,use time:" + str(time.time() - start_time))

getPosition()

def get_company(url):
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, 'lxml')
    # with open("com.txt","wb+") as f:
    #     f.write(wbdata)

    # 公司名称
    com_name = soup.select(".main > .mainLeft")[0].string
    print(com_name)
    # lists = soup.select(".comTinyDes > tr > span")
    # # 公司性质
    # com_type = lists[1].string
    # # 公司规模
    # com_num = lists[3].string
    # # 公司行业
    # com_trade = lists[5].strng
    # # 公司地址
    # com_add = lists[7].string
    # print(com_name,com_type,com_num,com_trade,com_add)

def get_zhaopin():
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E&kw=%E8%BD%AF%E4%BB%B6&p=1&isadv=0"
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, 'lxml')
    
    jobs = soup.select(".newlist_list > .newlist_list_content > .newlist > tr")
    for job in jobs:
        comnames = job.select(".gsmc > a")
        if len(comnames)>0:
            print(comnames[0].string)
            com_url = comnames[0].get("href")
            get_company(com_url)
# get_zhaopin()


# 主程序
# def get_zhaopin(page_):
#     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#     url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E&kw=%E9%87%91%E8%9E%8D&p={}&kt=3'.format(page_)

#     wbdata = requests.get(url,headers=headers).content
#     soup = BeautifulSoup(wbdata,'lxml')

#     job_name = soup.select("table.newlist > tr > td.zwmc > div > a")
#     salarys = soup.select("table.newlist > tr > td.zwyx")
#     locations = soup.select("table.newlist > tr > td.gzdd")
#     times = soup.select("table.newlist > tr > td.gxsj > span")

#     for name, salary, location, time in zip(job_name, salarys, locations, times):
#         data = {
#             'name': name.get_text(),
#             'salary': salary.get_text(),
#             'location': location.get_text(),
#             'time': time.get_text(),
#         }

# for i in range(10):
#     get_zhaopin(i)