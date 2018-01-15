# 使用切片进行翻转
def reverse(text):
    return text[::-1]

# 判断是否是回文
def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")