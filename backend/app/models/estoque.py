from .bobina import Bobina
from .movimentacao import Movimentacao
from .historico import Historico
from datetime import datetime

class Estoque:
    def __init__(self):
        self.bobinas = []
        self.historico = Historico()

    def adicionar_bobina(self, bobina: Bobina):
        self.bobinas.append(bobina)
        self.historico.adicionar_movimentacao(Movimentacao(bobina, 'entrada', datetime.now(), bobina.endereco))

    def remover_bobina(self, codigo):
        bobina = self.buscar_bobina(codigo)
        if bobina:
            self.bobinas.remove(bobina)
            self.historico.adicionar_movimentacao(Movimentacao(bobina, 'saída', datetime.now(), 'N/A'))

    def mover_bobina(self, codigo, novo_endereco):
        bobina = self.buscar_bobina(codigo)
        if bobina:
            self.historico.adicionar_movimentacao(Movimentacao(bobina, 'movimentação', datetime.now(), novo_endereco))
            bobina.endereco = novo_endereco

    def mover_para_producao(self, codigo):
        bobina = self.buscar_bobina(codigo)
        if bobina:
            self.historico.adicionar_movimentacao(Movimentacao(bobina, 'produção', datetime.now(), 'Produção'))
            bobina.endereco = 'Produção'

    def buscar_bobina(self, codigo):
        for bobina in self.bobinas:
            if bobina.codigo == codigo:
                return bobina
        return None

    def obter_historico(self, codigo):
        return self.historico.obter_historico_por_bobina(codigo)
