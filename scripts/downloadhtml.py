#import nltk   
#from urllib import urlopen

#url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
#html = urlopen(url).read()    
#raw = nltk.clean_html(html)  
#print(raw)
import mechanize
import nltk
from bs4 import BeautifulSoup
from html2text import html2text 
import re


def clean_html(html):
    """
    Copied from NLTK package.
    Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """

    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()

url = "http://www.nytimes.com/2015/08/31/business/challenged-on-left-and-right-the-fed-faces-a-decision-on-rates.html"
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
html = br.open(url).read().decode('utf-8')
f = open("test/html.txt", "w")
f.write( unicode(html)  )      # str() converts to string
f.close()
cleanhtml = clean_html(html)
print cleanhtml
f = open("test/cleanhtml.txt", "w")
f.write( unicode(cleanhtml)  )      # str() converts to string
f.close()
text = html2text(cleanhtml)
f = open("test/text.txt", "w")
f.write( unicode(text)  )      # str() converts to string
f.close()
soup = BeautifulSoup(html)
f = open("test/soup.txt", "w")
f.write( unicode(soup)  )      # str() converts to string
f.close()
