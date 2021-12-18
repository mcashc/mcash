import hashlib
import json
from datetime import datetime
#pip install cryptography


class Block:
    def __init__(self, transaction=[]):
        self.block_index = ''
        self.nonce=0
        self.tstamp=""
        self.transaction=transaction
        self.block_size=""
        self.minerName=""
        self.minerAddress=""
        self.block_reward=0
        self.fee_reward=0
        self.prevhash=""
        self.hash=self.calcHash()
        self.markle=""
        self.difficulty=""
        
    def calcHash(self):
        block_string = json.dumps({"nonce":self.nonce,"tstamp":self.tstamp,"transaciton":self.transaction,"prevhash":self.prevhash},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mineBlock(self, diffic):
        #print("Mining running")
        while(self.hash[:diffic] != str().zfill(diffic)):
            self.nonce +=1
            self.hash = self.calcHash()
            #print(self.hash+"\n")
        #print("Block mined ", self.hash+"\n")  
        nblock = [{"status":"Block Mined Success",
                   "timestamp":self.tstamp,
                   "block":self.block_index,
                   "prevhash":self.prevhash,
                   "hash":self.hash,
                   "transactions":len(self.transaction),
                   "miner":self.minerName,
                   "reward":self.block_reward,
                   "fee_reward":self.fee_reward
                   }]   
        print(nblock,"\n")
