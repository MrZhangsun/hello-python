# coding=utf-8
class InstanceObject(object):

    # 创建对象的时候首先是执行该方法，返回一个该类的实例对象
    def __new__(cls, *args, **kwargs):
        print "new is running"
        return super(InstanceObject, cls).__new__(cls)

    # 执行完__new__之后执行__init__方法
    def __init__(self, name):
        self.name = name
        print "init is running"


if __name__ == '__main__':
    obj = InstanceObject("new object")
    # 查看对象的所有属性值
    print obj.__dict__
