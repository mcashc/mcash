from block import Block

def firstBlock():    
        genblock = Block([])
        genblock.tstamp="2021-11-21 23:36:28"
        genblock.prevhash="00000000000000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b"
        genblock.block_index=0
        genblock.nonce=0
        genblock.markle="277d2543924f396a6fb9bd871d581ef346a62f8a5bc932768f4760ccb10ea407"
        genblock.block_reward=0
        genblock.minerName="Genesis Mining"
        genblock.block_size=0
        genblock.minerAddress="18KKMEyQUeCzA1TgNMepTYqHVH5mhamAPU"  
        return genblock

def genesis():
    genblock = firstBlock()
    genesisb = {'block_index': genblock.block_index, 
                'nonce': genblock.nonce, 
                'tstamp': genblock.tstamp, 
                'transaction': genblock.transaction, 
                'block_size': genblock.block_size, 
                'minerName': genblock.minerName, 
                'minerAddress': genblock.minerAddress, 
                'block_reward': genblock.block_reward, 
                'fee_reward': genblock.fee_reward, 
                'prevhash': genblock.prevhash, 
                'hash': genblock.hash, 
                'markle': genblock.markle, 
                'difficulty': genblock.difficulty
                }      
    return genesisb    

def newBlock(miningBlock):
    current_block = {'block_index': miningBlock.block_index, 
                    'nonce': miningBlock.nonce, 
                    'tstamp': miningBlock.tstamp, 
                    'transaction': miningBlock.transaction, 
                    'block_size': miningBlock.block_size, 
                    'minerName': miningBlock.minerName, 
                    'minerAddress': miningBlock.minerAddress, 
                    'block_reward': miningBlock.block_reward, 
                    'fee_reward': miningBlock.fee_reward, 
                    'prevhash': miningBlock.prevhash, 
                    'hash': miningBlock.hash, 
                    'markle': miningBlock.markle, 
                    'difficulty': miningBlock.difficulty
                    }
    return current_block                