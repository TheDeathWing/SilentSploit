import re
import time
import string
import requests as reqs
from silentsploit.core.modules import *
from silentsploit.utils import pprint_dict_in_order

class Exploit(Exploit):
    __info__ = {
       "Name": "IpLocate",
       "Description": "Geolocation using IP or HOST.\n"
                      "Get all available info about HOST or IP.",
       "Authors": ( 
                    "Mr-Z3r0" # Developer
                  ),
       "LastModified": "18-02-2020"
    }
    ip = OptHost("", "Target IP or host")
    api = OptString("http://ip-api.com/json/", "Api for requests")
    def run(self):
      if self.locate():
         print_success("Ip located")
         self.JSON = json.loads(self.locate().text)
         print("{RED}---------------------{END}".format(**colors))
         print("[{GREEN}!{END}] IP: {host}".format(host=self.ip, **colors))
         print("{RED}---------------------{END}".format(**colors))
         for line in self.JSON:
           print_status(line + ": " + str(self.JSON[line]))
         if "lon" in self.JSON and "lat" in self.JSON:
            print_status("Google Maps: http://www.google.com/maps/place/{0},{1}/@{0},{1},16z".format(self.JSON["lat"], self.JSON["lon"]))
      else:
        print_error("Error geolocationg IP: `%s`"%(self.ip))
    def locate(self):
      headers = "User-agent"
      response = reqs.get(
        url =  self.api + self.ip
      )
      return response
      time.sleep(.500) # Api ban you for 150 reqss per minute