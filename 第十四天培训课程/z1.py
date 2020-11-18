#coding:utf-8
import re 
'''
匹配的模式字符串使用特殊的语法来表示正则表达式
大部分的字母加上\代表不同的意思
标点符号只有加上了\才表示本身的符号，否则都有含义
要得到反斜杠？？？  r'\\'
'''
#  ^ 查找以某些字符开头的字符串
print(re.search((r'^ab'),'aabcdefg'))
#  $ 查找以某些字符结尾的字符串
print(re.search((r'@qq.com$'),'12345@qq.com'))
#  . 匹配任意字符
print(re.search((r'.de'),'ab34cd!@#$defg'))
#  []匹配中括号中的字符 [abc] 匹配a或b或c
print(re.search((r'[Pp]ython'),'python'))
#  [^]  匹配除了中括号中的字符 ，上面的反向取
print(re.search((r'[^Pp]ython'),'aython'))
#出现次数的规则
#   * 表示*前面的字符出现任意次数
print('------------')
print(re.search((r'ca*b'),'caaab'))
#   + 表示+前面的字符至少出现一次
print(re.search((r'ca+b'),'caaaaab'))
#   ? 表示?前面的字符至多出现一次
print(re.search((r'ca?b'),'cab'))
#   {m} 表示{m}前面的字符只能出现m次
print(re.search((r'ca{2}b'),'caaab'))
#   {m,n} 表示{m,n}前面的字符出现的次数在[m,n]之间
print(re.search((r'ca{2,4}b'),'caaaab'))
'''
贪婪模式：在表达式符合规则的情况下,尽可能多的去匹配,默认是贪婪模式
          ab+   ab   abbbbbb
非贪婪模式：在表达式符合规则的情况下,尽可能少的去匹配
                     在规则字符串最后加?  表示非贪婪模式
          ab+?   ab   abbbbbb
'''
print('-------')
print(re.search((r'ab+'),'abbbbbbbbb'))
print(re.search((r'ab+?'),'abbbbbbbbb'))
'''
匹配的字符串 :  r'ab(cd)ab'   匹配abcdab字符串 但是只获取cd
小括号代表要获取的字符串
'''
print(re.findall(r'a(.*)a','123abacdabsdgdsa1212'))
'''
要找   xx.img   xx.png
使用     表达式A|表达式B   
表示匹配  表达式A或者表达式B
'''
print(re.search(r'.*img|.*png','adf.png'))