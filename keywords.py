from html.parser import HTMLParser
from urllib import request
from bs4 import BeautifulSoup

url = ('https://gcc.gnu.org/bugzilla/show_bug.cgi?id=90623')  #此处为待爬链接
response = request.urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')

tmp = soup.find_all('td',class_='field_value',attrs={'id':'field_container_keywords'})    #爬取keyword标签
tmp_string = str(tmp[0])                #将爬取的标签强制转换为字符串

tmp1 = tmp_string.split('>')[1]
tmp2 = tmp1.split('<')[0]
result = tmp2.rstrip('\n')                 #这三句只是对字符串的过滤，只保留keyword部分

url_number =url.split('=')[1].split('\'')[0]        #过滤出原本链接中的bug编号

keyword_outcome = 'Keyword: ' + result
print(keyword_outcome)
file = open("output.txt",'a')
file.write(url_number +'\n')
#file.write(url + '\n')
file.write(keyword_outcome+'\n')
file.close()