from .movimentacao import Movimentacao

class Historico:
    def __init__(self):
        self.movimentacoes = []

    def adicionar_movimentacao(self, movimentacao: Movimentacao):
        self.movimentacoes.append(movimentacao)

    def obter_historico_por_bobina(self, codigo):
        historico_bobina = [mov for mov in self.movimentacoes if mov.bobina.codigo == codigo]
        return historico_bobina
