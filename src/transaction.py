import hashlib
import json
from datetime import datetime
import sys 
from sizecal import SizeofBlock
from coin import CoinInfo
sizetr = SizeofBlock()


class Transaction(CoinInfo):
    def __init__(self,from_address,to_address,amount,csupply):
        CoinInfo.__init__(self)
        self.from_address=from_address
        self.to_address=to_address
        self.amount=amount
        self.csupply = csupply
    
    def addTransaction(self):
        val = float(self.feesCount())
        total = float(self.amount)-val
        tr_string = json.dumps({"trxtime":str(datetime.utcnow()),"from_address":self.from_address,"to_address":self.to_address,"amountin":self.amount,"amountout":total},sort_keys=True).encode()
        hash = hashlib.sha256(tr_string).hexdigest()  

        #size = sys.getsizeof(self.from_address+self.to_address+str(self.amount)+str(total)+str(val))
        size = sizetr.trxSize(self.from_address, self.to_address, self.amount, total, val)

        trxvalue = {"trxhash":hash,"trxtime":str(datetime.utcnow()),"blocktime":str(datetime.utcnow()),"from_address":self.from_address,"to_address":self.to_address,
        "amountin":f'{self.amount:.{self.decimal}f}',"amountout":f'{total:.{self.decimal}f}',
        "fee":f'{val:.{self.decimal}f}',"sizeof":size,"block_index":'',"block_hash":'',"status":0,"confirmation":""}  
        return trxvalue

    def rewardTransaction(self,index,status):
        csupply = f'{self.csupply:.{self.decimal}f}'
        tr_string = json.dumps({"trxtime":str(datetime.utcnow()),"from_address":self.from_address,"to_address":self.to_address,"amountin":self.amount,"amountout":self.amount},sort_keys=True).encode()
        hash = hashlib.sha256(tr_string).hexdigest()  

        #size = sys.getsizeof(self.from_address+self.to_address+str(self.amount)+str(self.amount)+str(csupply))
        size = sizetr.trxSize(self.from_address, self.to_address, self.amount, self.amount, csupply)

        trxvalue = {"trxhash":hash,"trxtime":str(datetime.utcnow()),"blocktime":str(datetime.utcnow()),"from_address":self.from_address,"to_address":self.to_address,
        "amountin":f'{self.amount:.{self.decimal}f}',"amountout":f'{self.amount:.{self.decimal}f}',
        "fee":csupply,"sizeof":size,"block_index":index,"status":status}  
        return trxvalue

    def feesCount(self):
        bal = float(self.csupply)
        final = bal-bal-bal
        #print('Fees Count Base Final',final)
        if final>=self.supply:
            return f'{0.001:.{self.decimal}f}'
        else:
            return 0  
             
       
        