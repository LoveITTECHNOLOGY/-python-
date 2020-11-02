#coding:utf-8
#要复制文件，那就是读(复制)写(粘贴)操作
f = open('鸣人.jpg','rb')
for i in range(4):
    f.seek(0)
    f1 = open('../鸣人影分身'+str(i)+'.jpg','wb')
    f1.write(f.read())
    f1.close()
f.close()
