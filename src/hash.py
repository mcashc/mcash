
import hashlib
import json
import sys

tr_string = json.dumps({"markle":["5fb9e74b5dd9ebee60a776dc568fa03489ebf5c47d321c6090c1a4b83a870de4","3541112124efe75543bd7c9bec658126c2c8de69415064737a63707077612a0c"]},sort_keys=True).encode()
hash = hashlib.sha256(tr_string).hexdigest() 
print(hash)


tr_string = json.dumps({"from_address":"coinbase","to_address":"0x16c243a961f56819688e2cefeba9a268ce40abd0","amountin":10,"amountout":10},sort_keys=True).encode()
hash = hashlib.sha256(tr_string).hexdigest() 
print(hash)

tr_string = json.dumps({"from_address":"genesis","to_address":"0x779dc4d50681bbeb2b4c46c2410c94e684d70c66","amountin":0,"amountout":0},sort_keys=True).encode()
hash = hashlib.sha256(tr_string).hexdigest() 
print(hash)

print(sys.getsizeof(hash))

import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
#print(convert_size(1024*10000))   


{
            'trxhash': '5fb9e74b5dd9ebee60a776dc568fa03489ebf5c47d321c6090c1a4b83a870de4', 
            'trxtime': '2021-11-24 18:10:35.822130', 'blocktime': '2021-11-24 18:10:35.822130',
            'from_address': 'coinbase', 'to_address':'0x16c243a961f56819688e2cefeba9a268ce40abd0', 
            'amountin': 1000000000.00000000,'amountout': 10.00000000, 'fee': 0.00000000, "sizeof":150
            },
            {'trxhash': '3541112124efe75543bd7c9bec658126c2c8de69415064737a63707077612a0c', 
            'trxtime': '2021-11-24 18:10:35.822130', 'blocktime': '2021-11-24 18:10:35.822130',
            'from_address': 'genesis', 'to_address':'0x779dc4d50681bbeb2b4c46c2410c94e684d70c66', 
            'amountin': 0.00000000,'amountout': 0.00000000, 'fee': 0.00000000,"sizeof":150
            }
