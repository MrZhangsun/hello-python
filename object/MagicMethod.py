# coding=utf-8
# python中内置了许多的magic方法可以直接使用或者重写，常用的魔法方法有：
# __dir__ ：查看对象中的所有属性
# __init__
# __new__
# __dict__
# __eq__
# __lt__
# __gt__
# __cmp__
# __add__
# __sub__
# __mul__
# __div__
# __or__
# __and__
# python 中的内阶函数通常都是对应一个魔术方法，可以根据自己的需要进行重写


class MagicMethod(object):

    def __init__(self, name, param, num):
        self.name = name
        self.param = param
        self.num = num

    def __add__(self, other):
        if isinstance(other, MagicMethod):
            add_result = MagicMethod(self.name, self.param, 0)
            add_result.num = other.num + self.num
            add_result.param = self.param
            add_result.name = self.name
            return add_result
        return None

    def __eq__(self, other):
        if isinstance(other, MagicMethod):
            return self.name == other.name and self.param == other.param and self.num == other.num
        return False

    def __dir__(self):
        return self.__dict__.keys()

    # 类似java中的toString()
    def __str__(self):
        return "This method name is: %s and param is: %s" % (self.name, self.param)

    # 类似java中setter
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    # 类似java中的getter
    def __getattr__(self, item):
        return self.__dict__[item]

    # 对象销毁的时候调用
    def __del__(self):
        print "object is deleting"
        

if __name__ == '__main__':
    m1 = MagicMethod("m1", "param1", 2)
    m2 = MagicMethod("m2", "param2", 2)
    m3 = MagicMethod("m3", "param3", 3)
    m4 = MagicMethod("m3", "param3", 3)
    print m1.__dict__

    add12 = m1 + m2
    print add12.name, add12.param, add12.num
    print m4 == m3
    # dir()是内阶函数，对应的是__dir__魔术方法，可以通过重写魔术方法来控制内阶函数的输出
    print dir(m1)
    print m1

    print m1.name, m1.param
