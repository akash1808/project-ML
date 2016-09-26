import urllib
from bs4 import BeautifulSoup
import mechanize
import nltk
import re
#url = "https://www.yahoo.com"
#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)

# kill all script and style elements
#for script in soup(["script", "style"]):
#    script.extract()    # rip it out


# get text
#text = soup.get_text()

# break into lines and remove leading and trailing space on each
#lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
#chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
#text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text.encode('utf-8'))


#html = urllib.urlopen("https://blog.codeship.com/visualizing-algorithms-implementation/").read()
url = "http://www.news18.com/news/india/india-will-ratify-cop21-on-october-2-narendra-modi-1295641.html"
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
html = br.open(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
texts = soup.findAll(text=True)
titleTag = soup.html.head.title
print titleTag.string
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', unicode(element)):
        return False
    return True

#visible_texts = filter(visible, texts)
#print(visible_texts)

