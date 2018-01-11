"""
 类变量是共享的--它们可以被属于该类的所有实例访问。
 该类变量只有一个副本，当任何一个对象对类变量做出改变时，发生的变动将在其它所有示例中都会得到体现。

 对象变量由类的每一个独立的对象或实例所拥有。在这种情况下，每个对象都拥有属于它自己的字段的副本，也就是说，它们不会被共享，
 也不会以任何方式与其它不同实例中的相同名称的字段产生关联。
 """

 # coding=UTF-8

class Robot:
     # 表示有一个带有名字的机器人。

     # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        # 初始化数据
        self.name = name
        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人将会增加人口数量
        Robot.population += 1
    
    def die(self):
        # 挂了
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        # 来自机器人的问候
        print("Greetings, my masters call me {}".format(self.name))
    
    @classmethod  # 启用 @classmethod 装饰器等价于调用：how_many = classmethod(how_many)
    def how_many(cls):
        # 打印出当前的人口数量
        print("We have {:d} robots.".format(cls.population))



droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

"""
population 属于 Robot 类，因此它是一个类变量。name 变量属于一个对象（通过使用 self 分配），因此它是一个对象变量。
当一个对象变量与一个类变量名称相同时，类变量将会被隐藏。
除了 Robot.popluation，我们还可以使用 self.__class__.population，因为每个对象都通过 self.__class__ 属性来引用它的类。
"""