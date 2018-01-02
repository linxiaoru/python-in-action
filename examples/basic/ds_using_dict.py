# 只能使用不可变的对象（如字符串）作为字典的键值，但是可以使用可变或不可变的对象作为字典中的值。
# 形式 d = {key : value1, key2 : value2}
# 字典中的成对的键值-值对不会以任何方式进行排序，要排序只能在使用它们之前自行进行排序

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值-值配对
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一对键值-值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])