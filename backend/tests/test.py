import flet as ft

def main(page: ft.Page):
    # Define views
    view1 = ft.View(name="view1", controls=[ft.Text("View 1")])
    view2 = ft.View(name="view2", controls=[ft.Text("View 2")])
    view3 = ft.View(name="view3", controls=[ft.Text("View 3")])

    # Add views to the page
    page.views.append(view1)
    page.views.append(view2)
    page.views.insert(1, view3)

    # Remove the first view
    page.views.remove(view1)

    # Print the total number of views
    total = len(page.views)
    print("Total de views:", total)

    # Run the application
    page.run()

ft.app(target=main)
