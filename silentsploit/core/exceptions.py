class SilentSploitException(Exception):
    def __init__(self, msg = ""):
        super(SilentSploitException, self).__init__(msg)


class OptionValidationError(SilentSploitException):
    pass


class StopThreadPoolExecutor(SilentSploitException):
    pass