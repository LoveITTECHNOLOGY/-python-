#coding:utf-8
'''
递归调用：自己调用自己
将复杂的过程逐步简化
'''
#求1-100的和
def suma(n):
    if n==0:
        return 0
    else:
        return n+suma(n-1)
#print(suma(100))
'''
斐波那契数列：
兔子生兔子问题：
有一对兔子，第三月开始每个月会生一对兔子，
新兔子第三个月开始也会生一对兔子
问X月时有多少对兔子
1  1                             1
2  1                             1
3  1+1                           2
4  1+1 +1                        3
5  1+1 +1 +1 +1                  5
6  1+1 +1 +1 +1 +1 +1 +1         8 
X  多少对
'''
def rab(n):
    if n==1 or n==2:
        return 1
    else:
        return rab(n-1)+rab(n-2)
#print('第13个月有',rab(13),'对兔子。')

'''
          12 4 7 88 1 25 24  16    9   44
    12  4  7  1  24 16 9      25         99 44
  12 4 7 1 16 9    24       25    44   99
    1 4     7  9     12 16
     1   4 7   9     12 16  25    44   99
'''
def fast(a):
    if len(a)>=2:
        mid = a[len(a)//2]  #找基准数
        left,right=[],[]  #定义左右两边的列表
        a.remove(mid)  #移除mid
        for num in a:
            if num<mid:
                left.append(num)
            else:
                right.append(num)
        return fast(left) + [mid] + fast(right)
    else:
        return a
print(fast([9,6,3,12,4,6]))





