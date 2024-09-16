# pages/bobina_history.py
import flet as ft
import requests

# Importe BACKEND_URL do arquivo principal (main.py)
from main import BACKEND_URL 

def page_bobina_historico(page: ft.Page):
    page.title = "Visualizar Histórico"

    lote_field = ft.TextField(label="Lote da Bobina")
    historico_text = ft.Text("")
    visualizar_button = ft.ElevatedButton(
        text="Visualizar",
        on_click=lambda e: visualizar_historico_submit(
            page, lote_field, historico_text
        ),
    )
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Visualizar Histórico", size=20, weight=ft.FontWeight.BOLD),
                lote_field,
                visualizar_button,
                historico_text,
                voltar_button,
            ]
        )
    )

def visualizar_historico_submit(page: ft.Page, lote_field, historico_text):
    try:
        response = requests.get(
            f'{BACKEND_URL}/bobinas/{lote_field.value}/historico'
        )
        response.raise_for_status()
        historico = response.json()
        historico_formatado = "\n".join(
            [
                f"Data: {item['date_mov']} - Tipo: {item['tipo_mov']} - Endereço Antigo: {item['endereco_antigo']} - Metragem Antiga: {item['metragem_antiga']} - Nova Metragem: {item['nova_metragem']}"
                for item in historico
            ]
        )
        historico_text.value = historico_formatado
    except requests.exceptions.RequestException as e:
        historico_text.value = f"Erro ao obter histórico: {e}"
    page.update()
