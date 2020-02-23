from silentsploit.core.modules.encoders import BaseEncoder
from silentsploit.core.modules.payloads import Architectures


class Encoder(BaseEncoder):
    __info__ = {
        "Name": "Perl Hex Encoder",
        "Description": "Module encodes PERL payload to Hex format.",
        "Authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # routersploit module
        ),
    }

    architecture = Architectures.PERL

    def encode(self, payload):
        encoded_payload = bytes(payload, "utf-8").hex()
        return "eval(pack('H*','{}'));".format(encoded_payload)