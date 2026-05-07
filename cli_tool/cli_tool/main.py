import typer
from .s3 import list_bucket

app = typer.Typer()

@app.command()
def test(name:str):
    print(f"Name : {name}")

@app.command()
def hello(name:str):
    print(f"Hello : {name}")

@app.command()
def bucket():
    data = list_bucket()

    for bucket in data:
        print(bucket["Name"])
        

if __name__ == "__main__":
    app()
