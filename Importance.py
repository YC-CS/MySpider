from html.parser import HTMLParser
from urllib import request
from bs4 import BeautifulSoup

url = ('https://gcc.gnu.org/bugzilla/show_bug.cgi?id=103991')  #此处为待爬链接
response = request.urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')

tmp = soup.find('td',text=True)

print(tmp)