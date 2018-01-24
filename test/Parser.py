# coding=utf-8
import re
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding="utf-8")
nodes = soup.find_all('a')
print "方式一：获取所有的a标签"
for node in nodes:
    print node.name, node['href'], node.get_text()

print "方式二：正则匹配"

res = soup.find_all("a", href=re.compile("till"))
for re in res:
    print re.name, re['href'], re.get_text()

print "方式三：根据属性匹配"
attr = soup.find("a", href="http://example.com/elsie")
print attr.name, attr["href"], attr.get_text()

print "方式四：根据class匹配"
classes = soup.find_all("p", class_="story")
for class_ in classes:
    print class_.name, class_.get_text()