import urllib3, re
import requests as reqs
from bs4 import *
from silentsploit.core.modules import *
from silentsploit.utils import pprint_dict_in_order

class Exploit(Exploit):
    __info__ =  {
       "Name": "PasteBin_Dumper",
       "Authors": (
                     "Mr-Z3r0" # Developer 
                  ),
       "Description": "PasteBin email dumper.\n"
                      "Dumps email using a keyword with pastebin",
       "Version": "1.0"
    }
    keyword = OptString("", "Set a key for search in pastebin")
    file = OptString("combolist.txt", "File to save output")
    def run(self):
       if self.check():
          print_status("Dumping..")
       else:
          print_error("Ups, can't execute dump")
    def check(self):
        url = "https://psbdmp.ws"
        params = {
          "string": self.keyword
        }
        html = reqs.post(url, data=params).text
        
        pastebin_regex = re.compile(r"^https://pastebin.com/[\w]+$")
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.findAll('a', attrs={"href": pastebin_regex}):
           links = link.get('href')
           for list in links.split("\n"):
             pastebin = reqs.get(list)
             soup = BeautifulSoup(pastebin.text, 'html.parser')
             for res in soup.find_all("li"):
               combos = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+:[a-zA-Z0-9._-]+')
               combos = combos.findall(res.text)
               if combos:
                 for list in combos[0].split("\n"):
                  try:
                    print(list)
                    f = open(self.file, 'a+')
                    f.write(list+"\n")
                    f.close()
                  except IOError:
                    print_error("Can't open file")