"""
正则表达式
    概述：正确的，符合特定规则的字符串，用来处理文本信息的工具
    步骤:1.导包
            import re
        2.正则匹配
        result = re.match(正则表达式,字符串)#从左到右匹配，匹配成功返回匹配对象，匹配失败返回None,核心机制:只匹配到符合条件的就行
        result = re.search(正则表达式,字符串)#片段查找
        result = re.compile(正则表达式).sub(替换字符串,原字符串)#编译正则表达式，返回正则对象    替换
        3.获取匹配结果
        result.group()  #获取匹配结果
        4.判断是否匹配成功

正则常用规则
    r. : 匹配任意字符
    \.取消.的特殊含义，匹配点本身
    [abc]:abc中的任意字符
    [^abc] : 非abc的字符
    \d:代表数字0~9,等价[0~9]
    \D:代表非数字
    \s:代表空白字符即[\t\n\r]
    \S:代表非空白字符
    \w:代表非特殊字符,即数字,大小写字母,下划线，汉字 等价[0~9a~zA~Z_汉字]
    \w:代表特殊字符，与\w相对

    *:前面内容至少出现0次,至多无限
    ?:前面内容至少出现0次,至多1次
    +:前面内容至少出现1次,至多无数次
    {n}:前面内容恰好出现n次
    {n,}:前面内容至少出现n次m,至多无数次
    {n,m}:至少出现n次,
    
    ^:表示开头
    $:表示结尾

    |:匹配左右任意表达式
    (ab):将括号中字符作为一个分组
    \num:引用分组num匹配的字符串
    """


import re

# #规则匹配
# result = re.match(".it","你it")
# result = re.match(".it","你haoit")
# result = re.match("[abc]it","cit")


# #字符串替换
# s="hello  world"
# result = re.compile("hello").sub("你好",s)
# print(result)


# #多个字符串匹配
# result = re.match(".*hm.*","abchm123") #匹配成功

# result = re.match(".+hm.*","abchm123") #匹配成功
# result = re.match(".+hm.*","hm123") #匹配失败

# result = re.match(".?hm.*","hm123") #匹配成功
# result = re.match(".?hm.*","ahm123") #匹配成功
# result = re.match(".?hm.*","abchm123") #匹配失败

# result = re.match("\d{3,}hm\w{2,5}","123hm123") #匹配成功
# result = re.match("\d{3,}hm\w{2,5}","123hm123567") #匹配成功
# result = re.match("\d{3,}hm\w{2,5}","12hm123567") #匹配失败


result = re.search(r"^\d.*","12345hm")#成功
result = re.search(r"^\d.*[a-zA-Z]{3}$","12345acn")#成功

#手机号校验
#必须以1开头，第二位3-9，长度为11位
result = re.match("^1[3-9]\d{9}$","13325555744")
result = re.match("^1[3-9]\d{9}$","12325555744")

fruits = ["apple","peer","strawberry","banana"]
for i in fruits:
    if re.match("apple|peer",i):
        print(i)


# if result:
#     print(result.group())
# else:
#     print("匹配失败")