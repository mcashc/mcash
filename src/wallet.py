
from keygen import *
from addressgen import CryptoWallet

class Wallet:
    def createWallet(self):
        kg = KeyGenerator()
        kg.seed_input('')
        key = kg.generate_key()
        address1 = CryptoWallet.generate_address(key)
        address = CryptoWallet.checksum_address(address1)
        public = CryptoWallet.publickeyval(key).decode()
        return [{"privateKey":key,
                 "publickey":public,
                 "address":address}]

    def checkAddress(self,key):
        try:
            address1 = CryptoWallet.generate_address(key)
            address = CryptoWallet.checksum_address(address1)
            public = CryptoWallet.publickeyval(key).decode()
            return [{"privateKey":key,
                     "publickey":public,
                     "address":address}]
        except:
            return "Invalid Private Key"    

    def signWallet(self,key):
        try:
            address1 = CryptoWallet.generate_address(key)
            address = CryptoWallet.checksum_address(address1)
            return address
        except:
            return "Failed" 








