from silentsploit.core.modules.exploit import (
    BaseExploit,
)
from silentsploit.utils import (
    print_error,
)


class BaseEncoder(BaseExploit):
    architecture = None

    def __init__(self):
        self.module_name = self.__module__.replace("routersploit.modules.encoders.", "").replace(".", "/")

    def encode(self):
        raise NotImplementedError("Please implement 'encode()' method")

    def run(self):
        print_error("Module cannot be run")

    def __str__(self):
        return self.module_name

    def __format__(self, form):
        return format(self.module_name, form)