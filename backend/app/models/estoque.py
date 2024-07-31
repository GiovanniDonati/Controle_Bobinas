from .bobina import Bobina
from .movimentacao import Movimentacao
from .historico import Historico
from datetime import datetime

class Estoque:
    def __init__(self):
        self.bobinas = []
        self.historico = Historico()

    def endereco_ocupado(self, endereco):
        return any(bobina.endereco == endereco for bobina in self.bobinas)

    def adicionar_bobina(self, bobina: Bobina):
        if self.endereco_ocupado(bobina.endereco):
            raise ValueError(f"Endereço {bobina.endereco} já está ocupado por outra bobina.")
        self.bobinas.append(bobina)
        self.historico.adicionar_movimentacao(Movimentacao(bobina, 'entrada', datetime.now(), bobina.endereco))

    def remover_bobina(self, codigo):
        bobina = self.buscar_bobina(codigo)
        if bobina:
            self.bobinas.remove(bobina)
            self.historico.adicionar_movimentacao(Movimentacao(bobina, 'saída', datetime.now(), 'N/A'))
        else:
            raise ValueError(f"Bobina com código {codigo} não encontrada.")

    def mover_bobina(self, codigo, novo_endereco):
        if self.endereco_ocupado(novo_endereco):
            raise ValueError(f"Endereço {novo_endereco} já está ocupado por outra bobina.")
        bobina = self.buscar_bobina(codigo)
        if bobina:
            self.historico.adicionar_movimentacao(Movimentacao(bobina, 'movimentação', datetime.now(), novo_endereco))
            bobina.endereco = novo_endereco
        else:
            raise ValueError(f"Bobina com código {codigo} não encontrada.")

    def mover_para_producao(self, codigo):
        bobina = self.buscar_bobina(codigo)
        if bobina:
            self.historico.adicionar_movimentacao(Movimentacao(bobina, 'produção', datetime.now(), 'Produção'))
            bobina.endereco = 'Produção'
        else:
            raise ValueError(f"Bobina com código {codigo} não encontrada.")

    def buscar_bobina(self, codigo):
        for bobina in self.bobinas:
            if bobina.codigo == codigo:
                return bobina
        return None

    def obter_historico(self, codigo):
        return self.historico.obter_historico_por_bobina(codigo)