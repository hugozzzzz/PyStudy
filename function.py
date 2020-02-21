def fun(x):
    if(x>=0):
        return x
    else:
        return -x
print(fun(- 9))
# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(10))