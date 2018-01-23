# coding=utf-8
def get_instance(obj):
    if isinstance(obj, Program):
        print obj.name
    else:
        print "error"


class Program(object):

    hobby = "Program an App"

    def __init__(self, name, age, weight, language):
        self.name = name
        self._age = age
        self.__weight = weight
        self.language = language

    # 静态方法
    @classmethod
    def get_hobby(cls):
        return cls.hobby

    # 将方法作为属性直接调用
    @property
    def get_weight(self):
        return self.__weight

    # 定义普通的方法
    def get_introduction(self):
        print "My name is: %s, I am %d years old, my weight is %f", self.name, self._age, self.__weight

    def get_age(self):
        return self._age


class JavaProgram(Program):

    def __init__(self, name, age, weight, language):
        super(JavaProgram, self).__init__(name, age, weight, language)

    def get_introduction(self):
        print "this is java program"


class PythonProgram(Program):

    def __init__(self, name, age, weight, language):
        super(PythonProgram, self).__init__(name, age, weight, language)

    def get_introduction(self):
        print "this is python program"


if __name__ == '__main__':
    # 属性访问
    p1 = Program("guoguo", 23, 53.0, "python")
    # 打印结果是一个对象
    print p1

    # 访问公开属性
    print p1.name

    # 访问私有的属性，可以正常访问，但是IDE会有警告，这种私有属性的定义方式没有语法约束，是一种公序良俗，应当遵守。
    print p1._age

    # __xxx这种私有属性是不能直接访问的
    # print p1.__weight

    # 方法访问
    # 访问静态方法：用对象访问
    print p1.get_hobby()

    # 访问静态方法：用类名访问
    print Program.get_hobby()

    # 访问属性方法，不用加括号，和访问属性的方式一样,但是方法不能带参数
    print p1.get_weight

    # Python中一切接对象，方法，属性都是对象，类名+方法名这种方式调用的是对象类型
    print Program.get_weight, Program.get_hobby(), Program.get_introduction

    # 继承
    java = JavaProgram("jack", 23, 55.0, "java")
    print "%s is a %s program whose age is: %d, weight is: %f" % (java.name, java.language, java.get_age(), java.get_weight)

    # 判断一个对象是不是一个类的实例
    print isinstance(java, Program)

    # 判断一个类是不是其他类的子类
    print issubclass(JavaProgram, Program)

    # 判断一个类的类型
    print type(java)

    get_instance(java)

    get_instance(PythonProgram("jams", 25, 55, "python"))


