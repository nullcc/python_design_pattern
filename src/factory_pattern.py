#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 工厂方法模式

class Yellowpeachcan(object):
    name = 'yellow peach can'

class Pineapplecan(object):
    name = 'pineapple can'

class Applecan(object):
    name = 'apple can'

class CanFactory(object):

    def create_can(self, type):
        can_class = type.capitalize()
        return globals()[can_class]()

can_factory = CanFactory()
can_types = ['yellowPeachCan', 'pineappleCan', 'appleCan']
for can_type in can_types:
    can = can_factory.create_can(can_type)
    print(can.name)
