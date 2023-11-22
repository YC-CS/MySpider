from html.parser import HTMLParser
from urllib import request
# f = open(r'Keyword_input.txt','r')
# a = list(f)
# print(a)
# f.close()
f = open("Keyword_input.txt", "r")
list = f.read().splitlines()
print(list)
f.close()