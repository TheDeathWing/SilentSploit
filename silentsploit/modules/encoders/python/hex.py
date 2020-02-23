from silentsploit.core.modules.encoders import BaseEncoder
from silentsploit.core.modules.payloads import Architectures


class Encoder(BaseEncoder):
    __info__ = {
        "Name": "Python Hex Encoder",
        "Description": "Module encodes Python payload to Hex format.",
        "Authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # routersploit module
        ),
    }

    architecture = Architectures.PYTHON

    def encode(self, payload):
        encoded_payload = bytes(payload, "utf-8").hex()
        return "exec('{}'.decode('hex'))".format(encoded_payload)