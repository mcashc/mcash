from jsonrpclib import Server
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
port=9091
def main():
    conn = Server('http://'+local_ip+":"+str(port))
    #conn = Server('http://127.0.1.1:9091')
    #block index 8487
    #print(conn.chainStatus())
    #print(conn.resolve(),"\n")
    #print(conn.chainStatus(),"\n")
    #print(conn.getSupply())
    #print(conn.getBalance("0x779dc4d50681bbeb2b4c46c2410c94e684d70c66"))
    #print(conn.getBalance("0x16c243a961f56819688e2cefeba9a268ce40abd0"))
    #print(conn.newAddress())
    #print(conn.signCheckAddress("fbf0b8ebfcc1876ddf9e9fbecb084eda4f466070a49a0f7198702549127ff9dc"))

    #print(conn.addTransaction("fbf0b8ebfcc1876ddf9e9fbecb084eda4f466070a49a0f7198702549127ff9dc","0x779dc4d50681bbeb2b4c46c2410c94e684d70c66",952267.00000000))
    #print(conn.pendingTrx())
    while True:
        print(conn.mining("M Miner","0xeee76f840a6fAd52F4dcd8d24406cc77F2B6b695"))
    #print(conn.pendingTrx())
	#0xeee76f840a6fAd52F4dcd8d24406cc77F2B6b695
    print(conn.lastblock())
    print(conn.chainStatus(),"\n")
    #trx = conn.blockInfoHeight(8487)
    trx = conn.getAllBlock()
    for i in trx:
        #for t in i['transaction']:
            #print(t,"\n")
        #print(len(i['transaction']))
        #print(i)
        a=0
    #print(conn.blockInfoHash("00001c4e4b6c3ba1fc5d909139cd3cea2e78bdb00b67c4f61d91e4260e8c8790"),"\n")
    #print(conn.blockInfoHeight(800),"\n")
    #print(conn.getAllTransaction())
    
    #print(conn.getAllBlock())
    print(conn.genesisBlock())
    print(conn.lastblockHeight())



main()    