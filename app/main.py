from typing import List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class Stats(BaseModel):
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int

class Pokemon(BaseModel):
    id: int
    name: str
    type: List[str]
    stats: Stats


db = []

app = FastAPI()

@app.post("/pokemons/", status_code=201)
def create_pokemon(pokemon: Pokemon):
    db.append(pokemon)
    return pokemon


@app.get("/pokemons/", response_model=List[Pokemon])
def list_pokemons():
    return db


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)