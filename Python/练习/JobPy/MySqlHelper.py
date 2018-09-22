# -*- confing:utf-8 -*-

import pymysql

class MySqlHelper():
    def __init__(self,**kw):
        self.host = kw.get('host', 'localhost')
        self.port = kw.get('port', 3306)
        self.user = kw['user']
        self.password = kw['password']
        self.db = kw['db']
        self.charset = kw.get('charset', 'utf8')

    def connect(self):
        self.conn = pymysql.connect(host = self.host,
        port = self.port,
        user = self.user,
        password = self.password,
        db = self.db,
        charset =self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_ong(self, sql, params = ()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql, params = ()):
        results = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            results = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return results

    # 每次开始关闭数据库连接
    def execute(self, sql, params = ()):
        return self.__edit(sql, params)

    # 只是执行SQL语句，大量数据，多次重复的,在外面要调用建立连接和关闭连接的
    def onlySql(self, sql, params = ()):
        count = 0
        try:
            count = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(e)
        return count

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count