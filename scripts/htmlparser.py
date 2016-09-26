from flask import Flask
from flask import json
from flask import request
from lxml import html
import subprocess
import shlex
import sys
import os
import json
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

def fileparse(filepath):
    #print request.headers
    #data=json.dumps(request.json)
    #print data
    #print request
    inputfile = open(filepath)
    my_text = inputfile.readlines();
#    print my_text
    #msg= request.json["msg"]
    #tree = html.fromstring(msg.content)
    parser = MyHTMLParser()
        
    parser.feed(my_text[0])
#    print parser.data
    #return parser.data


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr

    def handle_endtag(self, tag):
        print "End tag  :", tag

    def handle_data(self, data):
        print "Data     :", data

    def handle_comment(self, data):
        print "Comment  :", data

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c

    def handle_decl(self, data):
        print "Decl     :", data


class MyHTMLParser2(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0 
    self.noteinfo = 0
    self.data = []
    self.counter = 0;
  def handle_starttag(self, tag, attrs):
    if tag == 'p':
      self.recording = 1
      self.counter += self.counter
    if tag == 'title':
      self.noteinfo = 1


  def handle_endtag(self, tag):
    if tag == 'div' or tag == 'title':
      # self.recording =0 
       self.noteinfo = 0;
       print "Encountered the end of a %s tag" % tag 

  def handle_data(self, data):
    
    if self.recording:
      print data
      item = {"id": self.counter, "value": data}
      self.data.append(item)


if __name__ == "__main__":
   value = fileparse(sys.argv[1])
