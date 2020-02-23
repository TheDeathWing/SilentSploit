#!/usr/bin/env python
#! -*- Encoding: utf-8 -*-
import sys, os
import argparse
# This var don't allow .pyc or bytecode files
# sys.dont_write_bytecode = True
from silentsploit.core.base import * 
from silentsploit.core.colors import *

def Framework(argv):
 silentsploit = SilentSploit()
 if len(argv[1:]):
  #silentsploit.nonInteractive(argv)
  print("No interactive shell will be added :)")
 else:
  silentsploit.start()
if __name__ == "__main__":
    try:
        Framework(sys.argv)
    except (KeyboardInterrupt, SystemExit):
        pass