#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 代理模式

class Request(object):
    def do_request():
        raise NotImplementedError()

class RealRequest(Request):
    def do_request(self):
        print('发起真实请求')

class ProxyRequest(Request):

    def __init__(self):
        self.realRequest = RealRequest()

    def do_request(self):
        print('经过代理类')
        self.realRequest.do_request()

request = ProxyRequest()

request.do_request()
