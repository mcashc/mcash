from blockchain import Blockchain
chain = Blockchain()

def mining(name,miner):
    chain.mineBlock(name, miner)

mining("Mala Khatun","0x16c243a961f56819688e2cefeba9a268ce40abd0")
print(chain.isChainValid())