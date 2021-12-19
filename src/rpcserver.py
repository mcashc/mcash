from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import socket
import sys,os
import jsonrpclib
from getinfo import Info
from blockchain import Blockchain
from wallet import Wallet
#pip install jsonrpclib

info = Info()
chain = Blockchain()
wallet = Wallet()

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
port = 9091

def chainStatus():
    return info.isChainValid()

def getBalance(b):
    return info.getBalance(b)	

def getAddressInfo(address):
    return info.getAddressInfo(address)	

def getTrxInfo(hash):
    return info.getTxInfo(hash)

def getAllTransaction():
    return info.getAllTransaction()

def getSupply():
    return info.getSupply()

def getAllBlock():
    return info.getAllBlock()

def blockInfoHeight(val):
    return info.getBlockInfoByNumber(val)

def blockInfoHash(val):
    return info.getBlockInfoByHash(val)

def genesisBlock():
    return chain.generateGenesisBlock()

def lastblock():
    return chain.getlastBlock()

def lastblockHeight():
    return str(chain.getlastBlockNumber())

def pendingTrx(): 
    return chain.pendingTrxList()

def addTransaction(key,to_address,amount):
    return chain.addTransactions(key, to_address, amount)

def mining(name,address):
	return info.mining(name, address)

def newAddress():
	return wallet.createWallet()

def signCheckAddress(key):
	return wallet.checkAddress(key)

def resolve():
	return chain.resolveChain()

server = SimpleJSONRPCServer(("0.0.0.0", port), bind_and_activate=False)
def serverStart(a=0):
	try:
		#server = SimpleJSONRPCServer(("localhost", port), bind_and_activate=False)
	    #server.socket = ssl.wrap_socket(server.socket, certfile='server.pem',server_side=True)
	    server.server_bind()
	    server.server_activate()		
	    server.register_function(newAddress)
	    server.register_function(signCheckAddress)
	    server.register_function(getBalance)
	    server.register_function(chainStatus)
	    server.register_function(getAddressInfo)
	    server.register_function(getTrxInfo)
	    server.register_function(getAllTransaction)
	    server.register_function(getSupply)
	    server.register_function(getAllBlock)
	    server.register_function(blockInfoHeight)
	    server.register_function(blockInfoHash)
	    server.register_function(genesisBlock)
	    server.register_function(lastblock)
	    server.register_function(lastblockHeight)
	    server.register_function(addTransaction)
	    server.register_function(pendingTrx)
	    server.register_function(mining)
	    server.register_function(resolve)
	    print("Server started on ",local_ip,port)
	    server.serve_forever()
	except:
		server.shutdown()
		server.server_close()	
		print(" Server Shutdown")


	
