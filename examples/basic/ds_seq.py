# 序列的主要功能是资格测试（Membership Test）（也就是 in 与 not in 表达式）和索引操作（Indexing Operations），它们能够允许我们直接获取序列中的特定项目。

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation
# 索引或“下标”操作符
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

"""
切片操作可提供三个参数，第一个起始位置，第二个结束位置（不包括该位置上的参数），
第三个间隔在切片操作中，第一个数字（冒号前面的那位）指的是切片开始的位置，
第二个数字（冒号后面的那位）指的是切片结束的位置。如果第一位数字没有指定，
Python 将会从序列的起始处开始操作。如果第二个数字留空，Python 将会在序列的末尾结束操作。
要注意的是切片操作会在开始处返回 start，并在 end 前面的位置结束工作。
也就是说，序列切片将包括起始位置，但不包括结束位置。
第三个参数，这一参数将被视为切片的步长（Step）（在默认情况下，步长大小为 1）
"""