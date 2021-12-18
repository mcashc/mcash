from transaction import Transaction

class TrxValidate:
    def coinbase(self,lastblock,miner_address,fees,block_reward):
        #print("Block Reward ",block_reward)
        if block_reward==0:
            trx = Transaction("0xfeeesaddress",miner_address,fees,0)
            reward = trx.rewardTransaction(lastblock,1)
            return reward
        else:
            trx = Transaction("coinbase",miner_address,block_reward,0)
            reward = trx.rewardTransaction(lastblock,1)
            return reward            


         