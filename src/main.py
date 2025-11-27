from fastapi import FastAPI, File
from typing import Annotated
from src.contract.contract import parse_contract
from src.contract.model import Contract
import magic
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/contract")
def contract(file: Annotated[bytes, File()]):
    import pdb; pdb.set_trace()

    mime = magic.Magic(mime=True)

    output = parse_contract(file, mime.from_buffer(file))
    return Contract.model_dump(output)
