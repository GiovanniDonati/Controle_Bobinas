from .movimentacao import Movimentacao

class Historico:
    def __init__(self):
        self.__movimentacoes = []

    def adicionar_movimentacao(self, movimentacao: Movimentacao):
        self.__movimentacoes.append(movimentacao)

    def obter_historico_por_bobina(self, codigo):
        return [mov for mov in self.__movimentacoes if mov.bobina.codigo == codigo]
