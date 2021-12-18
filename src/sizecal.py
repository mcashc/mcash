import sys
class SizeofBlock:
    def calcSize(self,arr):
        size=0
        for i in arr:
            #size += sys.getsizeof(i["from_address"]+i["to_address"]+str(i["amountin"])+str(i["amountout"])+str(i["fee"]))
            size+=i["sizeof"]
        return size 

    def trxSize(self,from_address,to_address,amountin,amountout,fee):       
        size = sys.getsizeof(from_address+to_address+str(amountin)+str(amountout)+str(fee))
        return size
        