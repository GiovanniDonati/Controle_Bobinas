# pages/bobina_stock.py
import flet as ft
import requests

# Importe BACKEND_URL do arquivo principal (main.py)
from main import BACKEND_URL 

def page_bobina_estoque(page: ft.Page):
    page.title = "Estoque de Bobinas"

    bobinas_text = ft.Text("")
    visualizar_button = ft.ElevatedButton(
        text="Visualizar",
        on_click=lambda e: vizualizar_bobinas_submit(page, bobinas_text),
    )
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Estoque de Bobinas", size=20, weight=ft.FontWeight.BOLD),
                visualizar_button,
                bobinas_text,
                voltar_button,
            ]
        )
    )

def vizualizar_bobinas_submit(page: ft.Page, bobinas_text):
    try:
        response = requests.get(f'{BACKEND_URL}/bobinas')
        response.raise_for_status()
        bobinas = response.json()
        bobinas_formatado = "\n".join(
            [
                f"Lote: {item['id_lote']} - Cortina: {item['cortina_id_codigo']} - Endereço: {item['endereco_id_endereco']} - Metragem: {item['metragem']}"
                for item in bobinas
            ]
        )
        bobinas_text.value = bobinas_formatado
    except requests.exceptions.RequestException as e:
        bobinas_text.value = f"Erro ao obter estoque de bobinas: {e}"
    page.update()
