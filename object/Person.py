# coding=utf-8
from msilib.schema import Property


class Person(object):
    # 这里定义的成员变量可以用类名直接调用，是属于类的属性，所有该类的对象都可以使用
    gender = "boy"

    def __init__(self, name, age):
        # 这里定义的成员变量是跟类的对象绑定的，只有该类的对象可以调用
        self.name = name
        self.age = age

    # @classmethod类似java中的static
    @classmethod
    def get_gender(cls):
        return cls.gender

    @property
    def get_age(self):
        return self.gender


if __name__ == '__main__':
    p1 = Person('zhangsan', 23)
    p2 = Person('lisi', 24)
    # 在Python中没有强制数据类型， 一个变量可以赋给任何类型
    p1.name = 1212
    p2.age = "hello"
    print p1.name, p1.age, p1.gender
    print p2.name, p2.age, p2.gender
    print Person.gender
    print p1.get_gender()
    print Person.get_age
