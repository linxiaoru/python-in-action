def binary_search(list, item):
    low = 0                     # low 和 high 用于跟踪要在其中查找的列表部分
    high = len(list) - 1

    while low <= high:          # 只要范围没有缩小到只包含一个元素，就检查中间的元素
        mid = (low + high)
        guess = list[mid]
        if guess == item:       # 找到了元素
            return mid
        if guess > item:        # 猜的大了
            high = mid - 1
        else:                   # 猜的小了
            low = mid + 1       
    return None                 # 没有指定的元素

mylist = [1, 3, 5, 7, 9]

print (binary_search(mylist, 3))  # => 1
print (binary_search(mylist, -1))  # => None