from coin import CoinInfo
class Supply(CoinInfo):
    def supcount(self,val):
        val = float(val)
        val = val-val-val
        #print("supply check",val)
        if val<=10000000:
            return 5000
        elif val<=15000000:
            return 2000            
        elif val<=20000000:
            return 2000
        elif val<self.supply:
            return 1
        else:
            return 0            

    def setdificulty(self,val):
        val = float(val)
        val = val-val-val
        if val<=10000000:
            return 2
        elif val<=15000000:
            return 3
        elif val<=20000000:
            return 5
        elif val<self.supply:
            return 7
        else:
            return 6