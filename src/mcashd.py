import typer
import sys,time
from rpcserver import serverStart
   
"""
if 'start' == sys.argv[1]: 
    thread = threading.Thread(target=starts,args=(1,))
    thread.start()

elif 'stop' == sys.argv[1]: 
    thread = threading.Thread(target=starts,args=(0,))
    thread.start()
    print("Server Shutdown ")

elif 'restart' == sys.argv[1]: 
    thread = threading.Thread(target=starts,args=(0,))
    thread.start()
    print("Server Restarted")
    thread = threading.Thread(target=starts,args=(1,))
    thread.start()
    """

app = typer.Typer()

@app.command()
def start():
    serverStart()


app()

