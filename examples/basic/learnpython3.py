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
a = [1, 2, 3, 4]    #  a 指向一个新的列表，[1, 2, 3, 4]
b = a               #  b 指向的是 a 所指向的
b is a              # => True，a 和 b 所关联的是同一个对象
b == a              # => True，a 指向的的对象和 b 指向的对象是相等的
b = [1, 2, 3, 4]    #  b 指向一个新的列表，[1, 2, 3, 4]
b is a              # => False，a 和 b 关联的不是同一个对象
b == a              # => True，a 指向的对象和 b 指向的对象的值是相等的。

# 字符串用双引号（"）或者单引号（'）来创建
"This is a string."
'This is alse a string.'

# 字符串也能够相加，但是最好不要这样做
"Hello" + "world!"  # => "Hello world!"
# 字符串表达式（非变量）能够不使用加号（+）直接拼接
"Hello" "world"     # => "Hello world"

# 字符串能够被当作是一个列表的元素
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

# None，0，空字符串，空列表，空字典，空元组都判定为 False
# 其他的值都是 True
bool(0)   # => False
bool("")  # => False
bool([])  # => False
bool({})  # => False
bool(())  # => False

####################################################
## 2. 变量和集合
####################################################

# Python 有一个用于打印的 print 函数
print("I'm Python. Nice to meet you!")      # => I'm Python. Nice to meet you!

# 默认情况下，print 函数会在输出结束时换行（就是在结尾多输出了一个换行符）
# 可以使用可选参数 end 来改变字符串的结尾，意思就是之前结束的时候是在末尾加了个换行符，现在可以使用 end 参数来改变这个换行符
print("Hello, World", end="!")      # => Hello, World!

# 从控制台获取输入数据的一个简单方式
input_string_var = input("Enter some data: ")   # 将数据作为字符串返回
# 注意：在早期版本的 Python 中，input() 方法被命名为 raw_input()

# 不用声明就可以给变量赋值
# 按照惯例变量使用小写加下划线拼接的形式书写
some_var = 5
some_var    # => 5

# 访问未赋值的变量会发生异常
# 参见下一节《控制流》来学习更多关于异常的处理
some_unknown_var    # 抛出命名错误异常

# if 可以用作表达式来使用
# 相当于 C 语言的三元运算符 "?:"
"yahoo!" if 3 > 2 else 2    # => "yahoo!", 类似于 3 > 2 ? "yahoo!" : 2

# 列表用于存储序列
li = []
# 也可以使用一个预先填充好的列表
other_li = [4, 5, 6]

# 可以在列表末尾添加元素
li.append(1)    # li 变为 [1] 
li.append(2)    # li 变为 [1, 2] 
li.append(4)    # li 变为 [1, 2, 4] 
li.append(3)    # li 变为 [1, 2, 4, 3]
# 使用 pop() 方法可以将列表最末位元素移除,并返回被移除的元素
li.pop()        # => 3, 此时 li 变为 [1, 2, 4]
# 将 3 放回列表
li.append(3)    #  li 又变回 [1, 2, 4, 3]

# 可以像其他语言访问数组一样访问一个列表
li[0]   # => 1
# 获取最末位元素
li[-1]  # => 3

# 越界查询会发生索引错误
li[4]   # => 抛出索引错误

# 可以使用切片语法来查询列表的范围
# 起始索引是包含起始位置的元素的，结束索引没有包含结束位置的元素
# 像数学中的开闭区间一样
# li[start:stop:step], start 是起始索引；stop 是结束索引；step 是要间隔的位数，1 就表示正向隔一个数取一，-2 就表示从列表最末位开始反向隔两位取一
li[1:3]     # => [2, 4]
# 省略结尾,就从起始索引位一直到列表末位
li[2:]      # => [4, 3]
# 省略开头，就从列表首位开始到结束索引前一位元素
li[:3]      # => [1, 2, 4]
# 每隔两位取一个
li[::2]     # => [1, 4]
# 将列表从末尾开始反向隔一位取一
li[::-1]    # => [3, 4, 2, 1]

# 使用切片可以进行深拷贝
li2 = li[:] # => li2 = [1, 2, 4, 3]，但是（li2 is li）返回 False，（li2 == li）返回的是 True

# 使用 del 可以移除列表的任意元素
del li[2]   # li 变为 [1, 2, 3]

# 移除第一个出现的与参数一样的值
li.remove(2)    # li 变为 [1, 3]
li.remove(2)    # 抛出 2 不在列表中的 ValueError 错误

# 在指定索引位置插入元素
li.insert(1, 2) # => li 又变回 [1, 2, 3]

# 获取第一个与指定参数匹配的元素的索引
li.index(2)     # => 1
li.index(4)     # 抛出 4 不在列表中的 ValueError 错误 

# 列表可以相加
# 注意：li 和 other_li 不会被修改
li + other_li   # => [1, 2, 3, 4, 5, 6]

# 使用 extend() 扩展合并列表
li.extend(other_li)     # li 现在是 [1, 2, 3, 4, 5, 6]

# 使用 in 来检查一个元素是否存在于一个列表中
1 in li     # => True

# 使用 len() 来检测列表的长度
len(li)     # => 6

# 元组和列表很相似，但是是不可变的
tup = (1, 2, 3)
tup[0]          # => 1
tup[0] = 3      # 抛出 TypeError（类型错误） 异常

# 注意：长度为 1 的元组应该在元组的最后一位元素后加上一个逗号，但是长度不为 1 的元组不应该在末位元素后面加逗号，即使是长度为 0 的也不要加
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# 使用在列表上的大多数操作也都是可以使用在元组上的
len(tup)            # => 3
tup + (4, 5, 6)     # => (1, 2, 3, 4, 5, 6)
tup[:2]             # => (1, 2)
2 in tup            # => True

# 可以把元组（或列表）中的元素取出来赋值给多个变量
a, b, c = (1, 2, 3) # a 现在是 1，b 是 2，c 是 3