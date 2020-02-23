from binascii import hexlify
from silentsploit.core.modules.encoders import BaseEncoder
from silentsploit.core.modules.payloads import Architectures


class Encoder(BaseEncoder):
    __info__ = {
        "Name": "PHP Hex Encoder",
        "Description": "Module encodes PHP payload to Hex format.",
        "Authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # routersploit module
        ),
    }

    architecture = Architectures.PHP

    def encode(self, payload):
        encoded_payload = str(hexlify(bytes(payload, "utf-8")), "utf-8")
        return "eval(hex2bin('{}'));".format(encoded_payload)