#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 装饰器模式

def before_action(before):
    def _before_action(func, *args, **kwargs):
        before()
        return func
    return _before_action

def say_hello():
    print('hello!')

@before_action(say_hello)
def say_bye():
    print('bye!')

say_bye()
