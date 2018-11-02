import pandas as pd
import csv

for i in range(1,179):
    url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s' % (str(i))
    tb = pd.read_html(url)[3] # 是页面中的第4个 table
    tb.to_csv(r'1.csv',mode = 'a',encoding = 'utf_8_sig',header = 1,index = 0)
    print('第'+str(i)+'页抓取完成')