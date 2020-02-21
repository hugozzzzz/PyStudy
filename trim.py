# 去除首尾空格到函数方法
b=' string '
def clear(n):
    if n[0]==' ':
        print("yes")
        return b[1:]
    if n[-1]==' ':
        print("yes")
        return b[:-1]
print(clear(b))