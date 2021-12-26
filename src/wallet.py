
from keygen import *
from addressgen import CryptoWallet

class Wallet:
    def createWallet(self):
        kg = KeyGenerator()
        kg.seed_input('')
        key = kg.generate_key()
        address = CryptoWallet.generate_address(key)
        public = CryptoWallet.private_to_public(key).decode()
        return [{"privateKey":key,
                 "publickey":public,
                 "address":address}]

    def checkAddress(self,key):
        try:
            address = CryptoWallet.generate_address(key)
            public = CryptoWallet.private_to_public(key).decode()
            return [{"privateKey":key,
                     "publickey":public,
                     "address":address}]
        except:
            return "Invalid Private Key"    

    def signWallet(self,key):
        try:
            address = CryptoWallet.generate_address(key)
            return address
        except:
            return "Failed" 








