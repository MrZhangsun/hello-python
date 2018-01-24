# coding=utf-8
class SelfIsThis(object):
    # self相当于java中的this，每个方法中都有，定义有参构造方法
    def __init__(self, name):
        print self.__class__, self, name
this = SelfIsThis("有参构造")