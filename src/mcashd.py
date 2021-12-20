import typer
#pip3 install typer
import sys,time
import threading
from rpcserver import serverStart


def starts(n):
    counter = 0
    var = ""
    if n==0:
        var=False
    else:
        var=True    
    while var:
        if var==True:
            serverStart()
            time.sleep(3)
            print("Function {} run!".format(counter))
            print(var)
            counter+=1
        else:
            break    
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
    thread = threading.Thread(target=starts,args=(1,))
    thread.start() 

@app.command()
def stop():
    thread = threading.Thread(target=starts,args=(0,))
    thread.start()
    print("Server Shutdown ")

@app.command()
def restart():
    thread = threading.Thread(target=starts,args=(0,))
    thread.start()
    print("Server Restarted")
    thread = threading.Thread(target=starts,args=(1,))
    thread.start()  

app()

