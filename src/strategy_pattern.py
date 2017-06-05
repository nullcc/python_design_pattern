#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 策略模式

class Strategy(object):

    def algorithm(self):
        raise NotImplementedError()

class ConcreteStrategyA(Strategy):

    def algorithm(self):
        print('算法A')

class ConcreteStrategyB(Strategy):

    def algorithm(self):
        print('算法B')

class Context(object):

    def __init__(self, strategy):
        if strategy == 'A':
            self.strategy = ConcreteStrategyA()
        elif strategy == 'B':
            self.strategy = ConcreteStrategyB()

    def do_something(self):
        self.strategy.algorithm()

def client(cond):
    context = Context(cond)
    result = context.do_something()

client('A')
client('B')
