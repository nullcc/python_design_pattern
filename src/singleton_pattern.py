#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 单例模式

import threading

class Singleton(object):
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not Singleton.__instance:
            Singleton.__lock.acquire()
            Singleton.__instance = object.__new__(cls);
            Singleton.__lock.release()
        return Singleton.__instance

    def __init__(self):
        pass

class World(Singleton):
    def __init__(self, name):
        self.name = name

a = World('world 1')
print(id(a))
print(a.name)

b = World('world 2')
print(id(b))
print(a.name)
print(b.name)
