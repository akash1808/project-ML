from flask import Flask
from flask import json
from flask import request
from lxml import html
import subprocess
import shlex
import os
import json
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
app = Flask(__name__)

@app.route('/query', methods=['POST'])
def get_docIds():
    print request.headers
    data=json.dumps(request.json)
    #print data
    #print request
    query= request.json["query"]
    return query

def run_command(cmd):
    cmd = shlex.split(cmd)
    return subprocess.check_output(cmd).decode('ascii')

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
    if tag == 'div':
      for name, value in attrs:
        if name == 'class' and value == 'PIAeditable PIAcontent':
          print name, value
          print "Encountered the beginning of a %s tag" % tag 
          self.recording = 1
          self.counter +=1 
    if tag == 'title':
      self.noteinfo = 1


  def handle_endtag(self, tag):
    if tag == 'div' or tag == 'title':
       self.recording =0 
       self.noteinfo = 0;
       print "Encountered the end of a %s tag" % tag 

  def handle_data(self, data):
    
    if self.recording:
      item = {"id": self.counter, "value": data}
      self.data.append(item)
    if self.noteinfo:
      item = {"title" : data}
      self.data.append(item)


if __name__ == "__main__":
    app.run('0.0.0.0')


