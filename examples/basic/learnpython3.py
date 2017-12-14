# 译自 https://learnxinyminutes.com/docs/python3/，对内容有进行修改，加入了自己的理解和补充。

# 单行注释用井号（#）开头。

""" 多行注释用三个双引号（""）包裹，
    通常，三个双引号中要换行可以直接换，
    不需要加换行符切割，可以用作多行字符串，
    并且可以在三个双引号中添加注释。
"""

####################################################
# 1. 基本数据类型和运算符
####################################################

# 数字
3  # => 3

# 数学运算
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

""" 整除法用（//），两个整型相除，得到的还是整型。
    但是,如果一个浮点数除以一个非浮点数得到的还会是一个浮点数，
    并且，计算的结果却是忽略小数部分，运算的结果类似两个整型相除，但是得到一个浮点数。
"""
5 // 3       # => 1
5.0 // 3.0   # => 1.0
-5 // 3      # => -2 同样适用于负数
-5.0 // 3.0  # => 1

# 单斜杠（/）除法即为 float 除法，得到的商会返回为浮点数形式
10.0 / 3    # => 3.3333333333333335

# 模除（求余）
7 % 3   # => 1

# 指数运算
2**3    # => 8

# 使用小括号提升运算的优先级
(1 + 3) * 2  # => 8

# 布尔值也是基本数据类型（注意大写）
True
False

# 加 not 取反
not True    # => False
not False   # => Ture

# 布尔运算符
# 注意（and）和（or）是大小写敏感的
True and False  # => False
False or True   # => True

# 注意使用布尔运算符时要用整型
# False 是 0，True 是 1。这里和 JS 很不一样，JS 里 0 是 false，其他的数字都是 true
# 不要混用布尔类型（整型）和位运算符 and/or（&，|）
0 and 2                 # => 0
-5 or 0                 # => -5
0 == False              # => True
2 == True               # => False
1 == True               # => True
-5 != False != True     # => True

# 判断是否相等用 ==
1 == 1  # => True
2 == 1  # => False

# 判断不等用 !=
1 != 1  # => False
2 != 1  # => True

# 比较判断
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# 比较判断可以链式判断
1 < 2 < 3   # => True
2 < 3 < 2   # => False

# is 和 ==
# is 检查两个变量是否关联的是同一个对象，但是 == 检查的是对象是否指向同样的值
a = [1, 2, 3, 4]    #  a 指向一个新的数组，[1, 2, 3, 4]
b = a               #  b 指向的是 a 所指向的
b is a              # => True，a 和 b 所关联的是同一个对象
b == a              # => True，a 指向的的对象和 b 指向的对象是相等的
b = [1, 2, 3, 4]    #  b 指向一个新的数组，[1, 2, 3, 4]
b is a              # => False，a 和 b 关联的不是同一个对象
b == a              # => True，a 指向的对象和 b 指向的对象的值是相等的。

# 字符串用双引号（"）或者单引号（'）来创建
"This is a string."
'This is alse a string.'

# 字符串也能够相加，但是最好不要这样做
"Hello" + "world!"  # => "Hello world!"
# 字符串表达式（非变量）能够不使用加号（+）直接拼接
"Hello" "world"     # => "Hello world"

# 字符串能够被当作是一个数组的元素
"This is a string"[0]   # => 'T'

# 可以使用 len() 函数来获取字符串的长度
len("This is a string")     # => 16

# 可以使用 .format 来格式化字符串
"{} can be {}".format("Strings", "interpolated")    # => "Strings can be interpolated"

# 可以重复使用格式化参数来减少重复的输入
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"

# 如果不想去数参数，可以使用关键字来代替。就是说上例中的 {0} 代表的是 .format() 的第一个参数，{1} 是第二个参数
"{name} wants to eat {food}".format(name="Bob", food="lasagna")     # => "Bob wants to eat lasagna"

# 如果你的 Python 3 代码也需要运行在 Python 2.5 及以下版本中，可以使用旧的格式化形式
"%s can be %s the %s way" % ("Strings", "interpolated", "old")      # => "Strings can be interpolated the old way"

# None 是一个对象
None    # => None

# 不要使用相等判断号（==）来比较对象和 None
# 使用 is 来代替。这个能够检查对象的值是否相等
"etc" is None   # => False
None is None   # => True

# None，0，空字符串，空数组，空字典，空元组都判定为 False
# 其他的值都是 True
bool(0)   # => False
bool("")  # => False
bool([])  # => False
bool({})  # => False
bool(())  # => False