import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from datetime import datetime
from backend.app.models.bobina import Bobina
from backend.app.models.estoque import Estoque

estoque = Estoque()

def criar_bobina():
    endereco = input("Digite o endereço da bobina: ")
    codigo = input("Digite o código da bobina: ")
    descricao = input("Digite a descrição da bobina: ")
    lote = input("Digite o lote da bobina: ")
    metragem = float(input("Digite a metragem da bobina: "))
    data_entrada = datetime.now().strftime("%d-%m-%Y, %H:%M")

    try:
        nova_bobina = Bobina(endereco, codigo, descricao, lote, metragem, data_entrada)
        estoque.adicionar_bobina(nova_bobina)
        print("Bobina criada com sucesso!")
    except ValueError as e:
        print(f"Erro ao criar bobina: {e}")

def remover_bobina():
    codigo = input("Digite o código da bobina a ser removida: ")
    try:
        estoque.remover_bobina(codigo)
        print("Bobina removida com sucesso!")
    except ValueError as e:
        print(f"Erro ao remover bobina: {e}")

def mover_bobina():
    codigo = input("Digite o código da bobina a ser movida: ")
    novo_endereco = input("Digite o novo endereço da bobina: ")
    try:
        estoque.mover_bobina(codigo, novo_endereco)
        print("Bobina movida com sucesso!")
    except ValueError as e:
        print(f"Erro ao mover bobina: {e}")

def mover_para_producao():
    codigo = input("Digite o código da bobina a ser movida para produção: ")
    try:
        estoque.mover_para_producao(codigo)
        print("Bobina movida para produção com sucesso!")
    except ValueError as e:
        print(f"Erro ao mover bobina para produção: {e}")

def visualizar_historico():
    codigo = input("Digite o código da bobina para visualizar o histórico: ")
    historico = estoque.obter_historico(codigo)
    if not historico:
        print("Histórico não encontrado")
    else:
        for mov in historico:
            print(f"{mov.tipo} em {mov.data} para {mov.endereco}")

def verificar_estoque():
    estoque.verificar_estoque()

def main():
    while True:
        print("\n1. Criar Bobina")
        print("2. Remover Bobina")
        print("3. Mover Bobina")
        print("4. Mover Bobina para Produção")
        print("5. Visualizar Histórico de Bobina")
        print("6. Verificar Estoque")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_bobina()
        elif opcao == '2':
            remover_bobina()
        elif opcao == '3':
            mover_bobina()
        elif opcao == '4':
            mover_para_producao()
        elif opcao == '5':
            visualizar_historico()
        elif opcao == '6':
            verificar_estoque()
        elif opcao == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()