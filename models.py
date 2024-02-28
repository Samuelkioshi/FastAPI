from typing import Optional
from pydantic import BaseModel, validator

class Viagem(BaseModel):
    id: Optional[int] = None
    descricao: str
    dias: int  
    noites: int  

    @validator('descricao')
    def validar_descricao(cls, value: str):
        # Validacao 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            print("A descrição deve ter pelo menos 3 palavras.")
            #raise ValueError('A descrição deve ter pelo menos 3 palavras.')
        # Validacao 2
        if value.islower():
            print("A descrição deve ser capitalizada")
            raise ValueError('A descrição deve ser capitalizada.')
        return value
viagens = [
    Viagem(id=1, descricao='Pacote para Ferando de Noronha', dias=15, noites=14),
    Viagem(id=2, descricao='Pacote para França', dias=14, noites=13),
]