from urllib.parse import ParseResult

key=input("请输出一个字符：")
def aa(key):
    if key is None:
        print("key是一个none值")
        return []
    else:
        print("key不为空")
        return type(key)
a=aa(key)
print(a)

