from base64 import b64encode
from silentsploit.core.modules.encoders import BaseEncoder
from silentsploit.core.modules.payloads import Architectures


class Encoder(BaseEncoder):
    __info__ = {
        "Name": "PHP Base64 Encoder",
        "Description": "Module encodes PHP payload to Base64 format.",
        "Authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # routersploit module
        ),
    }

    architecture = Architectures.PHP

    def encode(self, payload):
        encoded_payload = str(b64encode(bytes(payload, "utf-8")), "utf-8")
        return "eval(base64_decode('{}'));".format(encoded_payload)