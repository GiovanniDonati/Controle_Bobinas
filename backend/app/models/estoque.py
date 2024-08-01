from .bobina import Bobina
from .movimentacao import Movimentacao
from .historico import Historico
from datetime import datetime
import re

class Estoque:
    def __init__(self):
        self.__bobinas = []
        self.__historico = Historico()
        self.__enderecos_validos = self.__gerar_enderecos_validos()
        
    def __gerar_enderecos_validos(self):
        enderecos = []
        
        for letra in 'ABCD':
            for number in range(1, 96):
                enderecos.append(f'{letra}{number}')
                
        for number in range(17, 96):
            enderecos.append(f'E{number}')
    
        for number in range(47, 96):
            enderecos.append(f'F{number}')

        for number in range(82, 96):
            enderecos.append(f'G{number}')

        for letra in 'ABCDE':
            for number in range(1, 5):
                enderecos.append(f'G1-{letra}{number}')
        
        for letra in 'ABCD':
            for number in range(1, 6):
                enderecos.append(f'G2-{letra}{number}')
        
        for letra in 'AB':
            for number in range(1, 12):
                enderecos.append(f'G3-{letra}{number}')
        
        return enderecos

    def __endereco_ocupado(self, endereco):
        return any(bobina.endereco == endereco for bobina in self.__bobinas)

    def __lote_existente(self, lote):
        return any(bobina.lote == lote for bobina in self.__bobinas)
    
    def __endereco_valido(self, endereco):
        return endereco in self.__enderecos_validos

    def adicionar_bobina(self, bobina: Bobina):
        if not self.__endereco_valido(bobina.endereco):
            raise ValueError(f"Endereço {bobina.endereco} não é válido.")
        if self.__endereco_ocupado(bobina.endereco):
            raise ValueError(f"Endereço {bobina.endereco} já está ocupado por outra bobina.")
        if self.__lote_existente(bobina.lote):
            raise ValueError(f"Lote {bobina.lote} já existe.")
        self.__bobinas.append(bobina)
        self.__historico.adicionar_movimentacao(Movimentacao(bobina, 'Cadastro', datetime.now().strftime("%d-%m-%Y, %H:%M"), bobina.endereco))

    def remover_bobina(self, lote):
        bobina = self.buscar_bobina(lote)
        if bobina:
            self.__bobinas.remove(bobina)
            self.__historico.adicionar_movimentacao(Movimentacao(bobina, 'Baixa', datetime.now().strftime("%d-%m-%Y, %H:%M"), 'N/A'))
        else:
            raise ValueError(f"Bobina com lote {lote} não encontrada.")

    def mover_bobina(self, lote, novo_endereco):
        if not self.__endereco_valido(novo_endereco):
            raise ValueError(f"Endereço {novo_endereco} não é válido.")
        if self.__endereco_ocupado(novo_endereco):
            raise ValueError(f"Endereço {novo_endereco} já está ocupado por outra bobina.")
        bobina = self.buscar_bobina(lote)
        if bobina:
            self.__historico.adicionar_movimentacao(Movimentacao(bobina, 'Movimentação de estoque', datetime.now().strftime("%d-%m-%Y, %H:%M"), novo_endereco))
            bobina.endereco = novo_endereco
        else:
            raise ValueError(f"Bobina com lote {lote} não encontrada.")

    def mover_para_producao(self, lote):
        bobina = self.buscar_bobina(lote)
        if bobina:
            self.__historico.adicionar_movimentacao(Movimentacao(bobina, 'Produção', datetime.now().strftime("%d-%m-%Y, %H:%M"), 'Produção'))
            bobina.endereco = 'Produção'
        else:
            raise ValueError(f"Bobina com lote {lote} não encontrada.")

    def buscar_bobina(self, codigo):
        for bobina in self.__bobinas:
            if bobina.codigo == codigo:
                return bobina
        return None

    def obter_historico(self, codigo):
        return self.__historico.obter_historico_por_bobina(codigo)

    def verificar_estoque(self):
        def ordenar_enderecos(bobina):
            endereco = bobina.endereco
            partes = re.split(r'(-|\d+)', endereco)
            partes = [int(part) if part.isdigit() else part for part in partes]
            return partes
        
        bobinas_ordenadas = sorted(self.__bobinas, key=ordenar_enderecos)
        
        for bobina in bobinas_ordenadas:
            print(f"Endereço: {bobina.endereco}, Código: {bobina.codigo}, Lote: {bobina.lote}, Descrição: {bobina.descricao}, Metragem: {bobina.metragem}")
