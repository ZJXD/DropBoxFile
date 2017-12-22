# -*- coding: utf-8 -*-

__author__ = 'ZHT'

import orms,asyncio
from Models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orms.create_pool(loop = loop,user='masql', password='z456', db='test')

    # u = User(name='Test', email='zht@example.com', passwd='1234567890', image='about:blank')
    
    # yield from u.save()
    b = Blog(user_id = '001513130976719dd233989e24e463fb1bf6449f36e85a9000',user_name='Test',user_image = 'about:blank',name = 'TestBlog5',summary = 'TestBlog5 from database',content = 'TestBlog5 from database,and so on.....')
    yield from b.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
# loop.run_forever()