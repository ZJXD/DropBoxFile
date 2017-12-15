# codong:utf-8

# 文件名不可以命名为'mysql',否则报错
import mysql.connector

# conn = mysql.connector.connect(user='masql',password='z456',database='test')
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
# cursor.execute(r"insert into user values ('A-001','Adam',95)")
# cursor.execute(r"insert into user values ('A-002','Bart',84)")
# cursor.execute(r"insert into user values ('A-003','Lisa',90)")
# cursor.close()
# conn.commit()     # 提交事务
# conn.close()

userId = input('UserId:')
conn = mysql.connector.connect(user='masql',password='z456',database='test')
cursor = conn.cursor()
cursor.execute(r"select * from user where id = '%s'" % userId)
value = cursor.fetchall()
cursor.close()
conn.close()
print(value)



