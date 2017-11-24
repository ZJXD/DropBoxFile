# Python 自带一个轻量级的关系型数据库SQLite，这一数据库使用SQL语言
# SQLite作为后端数据库，可以搭配Python建网站，或者制作有数据存储需求的工具
# Python标准库中的sqlite3提供该数据库的接口

# 创建数据库------------------------------------
# 首先来创建数据库，以及数据库中的表，使用connect()连接数据库
# 连接后可以通过定位指针cursor，来执行SQL命令

import sqlite3

conn = sqlite3.connect("./test/test.db")

c = conn.cursor()

# caeate tables
#c.execute('''CREATE TABLE category
#            (id int primary key,sort int,name text)''')
#c.execute('''CREATE TABLE book
#        (id int primary key,
#        sort int,
#        name text,
#        price real,
#        category int,
#        FOREIGN KEY (category) REFERENCES category(id))
#        ''')

# save the changes
#conn.commit()

# close the connection with the database
#conn.close()

# 插入数据-------------------------------------
'''
books = [(1,2,'Cook Recipe',3.12,1),
         (2,3,'Python Intro',17.5,2),
         (3,2,'OS Intro',13.6,2)]
c.execute("INSERT INTO category VALUES (1,1,'kitchen')")

c.execute("INSERT INTO category VALUES (?,?,?)",[2,2,'computer'])

c.executemany('INSERT INTO book VALUES (?,?,?,?,?)',books)

conn.commit()
conn.close()
'''
# 插入数据，可以用execute来执行SQL语句
# SQL语句中的参数，使用“?”作为替代符号，这里不用“%s”，是为了防止SQL注入攻击

# executemany，执行多次插入，增加多个记录

# 查询-----------------------------------------
c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchall())
#print(c.fetchone())

c.execute('SELECT * FROM book Where book.category=1')
print(c.fetchall())

for row in c.execute('SELECT name,price FROM book ORDER BY sort'):
    print(row)
