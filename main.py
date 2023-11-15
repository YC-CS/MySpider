from html.parser import HTMLParser
from urllib import request
# f = open(r'income.txt','r')
# a = list(f)
# print(a)
# f.close()
f = open("income.txt", "r")
list = f.read().splitlines()
print(list)
f.close()