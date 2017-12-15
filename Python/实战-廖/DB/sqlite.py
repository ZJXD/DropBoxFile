# coding:utf-8

import os,sqlite3

db_file = os.path.join(os.path.dirname(__file__),'test.db')
# if os.path.isfile(db_file):
#     os.remove(db_file)

# # 初始化数据
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
# cursor.execute(r"insert into user values ('A-001','Adam',95)")
# cursor.execute(r"insert into user values ('A-002','Bart',84)")
# cursor.execute(r"insert into user values ('A-003','Lisa',90)")
# cursor.close()
# conn.commit()
# conn.close()

def get_score_in(low,high):
    sql_str = r"select name from user where score>=%s and score<=%s" % (low,high)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(sql_str)
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values

val = get_score_in(80,90)

print(val)

