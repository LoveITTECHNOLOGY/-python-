#coding:utf-8
class TestCounter:
    publicCount = 0 #公开的变量
    __sercretCount = 0 #私有的变量
    def count(self):
        self.__sercretCount+=1
        self.publicCount+=1
        print('私有变量的值为:%d' %self.__sercretCount)
c1 = TestCounter()
c1.count()
c1.count()
print('公开的变量为:%d' %c1.publicCount)
#print('私有的变量为:%d' %c1.__sercretCount)
#私有变量可以通过 对象名._类名__属性名 访问
print('私有的变量为:%d' %c1._TestCounter__sercretCount)



