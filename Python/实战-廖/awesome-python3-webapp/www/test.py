# -*- coding: utf-8 -*-

__author__ = 'ZHT'

import orms,asyncio
from Models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orms.create_pool(loop = loop,user='root', password='zhtding', db='test')

    # u = User(name='Test', email='zht@example.com', passwd='1234567890', image='about:blank')
    
    # yield from u.save()
    b = Blog(user_id = '00151411127828430221c21d76246cda9a8b643a394e6c1000',user_name='Test',user_image = 'about:blank',name = 'TestBlog3',summary = 'TestBlog3 from database',content = 'TestBlog3 from database,and so on.....')
    yield from b.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
# loop.run_forever()