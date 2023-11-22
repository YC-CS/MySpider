from html.parser import HTMLParser
from urllib import request
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == ('a') and ('class','list') in attrs:
            tuple = attrs[1]
            if 'gcc/cp/' in tuple[1] :
                tmp = tuple[1].split('f=')[1]
                outcome = 'code: '+ tmp.split(';')[0]
                print(outcome)
                file = open("Tree_output.txt", 'a')
                file.write(url + '\n')
                file.write(outcome +'\n')
                file.close()

parser = MyHTMLParser()

def TreeSpider(str = url):
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    parser.feed(html)



f = open("Tree_input.txt", "r")                  # Tree_input中逐行填写http地址
list = f.read().splitlines()
f.close()

for url in list:
    keyword = TreeSpider(url)
    number = url.split('=')[1].split('\'')[0]  # 过滤出原本链接中的bug编号
    print(number)
    print(keyword)
    write_file(number, keyword)
