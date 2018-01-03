name = 'Swaroop'

# startwith 方法用于查找字符串是否以给定的字符串内容开头。
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

# in 运算符用以检查给定的字符串是否是查询的字符串中的一部分。
if 'a' in name:
    print('Yes, it contains the string "a"')

# find 方法用于定位字符串中给定的子字符串的位置。如果找不到相应的子字符串， find 会返回 -1。
if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
# join 用以联结序列中的项目，其中字符串将会作为每一项目之间的分隔符，并以此生成并返回一串更大的字符串。
print(delimiter.join(mylist))