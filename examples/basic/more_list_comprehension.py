# 列表推导

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

"""
使用列表推导的优点在于，当我们使用循环来处理列表中的每个元素并将其存储到新的列表中时，
它能减少样板代码的数量。
"""