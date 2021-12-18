from rpcserver import serverStart
import typer
#pip3 install typer

app = typer.Typer()
@app.command()
def start():
    serverStart()  


app()