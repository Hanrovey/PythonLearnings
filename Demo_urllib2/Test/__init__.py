#coding:utf8

import urllib2
from Cookie import Cookie
import cookielib

url = "http://www.baidu.com"

print '第一种方法'
#直接请求
response1 = urllib2.urlopen(url, None, 10, None, None, None, None)
#获取状态码 如果是200，表示成功
print response1.getcode()
#读取内容获取长度
print len(response1.read())
     
                              
print "第二种方法"  
#创建request对象
request = urllib2.Request(url)
#添加http的头
request.add_header("user-agent","Mozilla/5.0") 
#发送请求获取数据    
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())


print '第三种方法'
#创建cookie容器
cj = cookielib.CookieJar()
#创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#给urllib2安装opener
urllib2.install_opener(opener)
#使用带有cookie的urllib2访问网页
response3 = urllib2.urlopen(url, None, 10, None, None, None, None)
print response3.getcode()
print cj
print response3.read()
















                                                