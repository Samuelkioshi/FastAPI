from typing import Dict, List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from time import sleep
from models import Viagem
from models import viagens


def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)

app = FastAPI(
    title='API de Viagens',
    version='0.0.1',
    description='Uma API Fast'
)

@app.get('/viagens',
         description='Retorna todos os viagens ou uma lista vazia.',
         summary='Retorna todos os viagens',
         response_model=List[Viagem],
         response_description='Viagens encontrados com sucesso.')
async def get_viagens(db: Any = Depends(fake_db)):
    return viagens

@app.post('/viagens', status_code=status.HTTP_201_CREATED, response_model=Viagem)
async def post_viagem(viagem: Viagem):
    next_id: int = len(viagens) + 1
    viagem.id = next_id
    viagens.append(viagem)
    return viagem

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)