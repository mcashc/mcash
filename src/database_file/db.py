import ast
import os, shutil
import sqlite3
from blockd import genesis
import pymongo


class Dbclass:
    
    def __init__(self):
        #SQLite3 Connection
        self.conn = sqlite3.connect('././dataStore/block.db')
        self.cur = self.conn.cursor()
        self.createBlockTable()
        self.createTrxTable()
        #MongoDb Connection
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.dbs = self.myclient['blockchain']
        self.blocks = self.dbs["blocks"]
        self.trxs = self.dbs["trxs"]

    def createBlockTable(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS block(block_index INT NOT NULL,hash TEXT NOT NULL,blocks TEXT NOT NULL)''')

    def createTrxTable(self):           
        self.conn.execute('''CREATE TABLE IF NOT EXISTS trx(trxhash TEXT NOT NULL,data TEXT NOT NULL)''')
 
    def blockRecord(self):
        #Sqlite3
        block=[genesis()]
        """
        try:
            self.cur.execute("SELECT blocks FROM block ORDER BY block_index ASC")
            data = list(self.cur.fetchall())
            for i in data:
                d = ast.literal_eval(i[0])
                block.append(d)
        except:
            print("Error")  """

        #MongoDb
        for b in self.blocks.find({},{ "_id": 0}).sort("block_index",1):
            block.append(b)
           
        return block 


    def insertBlock(self,block_index,hash,current_block):
        #Sqlite3
        """
        self.cur.execute("SELECT * FROM block WHERE block_index=?",(block_index,))
        entry = self.cur.fetchone()
        if entry==None:
            try:
                self.conn.execute("INSERT INTO block(block_index,hash,blocks)VALUES(?,?,?)",(block_index,str(hash),str(current_block),)) 
                self.conn.commit()
            except:
                print("Error")"""
        #MongoDb
        ent = self.blocks.find_one({"block_index":block_index})
        if ent==None:
            self.blocks.insert_one(current_block)        
  

    def removeBlock(self,block_index):
        #Sqlite3
        """
        try:
            self.cur.execute("DELETE FROM block WHERE block_index=?",(block_index,))    
            self.conn.commit()
        except:
            print("Error")   """
        #MongoDb    
        self.blocks.delete_one({"block_index":block_index})

    def pendingTrx(self):
        #Sqlite3
        trx=[]
        """
        try:
            self.cur.execute("SELECT data FROM trx")
            data = list(self.cur.fetchall())
            for i in data:
                d = ast.literal_eval(i[0])
                trx.append(d)    
        except:
            print("Error")  """

        #MongoDb
        for t in self.trxs.find({},{ "_id": 0}):
            trx.append(t)
                              
        return trx

    def insertTrx(self,trxhash,trxappend):
        #Sqlite3
        """
        try:
            self.conn.execute("INSERT INTO trx(trxhash,data)VALUES(?,?)",(str(trxhash),str(trxappend),)) 
            self.conn.commit()
        except:
            print("Error")  """ 

        #MongoDb    
        self.trxs.insert_one(trxappend)

    def removeTrx(self,trxhash):
        #Sqlite3
        """
        try:
            self.cur.execute("DELETE FROM trx WHERE trxhash=?",(trxhash,))    
            self.conn.commit()
        except:
            print("Error")"""

        #MongoDb    
        self.trxs.delete_one({"trxhash":trxhash})




"""
    def blockRecord(self):
        #self.db.delete(b'3330')
        data=[]
        for key,value in self.db:
            dvalue = ast.literal_eval(value.decode())
            data.append(dvalue)  
        va=-0    
        block=[genesis()]
        while va < len(data):
            va+=1
            for i in data:
                if va==i['block_index']:
                    block.append(i)
        return block   


    def blockRecord(self):
        #self.db.delete(b'3330')
        data=[genesis()]
        for key,value in self.db:
            dvalue = ast.literal_eval(value.decode())
            last = data[-1]
            lastblock = last["block_index"]+1
            #print(dvalue["block_index"])
            if lastblock==dvalue["block_index"]:
                data.append(dvalue)  
        return data    

    def copyBlock(self):
        db = self.db
        root_src_dir = r'./blockStore'
        root_dst_dir = './blockBackUp'
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)   
            try:    
                shutil.copy(src_file, dst_dir)
            except:
                a=0  
                               
"""        