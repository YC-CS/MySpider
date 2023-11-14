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
                file = open("output.txt",'a')
                file.write(url + '\n')
                file.write(outcome+'\n')
                file.close()

parser = MyHTMLParser()

url = 'https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=aeca44768d54b089243004d1ef00d34dfa9f6530'
response = request.urlopen(url)
html = response.read().decode('utf-8')
parser.feed(html)