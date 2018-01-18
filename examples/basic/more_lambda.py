"""
lambda 语句可以创建一个新的函数对象。
lambda 需要一个参数，后面跟一个表达式作为函数体，这一表达式执行的值将作为这个新函数的返回值。
"""

points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

# sort 方法可以获得一个 key 参数，泳衣决定列表的排序方式