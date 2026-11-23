from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Hello World"}

@app.get("/name/{name}")
def read_name(name: str):
    return {"Hello Bro": name}