import re
import time
import string
import requests as reqs
from silentsploit.core.modules import *
from silentsploit.utils import pprint_dict_in_order

class Exploit(Exploit):
   __info__ = {
       "Name": "4Hash",
       "Description": "Hash Cracker. For all hash.\n"
                      "Detect and crack hash using wordlists.",
       "Authors": (
                     "Mr-Z3r0" # Developer and creator
                  ),
       "Version": "1.0"
   }
   hash = OptString("", "Hash for crack. Set a valid hash")
   wordlist = OptFile("", "Enter your wordlist of passwords")
   def run(self):
      if self.check():
        print(self.check())
      else:
        pass
   def check(self):
      print_info("Possible Hash: ")
      print_success("{type} - ({hash})".format(type=self.detect(), hash=self.hash))
   def detect(self):
      SHA512= ('dd0ada8693250b31d9f44f3ec2d4a106003a6ce67eaa92e384b356d1b4ef6d66a818d47c1f3a2c6e8a9a9b9bdbd28d485e06161ccd0f528c8bbb5541c3fef36f')
      md = ('ae11fd697ec92c7c98de3fac23aba525')
      sha1 = ('4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333')
      sha224 = ('e301f414993d5ec2bd1d780688d37fe41512f8b57f6923d054ef8e59')
      sha384 = ('3b21c44f8d830fa55ee9328a7713c6aad548fe6d7a4a438723a0da67c48c485220081a2fbc3e8c17fd9bd65f8d4b4e6b')
      sha256 = ('2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e')
      mysql1323 = ("5d2e19393cc5ef67")
      mysql41 = ("*88166B019A3144C579AC4A7131BCC3AD6FF61DA6")
      mssql2000 = ("0x0100DE9B3306258B37432CAC3A6FB7C638946FA393E09C9CBC0FA8C6E03B803390B1C3E7FB112A21B2304595D490")
      mssql2005 = ('0x01008110620C7BD03A38A28A3D1D032059AE9F2F94F3B74397F8')
      
      if len(self.hash)==len(mysql1323) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
          hash = "mysql1323"
      elif len(self.hash)==len(mysql41) and "*" in hash_str:
          hash = "mysql41"
      elif len(self.hash)==len(mssql2000) and "0x0" in hash_str:
          hash = "mssql2000"
      elif len(self.hash)==len(mssql2005) and "0x0" in hash_str:
          hash = "mssql2005"
      elif len(self.hash)==len(sha1):
          hash = "sha1"
      elif len(self.hash)==len(SHA512):
          hash = "SHA512"
      elif len(self.hash)==len(sha224):
          hash = "Sha224"
      elif len(self.hash)==len(sha384):
          hash = "sha384"
      elif len(self.hash)==len(sha256):
          hash = "sha256"
      elif self.hash:
          print_error("Set a hash")
      else:
          hash = "md5"
      return hash