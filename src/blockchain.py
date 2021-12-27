import hashlib
import json
import sys
import json
from datetime import datetime
from block import Block
from transaction import Transaction
from wallet import Wallet
from supply import Supply
from trxvalidate import TrxValidate
from sizecal import SizeofBlock
from blockd import genesis,newBlock
from coin import CoinInfo
from database_file.db import Dbclass
import ast
#pip install cryptography
#pip install pycryptodome
#pip install blocksmith
wallet = Wallet()
supply = Supply() 
sizeb = SizeofBlock()
db = Dbclass()


class Blockchain(CoinInfo):
    def __init__(self):
        CoinInfo.__init__(self)
        self.chain = db.blockRecord()
        self.pending_trx =db.pendingTrx()

    def generateGenesisBlock(self):    
        return genesis()
    
    def getlastBlock(self):         
            return self.blockRecord()[-1]    

    def getlastBlockNumber(self):               
            block = self.blockRecord()[-1]
            blocknumber = int(block["block_index"])
            return blocknumber

    def addTransactions(self,key,to_address,amount):
        address = wallet.signWallet(key)
        returnmessage = self.getBalance(address)
        if address=="Failed":
            return [{"message":"Invalid Private Key"}]
        else:    
            balance = float(returnmessage)
            amount = float(amount)
            if (balance>=amount):
                trx = Transaction(address,to_address,amount,self.getBalance("coinbase"))
                trxappend = trx.addTransaction()
                trxhash = trxappend["trxhash"]
                #tinfo = db.tdb.put(str(trxhash).encode(),str(trxappend).encode())
                #self.pending_trx.append(trxappend)   
                db.insertTrx(trxhash, trxappend)
                return [{"message":"Success","from_address":address,"current_balance":f'{balance:.{self.decimal}f}',"sent_amount":f'{amount:.{self.decimal}f}',"to_address":to_address}]
            else:
                return [{"message":"Not enough balance","from_address":address,"current_balance":f'{balance:.{self.decimal}f}',"sent_amount":f'{amount:.{self.decimal}f}',"to_address":to_address}]

    def getBalance(self,address):       
        balance=0
        for b in db.blockRecord():
            for t in b["transaction"]:
                if t['from_address'] == address:
                    balance -= float(t['amountin'])                
                if t['to_address'] == address:
                    balance += float(t['amountout'])
        for pt in self.pendingTrxList():
                if pt['from_address'] == address:
                    balance -= float(pt['amountin'])                     
        return f'{balance:.{self.decimal}f}'

    def mineBlock(self, miner_name,miner_address):
        if self.isChainValid()==True:
            lastblock = self.getlastBlock()["block_index"]+1
            trxlist = []
            fees=0
            supbal = self.getBalance("coinbase")
            block_reward = supply.supcount(supbal)
            bonus = float(block_reward)+fees
            roothash =[]
            for i in db.pendingTrx():
                fees+=float(i["fee"])
                trxvalue = {"trxhash":i["trxhash"],"trxtime":i["trxtime"],"blocktime":str(datetime.utcnow()),"from_address":i["from_address"],"to_address":i["to_address"],
                        "amountin":i["amountin"],"amountout":i["amountout"],"fee":i["fee"],"sizeof":i["sizeof"],"block_index":lastblock,"status":1}  
                trxlist.append(trxvalue)   
                roothash.append(i["trxhash"])  
            coinbase = TrxValidate()
            revalue = coinbase.coinbase(lastblock, miner_address,fees,block_reward)
            trxlist.append(revalue)
            roothash.append(revalue['trxhash'])
            tr_string = json.dumps({"markle":roothash,"block_index":str(lastblock)},sort_keys=True).encode()
            hash = hashlib.sha256(tr_string).hexdigest() 
            difficulty = supply.setdificulty(supbal)
            miningBlock = Block(trxlist)
            miningBlock.prevhash=self.getlastBlock()["hash"]
            miningBlock.block_index = lastblock
            miningBlock.tstamp=str(datetime.utcnow())
            miningBlock.minerName = miner_name
            miningBlock.minerAddress = miner_address
            miningBlock.block_reward = f'{block_reward:.{self.decimal}f}'
            miningBlock.fee_reward=f'{fees:.{self.decimal}f}'
            miningBlock.difficulty=difficulty
            if(len(trxlist)>500):
                miningBlock.mineBlock(3)
            else:    
                miningBlock.mineBlock(difficulty)   
            miningBlock.markle=hash  
            miningBlock.block_size=sizeb.calcSize(trxlist)
            current_block = newBlock(miningBlock)
            db.insertBlock(miningBlock.block_index,miningBlock.hash,current_block)
            for root in roothash:
                db.removeTrx(root)
            return True
        else:
            self.resolveChain()    
 
    
    def isChainValid(self):
        block=Block()
        chain = self.blockRecord()
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
            if (currb["hash"] != block.calcHash() and currb["markle"]!=hash):
                print("invalid hash","Block_Index ",currb["block_index"])  
                print("Markle ",currb["markle"],"\n","Hash ",hash) 
                return False
            if (currb["prevhash"] != prevb["hash"]):
                print("invalid chain","Block_Index ",currb["block_index"]) 
                return False  
        return True      

    def resolveChain(self):
        block=Block()
        chain = self.blockRecord()
        for i in range(1,len(chain)):
            prevb= chain[i-1]
            currb=chain[i]
            roothash=[]
            for i in currb["transaction"]:
                roothash.append(i['trxhash'])
            tr_string = json.dumps({"markle":roothash,"block_index":str(currb["block_index"])},sort_keys=True).encode()
            hash = hashlib.sha256(tr_string).hexdigest() 
            if (currb["markle"]!=hash): 
                length = len(chain)-currb["block_index"]
                for b in range(0,length):
                    index = currb["block_index"]+b
                    print("Remove Block ",index,"\n","Hash ",hash) 
                    db.removeBlock(index) 
                db.removeBlock(currb["block_index"])             
            if (currb["hash"] != block.calcHash() and currb["markle"]!=hash):
                length = len(chain)-currb["block_index"]
                for b in range(0,length):
                    index = currb["block_index"]+b
                    print("Remove invalid hash","Block_Index ",index)  
                    print("Markle ",currb["markle"],"\n","Hash ",hash)  
                    db.removeBlock(index)     
                db.removeBlock(currb["block_index"]) 
            if (currb["prevhash"] != prevb["hash"]):
                length = len(chain)-currb["block_index"]
                for b in range(0,length):
                    index = currb["block_index"]+b
                    print("Remove Block invalid chain","Block_Index ",index) 
                    db.removeBlock(index) 
                db.removeBlock(currb["block_index"])   

    def blockRecord(self):
        return db.blockRecord()

    def pendingTrxList(self):
        return db.pendingTrx()        
      
          


