from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Characteristics(BaseModel):
    ram_memory: int
    rom_memory: int


class Phone(BaseModel):
    identifier: str
    model: str
    characteristics: Characteristics

phones = []

@app.get("/health")
def health_check():
    return "Ok"

@app.post("/phones", status_code=201)
async def create_phone(phone: Phone):
    phones.append(phone)
    return phone

@app.get("/phones", response_model=List[Phone])
async def get_phones():
    return phones

@app.get("/phones/{id}")
async def get_phone(id: str):
    for phone in phones:
        if phone.identifier == id:
            return phone
    raise HTTPException(status_code=404, detail="telephone non trouvé")

@app.put("/phones/{id}/characteristics")
async def update_characteristics(id: str, characteristics: Characteristics):
    for phone in phones:
        if phone.identifier == id:
            phone.characteristics = characteristics
            return {"message": "Characteristiques mis a jour succes"}