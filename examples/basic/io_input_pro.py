"""
要想检查文本是否属于回文需要忽略其中的标点、空格与大小写。例如，“Rise to vote, sir.”是一段回文文本
"""

forbidden = (' ', '.', '“', '”', '，', ',')

def fillter_forbidden_text(text):
    text_copy = text.lower()
    for single_text in text:
        if single_text in forbidden:
            text_copy = text_copy.replace(single_text, '')
    return text_copy

# 使用切片进行翻转
def reverse(text):
    return text[::-1]

# 判断是否是回文
def is_palindrome(text):
    format_text = fillter_forbidden_text(text)
    return format_text == reverse(format_text)

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")