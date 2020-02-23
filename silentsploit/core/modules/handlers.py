from silentsploit.core.modules.option import *
from silentsploit.core.colors import *

class BaseHandler(BaseExploit):
    def handle(self):
        raise notImplementedError("Please implement 'handle' method")
        
    def run(self):
        print_error("Module cannot be run")