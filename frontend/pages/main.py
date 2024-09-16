import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import flet as ft
from pages.bobina_create import page_bobina_creator
from pages.bobina_remove import page_bobina_remover
from pages.bobina_move import page_bobina_mover
from pages.bobina_move_production import page_bobina_mover_producao
from pages.bobina_history import page_bobina_historico
from pages.bobina_stock import page_bobina_estoque

# Substitua 'http://seu_backend:8000' pela URL real do seu backend
BACKEND_URL = 'http://localhost:5000'  # geralmente Flask usa a porta 5000 por padrão

def page_home(page: ft.Page):
    page.title = "Controle de Bobinas"
    page.window.maximized = False
    page.window.width = 600
    page.window.height = 800

    page.add(
        ft.Column(
            [
                ft.ElevatedButton(text="Criar Bobina", on_click=lambda _: page.go('/criar_bobina')),
                ft.ElevatedButton(text="Remover Bobina", on_click=lambda _: page.go('/remover_bobina')),
                ft.ElevatedButton(text="Mover Bobina", on_click=lambda _: page.go('/mover_bobina')),
                ft.ElevatedButton(text="Mover para Produção", on_click=lambda _: page.go('/mover_para_producao')),
                ft.ElevatedButton(text="Visualizar Histórico", on_click=lambda _: page.go('/visualizar_historico')),
                ft.ElevatedButton(text="Visualizar Estoque", on_click=lambda _: page.go('/vizualizar_bobinas'))
            ]
        )
    )


def main(page: ft.Page):
    page.on_route_change = lambda e: page.views.clear()
    page.views.append(
        ft.View(
            "/",
            [
                ft.View(
                    "/",
                    [
                        page_home
                    ],
                ),
                ft.View(
                    "/criar_bobina",
                    [
                        page_bobina_creator
                    ],
                ),
                ft.View(
                    "/remover_bobina",
                    [
                        page_bobina_remover
                    ],
                ),
                ft.View(
                    "/mover_bobina",
                    [
                        page_bobina_mover
                    ],
                ),
                ft.View(
                    "/mover_para_producao",
                    [
                        page_bobina_mover_producao
                    ],
                ),
                ft.View(
                    "/visualizar_historico",
                    [
                        page_bobina_historico
                    ],
                ),
                ft.View(
                    "/vizualizar_bobinas",
                    [
                        page_bobina_estoque
                    ],
                ),
            ],
        )
    )
    page.go(page.route)

ft.app(target=main, view=ft.WEB_BROWSER)
