list=['11','22','33']
print(list[-1],'索引数目=',len(list))
sum=0
n=0
while n<100:
    n=n+1 
    if n%2==0:
        continue
    if n>10:
        break
    print(n)
    
print(n)
# 十进制转换为16进制
print(hex(1000))