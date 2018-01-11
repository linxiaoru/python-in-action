# 类与对象一如函数那般都可以带有方法，唯一不同的地方在于类还有一个额外的 self 变量。

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()

# 也可并作 Person().say_hi()