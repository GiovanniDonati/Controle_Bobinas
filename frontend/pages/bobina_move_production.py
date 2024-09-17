# pages/bobina_move_production.py
import flet as ft
import requests

# Importe BACKEND_URL do arquivo principal (main.py)
from frontend.pages.config import BACKEND_URL

def page_bobina_mover_producao(page: ft.Page):
    page.title = "Mover para Produção"

    lote_field = ft.TextField(label="Lote da Bobina")
    mover_button = ft.ElevatedButton(
        text="Mover", on_click=lambda e: mover_para_producao_submit(page, lote_field)
    )
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Mover para Produção", size=20, weight=ft.FontWeight.BOLD),
                lote_field,
                mover_button,
                voltar_button,
            ]
        )
    )

def mover_para_producao_submit(page: ft.Page, lote_field):
    try:
        response = requests.put(
            f'{BACKEND_URL}/bobinas/{lote_field.value}/producao'
        )
        response.raise_for_status()
        page.snack_bar = ft.SnackBar(
            ft.Text("Bobina movida para produção com sucesso!")
        )
        lote_field.value = ""  # Limpar o campo após mover
        page.update()  # Atualizar a página para refletir o campo limpo
    except requests.exceptions.RequestException as e:
        page.snack_bar = ft.SnackBar(
            ft.Text(f"Erro ao mover bobina para produção: {e}")
        )
    page.open_snack_bar()
