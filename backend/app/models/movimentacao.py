from datetime import datetime
from .bobina import Bobina

class Movimentacao:
    def __init__(self, bobina: Bobina, tipo: str, data: datetime, localizacao: str):
        self.bobina = bobina
        self.tipo = tipo
        self.data = data
        self.localizacao = localizacao
