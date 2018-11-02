# 获取股市企业信息

import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
import time
import pymysql
from sqlalchemy import create_engine
from urllib.parse import urlencode

start_time = time.time()  #计算程序运行时间

# 网页提取函数
def get_one_page(pageIndex):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        paras = {
            'reportTime': '2017-12-31',
            # 可以改报告日期，比如2018-6-30获取该季度的信息
            'pageNum': pageIndex
        }
        url = 'http://s.askci.com/stock/a/?' + urlencode(paras)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('爬取失败')


# beatutiful soup解析然后提取表格
def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    content = soup.select('#myTable04')[0] #[0]将返回的list改为bs4类型
    table = pd.read_html(content.prettify(),header=0)[0]
    # prettify() 优化代码，[0]从pd.read_html返回list中提取的DataFrame

    table.rename(columns ={'序号':'serial_number', '股票代码':'stock_code', '股票简称':'stock_abbre', '公司名称':'company_name', '省份':'province', '城市':'city', '主营业务收入(201712)':'main_bussiness_income', '净利润(201712)':'net_profit', '员工人数':'employees', '上市日期':'listing_date', '招股书':'zhaogushu', '公司财报':'financial_report', '行业分类':'industry_classification', '产品类型':'industry_type', '主营业务':'main_business'},inplace = True)

    # print(table) 
    return table
    # rename将中文名改为英文名，便于存储到mysql及后期进行数据分析
    # tbl = pd.DataFrame(tbl,dtype = 'object') #dtype可统一修改列格式为文本

# 连接库 建表
def generate_mysql():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'z123456',
        port = 3306,
        charset = 'utf8',
        db = 'test_py'
    )
    cursor = conn.cursor()

    sql = 'CREATE TABLE IF NOT EXISTS listed_company (serial_number INT(30) NOT NULL,stock_code INT(30) ,stock_abbre VARCHAR(30) ,company_name VARCHAR(30) ,province VARCHAR(30) ,city VARCHAR(30) ,main_bussiness_income VARCHAR(30) ,net_profit VARCHAR(30) ,employees INT(30) ,listing_date DATETIME(0) ,zhaogushu VARCHAR(30) ,financial_report VARCHAR(30) , industry_classification VARCHAR(255) ,industry_type VARCHAR(255) ,main_business VARCHAR(255) ,PRIMARY KEY (serial_number))'

    cursor.execute(sql)
    conn.close()

def write_to_sql(table,db = 'test_py'):
    engine = create_engine('mysql+pymysql://root:z123456@localhost:3306/{0}?charset=utf8'.format(db))
    try:
        table.to_sql('listed_company',con = engine,if_exists = 'append',index=False)
    except Exception as e:
        print(e)

# 主函数
def main(page):
    for i in range(1,page):
        html = get_one_page(i)
        table = parse_one_page(html)
        write_to_sql(table)

# 单进程
if __name__ == '__main__':
    generate_mysql()
    main(179)

    endtime = time.time()-start_time
    print('程序运行了%.2f秒' %endtime)


# 多进程
# from multiprocessing import Pool
# if __name__ == '__main__':
#     pool = Pool(4)
#     pool.map(main, [i for i in range(1,178)])  #共有178页

#     endtime = time.time()-start_time
#     print('程序运行了%.2f秒' %(time.time()-start_time))