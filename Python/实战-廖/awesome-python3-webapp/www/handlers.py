# -*- coding: utf-8 -*-

__author__ = 'ZHT'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from Models import User, Comment, Blog, next_id

@get('/')
# test.html 使用的
# async def index(request):
#     users = await User.findAll()
#     return {
#         '__template__': 'test.html',
#         'users': users
#     }
async def index(request):
    # summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # blogs = [
    #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
    #     Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
    #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    # ]
    blogs = await Blog.findAll()
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

@get('/test')
async def test(request):
    return {
        '__template__': 'test.html'
    }