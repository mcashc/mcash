from jsonrpclib import Server
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
port=9091
def main():
    #conn = Server('http://'+local_ip+":"+str(port))
    conn = Server('http://161.97.89.98:9091')
    #block index 8487
    #print(conn.chainStatus())
    #print(conn.resolve(),"\n")
    #print(conn.chainStatus(),"\n")
    #print(conn.getSupply())
    #print(conn.getBalance("18KKMEyQUeCzA1TgNMepTYqHVH5mhamAPU"))
    #print(conn.getBalance("1G76cdRnFjA6gq23ihrx87WPMihrcJHuHF"))
    #print(conn.newAddress())
    #print(conn.signCheckAddress("fbf0b8ebfcc1876ddf9e9fbecb084eda4f466070a49a0f7198702549127ff9dc"))

    #print(conn.addTransaction("fbf0b8ebfcc1876ddf9e9fbecb084eda4f466070a49a0f7198702549127ff9dc","0x779dc4d50681bbeb2b4c46c2410c94e684d70c66",952267.00000000))
    #print(conn.pendingTrx())
    while True:
        #print(conn.addTransaction("965de5600d1645737cb2a80133ce87c9a7fa896c28196017cb5a793b9edf930d","1G76cdRnFjA6gq23ihrx87WPMihrcJHuHF",9.00000000))
        #print(conn.addTransaction("965de5600d1645737cb2a80133ce87c9a7fa896c28196017cb5a793b9edf930d","1G76cdRnFjA6gq23ihrx87WPMihrcJHuHF",3.00000000))
        #print(conn.addTransaction("965de5600d1645737cb2a80133ce87c9a7fa896c28196017cb5a793b9edf930d","1G76cdRnFjA6gq23ihrx87WPMihrcJHuHF",2.00000000))
        #print(conn.addTransaction("965de5600d1645737cb2a80133ce87c9a7fa896c28196017cb5a793b9edf930d","1G76cdRnFjA6gq23ihrx87WPMihrcJHuHF",6.00000000))
        #print(conn.addTransaction("965de5600d1645737cb2a80133ce87c9a7fa896c28196017cb5a793b9edf930d","1G76cdRnFjA6gq23ihrx87WPMihrcJHuHF",8.00000000))
        #print(conn.addTransaction("965de5600d1645737cb2a80133ce87c9a7fa896c28196017cb5a793b9edf930d","1G76cdRnFjA6gq23ihrx87WPMihrcJHuHF",10436389.00000000))
        print(conn.mining("M Miner","18KKMEyQUeCzA1TgNMepTYqHVH5mhamAPU"))
    #print(conn.pendingTrx())
	#1G76cdRnFjA6gq23ihrx87WPMihrcJHuHF
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