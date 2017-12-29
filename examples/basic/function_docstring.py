def print_max(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大值。

    The two values must be integers.这两个数应该是整数'''
    
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
    
print_max(3, 5)

# 使用函数的 __doc__ 属性来获取 print_max 的文档字符串属性。 
print(print_max.__doc__)

# help() 函数能获取函数的 __doc__ 属性，使用 q 键来退出 help
help(print_max)