import re
import os.path
import socket
from silentsploit.utils import *
from silentsploit.core.exceptions import *



class Option(object):
    """ Exploit attribute that is set by the end user """

    def __init__(self, default, description="", advanced=False):
        self.label = None
        self.description = description

        try:
            self.advanced = bool(advanced)
        except ValueError:
            raise OptionValidationError("Invalid value. Cannot cast '{}' to boolean.".format(advanced))

        if default or default == 0:
            self.__set__("", default)
        else:
            self.display_value = ""
            self.value = ""

    def __get__(self, instance, owner):
        return self.value

class OptIP(Option):
    """ Option IP attribute """

    def __set__(self, instance, value):
        if not value or is_ipv4(value) or is_ipv6(value):
            self.value = self.display_value = value
        else:
            raise OptionValidationError("Invalid address. Provided address is not valid IPv4 or IPv6 address.")
class OptHost(Option):
    """ Option Host Or Ip attribute """
    def __set__(self, instance, value):
       try: 
           socket.gethostbyname(value)
           self.value = self.display_value = value
       except:
           raise OptionValidationError("Invalid ip or hostname. Provide address is not valid.")
class OptFile(Option):
    """ Option File attribute """

    def __set__(self, instance, value):
            try:
                with open(value) as f:
                  self.value = self.display_value = value
            except IOError:
                raise IOError("File '{}' does not exist.".format(value))


class OptPort(Option):
    """ Option Port attribute """

    def __set__(self, instance, value):
        try:
            value = int(value)

            if 0 < value <= 65535:  # max port number is 65535
                self.display_value = str(value)
                self.value = value
            else:
                raise OptionValidationError("Invalid option. Port value should be between 0 and 65536.")
        except ValueError:
            raise OptionValidationError("Invalid option. Cannot cast '{}' to integer.".format(value))


class OptBool(Option):
    """ Option Bool attribute """

    def __init__(self, default, description="", advanced=False):
        self.description = description

        if default:
            self.display_value = "true"
        else:
            self.display_value = "false"

        self.value = default

        try:
            self.advanced = bool(advanced)
        except ValueError:
            raise OptionValidationError("Invalid value. Cannot cast '{}' to boolean.".format(advanced))

    def __set__(self, instance, value):
        if value == "true":
            self.value = True
            self.display_value = value
        elif value == "false":
            self.value = False
            self.display_value = value
        else:
            raise OptionValidationError("Invalid value. It should be true or false.")


class OptInteger(Option):
    """ Option Integer attribute """

    def __set__(self, instance, value):
        try:
            self.display_value = str(value)
            self.value = int(value)
        except ValueError:
            try:
                self.value = int(value, 16)
            except ValueError:
                raise OptionValidationError("Invalid option. Cannot cast '{}' to integer.".format(value))


class OptFloat(Option):
    """ Option Float attribute """

    def __set__(self, instance, value):
        try:
            self.display_value = str(value)
            self.value = float(value)
        except ValueError:
            raise OptionValidationError("Invalid option. Cannot cast '{}' to float.".format(value))


class OptString(Option):
    """ Option String attribute """

    def __set__(self, instance, value):
        try:
            self.value = self.display_value = str(value)
        except ValueError:
            raise OptionValidationError("Invalid option. Cannot cast '{}' to string.".format(value))


class OptMAC(Option):
    """ Option MAC attribute """

    def __set__(self, instance, value):
        regexp = r"^[a-f\d]{1,2}:[a-f\d]{1,2}:[a-f\d]{1,2}:[a-f\d]{1,2}:[a-f\d]{1,2}:[a-f\d]{1,2}$"
        if re.match(regexp, value.lower()):
            self.value = self.display_value = value
        else:
            raise OptionValidationError("Invalid option. '{}' is not a valid MAC address".format(value))


class OptWordlist(Option):
    """ Option Wordlist attribute """

    def __get__(self, instance, owner):
        if self.display_value.startswith("file://"):
            path = self.display_value.replace("file://", "")
            with open(path, "r") as f:
                lines = [line.strip() for line in f.readlines()]
                return lines

        return self.display_value.split(",")

    def __set__(self, instance, value):
        if value.startswith("file://"):
            path = value.replace("file://", "")
            if not os.path.exists(path):
                raise OptionValidationError("File '{}' does not exist.".format(path))

        self.value = self.display_value = value


class OptEncoder(Option):
    """ Option Encoder attribute """

    def __init__(self, default, description="", advanced=False):
        self.description = description

        if default:
            self.display_value = default
            self.value = default
        else:
            self.display_value = ""
            self.value = None

        try:
            self.advanced = bool(advanced)
        except ValueError:
            raise OptionValidationError("Invalid value. Cannot cast '{}' to boolean.".format(advanced))

    def __set__(self, instance, value):
        encoder = instance.get_encoder(value)

        if encoder:
            self.value = encoder
            self.display_value = value
        else:
            raise OptionValidationError("Encoder not available. Check available encoders with `show encoders`.")