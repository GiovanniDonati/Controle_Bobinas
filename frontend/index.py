import flet as ft

def home_page(page: ft.Page):
    def navigate_to_main(e):
        page.controls.clear()
        main(page)
    
    page.controls.append(ft.Text("Bobinas em Produção"))
    page.controls.append(ft.ElevatedButton(text="Home", on_click=navigate_to_main))
    page.update()

def historic(page: ft.Page):
    def navigate_to_main(e):
        page.controls.clear()
        main(page)
    
    page.controls.append(ft.Text("Histórico de movimentações"))
    page.controls.append(ft.ElevatedButton(text="Home", on_click=navigate_to_main))
    page.update()

def main(page: ft.Page):
    page.title = "Controle de Bobinas"
    
    page.window_width = 400
    page.window_height = 400
    
    def navigate_to_home(e):
        page.controls.clear()
        home_page(page)
    
    def navigate_to_about(e):
        page.controls.clear()
        historic(page)
    
    page.controls.append(ft.ElevatedButton(text="Produção", on_click=navigate_to_home))
    page.controls.append(ft.ElevatedButton(text="Histórico", on_click=navigate_to_about))
    page.update()

ft.app(target=main)
