from customtkinter import *
cp = '#0D55B4'

class MainView():

    def __init__(self, app):
        self.app=app
        self.main()

    def main(self):

        self.clean_window()
        self.app.geometry("274x420")

        title=CTkLabel(self.app, text="Inventario", bg_color=cp, width=574, height=55, font=("", 40))
        title.pack()

        container=CTkFrame(self.app, bg_color='transparent', height=420, width=274)
        container.pack(pady=70)

        products_button=CTkButton(container, text='Productos', height=50, width= 150, command=self.products_view)
        products_button.pack(pady=10)

        sales_button=CTkButton(container, text='Ventas', height=50, width= 150, command=self.sales_view)
        sales_button.pack(pady=10)

        store_button=CTkButton(container, text='Almacen', height=50, width= 150)
        store_button.pack(pady=10)

    def products_view(self):
        from Views.ProductsView import ProductsView
        self.clean_window()
        products_view=ProductsView(self.app)
        products_view.products(self.main)

    def sales_view(self):
        from Views.SalesView import SalesView
        self.clean_window()
        sales_view=SalesView(self.app)
        sales_view.sales(self.main)

    def clean_window(self):
        for widget in self.app.winfo_children():
            widget.destroy()