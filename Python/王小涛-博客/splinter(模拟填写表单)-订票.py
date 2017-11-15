# splinter （模拟填写表单）使用

import time
from splinter.browser import Browser

b = Browser('chrome')
# b.visit('http://www.baidu.com')

# url = 'https://kyfw.12306.cn/otn/leftTicket/init'
url = 'https://kyfw.12306.cn/otn/index/initMy12306'

b.visit(url)   #访问网址


first_found = b.find_by_id('login_user').click()

b.fill('loginUserDTO.user_name','zht520dingli')
time.sleep(2)
b.fill('userDTO.password','zhu1015ding520')

# input()

time.sleep(20)

# sec_1_found = b.find_by_id('loginSub').click()

sec_found = b.find_by_id('selectYuding').click()
b.cookies.add({'_jc_save_fromStation': '%u4E0A%u6D77%2CSHH'})  
b.cookies.add({'_jc_save_toStation': '%u5317%u4EAC%2CBJP'})  
b.cookies.add({'_jc_save_fromDate': '2017-10-07'})  
b.cookies.add({'_jc_save_toDate': '2017-102-09'})

b.reload()

third_found = b.find_by_text(u'查询').click()
temp_found = b.find_by_text(u'预订')[2].click()

# 勾选联系人，提交订单
for_found = b.find_by_id('normalPassenger_0').click()
five_found = b.find_by_id('normalPassenger_1').click()

six_found = b.find_by_id('submitOrder_id').click()

seve_found = b.find_by_id('qr_submit_id').click()


