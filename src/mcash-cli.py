from getinfo import Info
from blockchain import Blockchain
from wallet import Wallet
import typer

info = Info()
chain = Blockchain()
wallet = Wallet()
app = typer.Typer(help="MCash CLI Command",add_completion=True)
 
@app.command()
def chainstatus():
    print(info.isChainValid())
@app.command()
def getbalance(address):
    print(info.getBalance(address))	
@app.command()
def getaddressinfo(address):
    print(info.getAddressInfo(address))	
@app.command()
def gettrxinfo(hash):
    print(info.getTxInfo(hash))
@app.command()
def getalltransaction():
    print(info.getAllTransaction())
@app.command()
def getsupply():
    print(info.getSupply())
@app.command()
def getallBlock():
    print(info.getAllBlock())
@app.command()
def blockinfoheight(block_index):
    print(info.getBlockInfoByNumber(block_index))
@app.command()
def blockinfohash(block_hash):
    print(info.getBlockInfoByHash(block_hash))
@app.command()
def genesisblock():
    print(chain.generateGenesisBlock())
@app.command()
def lastblock():
    print(chain.getlastBlock())
@app.command()
def lastblockheight():
    print(chain.getlastBlockNumber())
@app.command()
def pendingTrx():
    print(chain.pendingTrxList())
@app.command()
def addtransaction(private_key,to_address,amount):
    print(chain.addTransactions(private_key, to_address, amount))
@app.command()
def mining(name,address):
    print(info.mining(name, address))
@app.command()
def newaddress():
	print(wallet.createWallet())
@app.command()
def signcheckaddress(key):
	print(wallet.checkAddress(key))
@app.command()
def resolve():
	print(chain.resolveChain())



if __name__=="__main__":
    app()