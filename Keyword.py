from html.parser import HTMLParser
from urllib import request
from bs4 import BeautifulSoup


def spider(income = str):

    response = request.urlopen(income)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    tmp = soup.find_all('td', class_='field_value', attrs={'id': 'field_container_keywords'})  # 爬取keyword标签

    tmp_string = str(tmp[0])                         # 将爬取的标签强制转换为字符串
    tmp1 = tmp_string.split('>')[1]
    tmp2 = tmp1.split('<')[0]
    result = tmp2.rstrip('\n')                       # 这三句只是对字符串的过滤，只保留keyword部分
    outcome = 'Keyword: ' + result
    return outcome


def write_file(income1 = str,income2 = str):
    file = open("Keyword_output.txt", 'a')
    file.write(income1 + '\n')
    file.write(income2 + '\n')
    file.close()

f = open("Keyword_input.txt", "r")                   # Keyword_input中逐行填写bug的编号
list = f.read().splitlines()
f.close()


for bug_number in list:
    url = 'https://gcc.gnu.org/bugzilla/show_bug.cgi?id=' + bug_number
    keyword = spider(url)
    number = url.split('=')[1].split('\'')[0]        # 过滤出原本链接中的bug编号
    print(number)
    print(keyword)
    write_file(number, keyword)
