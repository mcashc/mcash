import psycopg2

conn = psycopg2.connect("dbname=blockchain user=postgres password=11111111")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS block(block_index INT NOT NULL,hash TEXT NOT NULL,blocks TEXT NOT NULL)''')
cur.execute('''CREATE TABLE IF NOT EXISTS trx(trxhash TEXT NOT NULL,data TEXT NOT NULL)''')

