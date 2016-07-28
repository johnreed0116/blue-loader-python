"""
*******************************************************************************
*   Ledger Blue
*   (c) 2016 Ledger
*
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
*  Unless required by applicable law or agreed to in writing, software
*  distributed under the License is distributed on an "AS IS" BASIS,
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*  limitations under the License.
********************************************************************************
"""

from .hexParser import IntelHexParser
from .hexParser import IntelHexPrinter
from secp256k1 import PublicKey
import hashlib
import binascii
import argparse

def auto_int(x):
    return int(x, 0)

parser = argparse.ArgumentParser()
parser.add_argument("--hex", help="Hex file to be verify")
parser.add_argument("--key", help="The public key to verify with (hex encoded)")
parser.add_argument("--signature", help="The signature to verify with (hex encoded)")

args = parser.parse_args()

if args.hex == None:
	raise Exception("Missing hex filename to verify")
if args.key == None:
	raise Exception("Missing public key")
if args.signature == None:
	raise Exception("Missing signature")

# parse
parser = IntelHexParser(args.hex)

# prepare data
m = hashlib.sha256()
# consider areas are ordered by ascending address and non-overlaped
for a in parser.getAreas():
	m.update(a.data)
dataToSign = m.digest()

publicKey = PublicKey(bytes(bytearray.fromhex(args.key)), raw=True)
signature = publicKey.ecdsa_deserialize(bytes(bytearray.fromhex(args.signature)))
if not publicKey.ecdsa_verify(bytes(dataToSign), signature, raw=True):
	raise Exception("Signature not verified")

print "Signature verified"
