#coding:utf-8
'''
冒泡排序
比较X轮
每一轮中，两两相比，大的放右边，执行一轮后，最大的在最右边
X轮后，完成排序
1.比较多少轮  2.每轮比多少次   与元素数量的关系
'''
def bull(a):
    for i in range(len(a)-1): #比较的轮数
        for j in range(len(a)-1-i): #每一轮比较的次数
            if a[j]>a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
    print(a)
#bull([9,6,3,12,4])
      
      
'''
2.选择排序
每个元素都与第一个元素进行比较，将小的放最左边
一轮过后最小的在最左边
执行X轮
'''  
def sel(a):
    for i in range(len(a)-1):
         #找到第i个元素  a[i] 当前这一轮的最左边的元素
         for j in range(i+1,len(a)):
             #让i+1个元素开始的后面每一个元素和i进行比较
             if a[j]<a[i]:
                 t = a[j]
                 a[j] = a[i]
                 a[i] = t
    print(a)
#sel([9,6,3,12,4,6])

'''
3.插入排序
把列表看做两个列表，一个是排好了序的，另一个是未排序的
每次从未排序列表中拿一个插入到排好了序的列表中
未排序:5
           len-1  
已排序:1 2 4 6 5   
'''
def ins(a):
    #循环的轮数
    for i in range(1,len(a)):   #找第一个要插入的数据     
        j = i-1 #j就是i的前一个元素
        t = a[i]
        while(j>=0 and a[j]>t):
            #把位置让给要插入的数据
            a[j+1] = a[j]
            a[j] = t
            j-=1
    print(a)
ins([9,6,3,12,4,6]) 
    
    