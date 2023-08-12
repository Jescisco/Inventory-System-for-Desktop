from customtkinter import *
cp = '#0D55B4'

class MainView():

    def __init__(self, app):
        self.app = app

        title=CTkLabel(self.app, text="Inventario", bg_color=cp, width=574, height=55, font=("", 40))
        title.pack()

        container=CTkFrame(self.app, bg_color='transparent', height=500, width=400)
        container.pack(pady=70)

        products_button=CTkButton(container, text='Productos', height=50, width= 150, command=lambda:self.products_view(container))
        products_button.pack(pady=10)

        sales_button=CTkButton(container, text='Ventas', height=50, width= 150)
        sales_button.pack(pady=10)

    def products_view(self, container):
        from Views.ProductsView import ProductsView
        self.clean_cont(container)
        products_view=ProductsView(self.app)
        products_view.products(container)

    def clean_cont(self, container):
        for widget in container.winfo_children():
            widget.destroy()