class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def print_info(self):
        print('%s:%s' %(self.name,self.__age))

xiaoming=Student('xiaoming',21)
xiaoqiang=Student('xiaoqiang',22)
xiaoming.print_info()
xiaoqiang.print_info()
xiaoming.father='daming'
print(xiaoming.father)
print(xiaoming.name)
# 私有的变量不能直接访问，但可以通过函数访问
print(xiaoming.__age)
# python编译器实际上把私有的_age变量改成了_Student__age形式，所以用_Student__age也能继续访问__age变量，
# 但是建议不要用，因为不同的python编译器可能改成不同到变量名
print(xiaoming._Student__age)

