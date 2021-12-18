from blockchain import Blockchain
from block import Block
from coin import CoinInfo
import hashlib
import ast
import json
block = Blockchain()

class Info(CoinInfo):
    def mining(self,name,miner):
        block.mineBlock(name, miner)

    def isChainValid(self):
        blocks=Block()
        chain = block.blockRecord()
        for i in range(1,len(chain)):
            prevb= chain[i-1]
            currb=chain[i]
            roothash=[]
            for i in currb["transaction"]:
                roothash.append(i['trxhash'])
            tr_string = json.dumps({"markle":roothash,"block_index":str(currb["block_index"])},sort_keys=True).encode()
            hash = hashlib.sha256(tr_string).hexdigest() 
            if (currb["markle"]!=hash): 
                print("Invalid Markle Root ",currb["markle"],"\n","Hash ",hash) 
                return False             
            if (currb["hash"] != blocks.calcHash() and currb["markle"]!=hash):
                print("invalid hash","Block_Index ",currb["block_index"])  
                print("Markle ",currb["markle"],"\n","Hash ",hash) 
                return False
            if (currb["prevhash"] != prevb["hash"]):
                print("invalid chain","Block_Index ",currb["block_index"]) 
                return False  
        return True    
    def getAddressInfo(self,address):
        lastblock = int(block.getlastBlockNumber())
        trx = []
        balance=0
        totalin=0
        totalout=0
        for b in block.blockRecord():
            confirm = lastblock-int(b["block_index"])
            for t in b["transaction"]:
                if t['from_address'] == address:
                    trxvalue = {"trxhash":t["trxhash"],"trxtime":t["trxtime"],"blocktime":t["blocktime"],
                                "from_address":t["from_address"],"to_address":t["to_address"],
                                "amountin":t["amountin"],"amountout":t["amountout"],"fee":t["fee"],
                                "sizeof":t["sizeof"],"block_index":t["block_index"],
                                "block_hash":b["hash"],"status":1,"confirmation":confirm
                                }  
                    trx.append(trxvalue)
                    balance -= float(t['amountin']) 
                    totalout +=float(t['amountin'])                
                if t['to_address'] == address:
                    trxvalue = {"trxhash":t["trxhash"],"trxtime":t["trxtime"],"blocktime":t["blocktime"],
                                "from_address":t["from_address"],"to_address":t["to_address"],
                                "amountin":t["amountin"],"amountout":t["amountout"],"fee":t["fee"],
                                "sizeof":t["sizeof"],"block_index":t["block_index"],
                                "block_hash":b["hash"],"status":1,"confirmation":confirm
                                }  
                    trx.append(trxvalue)
                    balance += float(t['amountout'])       
                    totalin +=float(t['amountout'])         
        for pt in block.pendingTrxList():
                if pt['from_address'] == address:
                    trx.append(pt)
                    balance -= float(pt['amountin'])   
                    totalout += float(pt['amountin'])              
        trx.reverse()     
        result = [{"address":address,
                   "balance":f'{balance:.{self.decimal}f}',
                   "totalin":f'{totalin:.{self.decimal}f}',
                   "totalout":f'{totalout:.{self.decimal}f}',
                   "transactions":trx
                   }]   
        if address=="coinbase" or address=="0xfeeesaddress":
            return []   
        else:            
            return result

    def getTxInfo(self,hash):
        lastblock = int(block.getlastBlockNumber())
        trx = []
        for b in block.blockRecord():
            confirm = lastblock-int(b["block_index"])
            for i in b["transaction"]:
                if i['trxhash'] == hash:
                    #trx.append(t)   
                    trxvalue = {"trxhash":i["trxhash"],"trxtime":i["trxtime"],"blocktime":i["blocktime"],
                                "from_address":i["from_address"],"to_address":i["to_address"],
                                "amountin":i["amountin"],"amountout":i["amountout"],"fee":i["fee"],
                                "sizeof":i["sizeof"],"block_index":i["block_index"],
                                "block_hash":b["hash"],"status":1,"confirmation":confirm
                                }  
                    trx.append(trxvalue)        
        for pt in block.pendingTrxList():
                if pt['trxhash'] == hash:
                    trx.append(pt)
        return trx

    def getAllTransaction(self):
        lastblock = int(block.getlastBlockNumber())
        trx = []
        for b in block.blockRecord():
            confirm = lastblock-int(b["block_index"])
            for i in b["transaction"]:
                trxvalue = {"trxhash":i["trxhash"],"trxtime":i["trxtime"],"blocktime":i["blocktime"],
                            "from_address":i["from_address"],"to_address":i["to_address"],
                            "amountin":i["amountin"],"amountout":i["amountout"],"fee":i["fee"],
                            "sizeof":i["sizeof"],"block_index":i["block_index"],
                            "block_hash":b["hash"],"status":1,"confirmation":confirm
                            }  
                trx.append(trxvalue)                 
        for pt in block.pendingTrxList():
                trx.append(pt)        
        trx.reverse()
        return trx

    def getBalance(self,address):
        balance=0
        for b in block.blockRecord():
            for t in b["transaction"]:
                if t['from_address'] == address:
                    balance -= float(t['amountin'])                
                if t['to_address'] == address:
                    balance += float(t['amountout'])
        for pt in block.pending_trx:
                if pt['from_address'] == address:
                    balance -= float(pt['amountin'])    
        if address=="coinbase" or address=="0xfeeesaddress":
            return []   
        else:                                    
            return f'{balance:.{self.decimal}f}'

    def getSupply(self):
        balance=0
        for b in block.blockRecord():
            for t in b["transaction"]:
                if t['from_address'] == "coinbase":
                    balance -= float(t['amountin'])                
                if t['to_address'] == "coinbase":
                    balance += float(t['amountout'])
        balance = f'{balance-balance-balance:.{self.decimal}f}'         
        return [{"name":self.name,"symbol":self.symbol,"decimal":self.decimal,"current_supply":balance,"max_supply":self.supply}]

    def getAllBlock(self):
        #block.resolveChain()
        allblock=block.blockRecord()
        allblock.reverse()
        return allblock

    def getBlockInfoByNumber(self,val):
        lastblock = block.getlastBlockNumber()
        blocks=[]
        for b in block.blockRecord():
            if b["block_index"]==int(val):
                confirm = lastblock-int(b["block_index"])
                record = {'block_index': b["block_index"], 'nonce': b["nonce"], 
                          'tstamp': b["tstamp"], 
                           'transaction': b["transaction"], 'block_size': b["block_size"], 
                           'minerName': b["minerName"], 'minerAddress': b["minerAddress"], 
                           'block_reward': b["block_reward"], 'fee_reward': b["fee_reward"], 
                           'prevhash': b["prevhash"], 'hash': b["hash"], 
                           'markle': b["markle"], 'difficulty': b["difficulty"],
                           'confirmation':confirm
                           }
                blocks.append(record)
        return blocks

    def getBlockInfoByHash(self,val):
        lastblock = block.getlastBlockNumber()
        blocks=[]
        for b in block.blockRecord():
            if b["hash"]==val:
                confirm = lastblock-int(b["block_index"])
                record = {'block_index': b["block_index"], 'nonce': b["nonce"], 
                          'tstamp': b["tstamp"], 
                           'transaction': b["transaction"], 'block_size': b["block_size"], 
                           'minerName': b["minerName"], 'minerAddress': b["minerAddress"], 
                           'block_reward': b["block_reward"], 'fee_reward': b["fee_reward"], 
                           'prevhash': b["prevhash"], 'hash': b["hash"], 
                           'markle': b["markle"], 'difficulty': b["difficulty"],
                           'confirmation':confirm
                           }
                blocks.append(record)
        return blocks
"""
epay = Info()
chain = epay.getAllBlock()
for i in chain:
    #for t in i['transaction']:
        #print(t,"\n")  
    #print(i,"\n")
    p=0
  
print(block.isChainValid(),"\n")
#print(epay.mining("Arif","0x779dc4d50681bbeb2b4c46c2410c94e684d70c66"))
#print(block.resolveChain(),"\n")
print(epay.getBalance("0x779dc4d50681bbeb2b4c46c2410c94e684d70c66"))
print(epay.getBalance("0x16c243a961f56819688e2cefeba9a268ce40abd0"))

for i in range(0,1000):
    print(block.addTransactions("fbf0b8ebfcc1876ddf9e9fbecb084eda4f466070a49a0f7198702549127ff9dc","0x779dc4d50681bbeb2b4c46c2410c94e684d70c66",10))
    print(block.addTransactions("fbf0b8ebfcc1876ddf9e9fbecb084eda4f466070a49a0f7198702549127ff9dc","0x779dc4d50681bbeb2b4c46c2410c94e684d70c66",30))
    print(block.addTransactions("fbf0b8ebfcc1876ddf9e9fbecb084eda4f466070a49a0f7198702549127ff9dc","0x779dc4d50681bbeb2b4c46c2410c94e684d70c66",13))
    
print(block.pendingTrxList())
print(block.getlastBlockNumber())

#print(epay.getBlockInfoByHash("00001c4e4b6c3ba1fc5d909139cd3cea2e78bdb00b67c4f61d91e4260e8c8790"),"\n")
#print(epay.getBlockInfoByNumber(800),"\n")
print(epay.getSupply())

for i in block.blockRecord():
    d = ast.literal_eval(i[0])
    #print(d["hash"])
    """