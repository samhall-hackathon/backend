from fastapi import FastAPI, File
from typing import Annotated
from src.contract.contract import parse_contract
from src.contract.model import Contract
import magic
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/contract", response_model=Contract)
def contract(file: Annotated[bytes, File()]):
    mime = magic.Magic(mime=True)
    return parse_contract(file, mime.from_buffer(file))
