from customtkinter import *
from tkinter import ttk
from Controllers.ProductsController import ProductsController
cp = '#0D55B4'
cs= '#91C1FF'

class ProductsView():

    def __init__(self, app):
        self.app=app
        self.__ProductsController=ProductsController()
        self.app.geometry("975x550")

    def products(self):
        title=CTkLabel(self.app, text="Productos", bg_color=cp, width=974, height=55, font=("", 40))
        title.pack()

        mini_container=CTkFrame(self.app, width=20, height=50)
        mini_container.pack(side=LEFT, padx=20)

        add_button=CTkButton(mini_container, text="Registrar", width=150, height=50, command=self.add_product_form)
        add_button.pack(pady=10)

        edit_button=CTkButton(mini_container, text="Editar", width=150, height=50)
        edit_button.pack()

        delete_button=CTkButton(mini_container, text="Eliminar", width=150, height=50)
        delete_button.pack(pady=10)

        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background=cs, relief="flat")
        style.map("Treeview.Heading", background=[('active',cs)])

        self.grid = ttk.Treeview(self.app, columns=("#1","#2","#3","#4","#5"), show="headings")
        self.grid.place(x=275, y=120, width=600, height=380)

        self.grid.column("#0", width=0, anchor=CENTER)
        self.grid.column("#1",width=30, anchor=CENTER)
        self.grid.column("#2",width=45, anchor=CENTER)
        self.grid.column("#3",width=35, anchor=CENTER)
        self.grid.column("#4",width=35, anchor=CENTER)
        self.grid.column("#5",width=45, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="Nombre", anchor=CENTER)
        self.grid.heading("#2", text="Codigo", anchor=CENTER)
        self.grid.heading("#3", text="Precio Compra", anchor=CENTER)
        self.grid.heading("#4", text="Precio Venta", anchor=CENTER)
        self.grid.heading("#5", text="Existencia", anchor=CENTER)

        self.get_products()

    def get_products(self, data:list=[]):
        records=self.grid.get_children()
        for children in records:
            self.grid.delete(children)
        if data==[]:
            data=self.__ProductsController.read_product()
        i=0
        for product in data:
            self.grid.insert('', i, text=product[0], values=(product[1],product[2],product[3],product[4],product[5]))

    def add_product_form(self):
        self.form("Añadir", self.add_product)

    def add_product(self):
        pass

    def edit_product_form(self):
        pass

    def edit_product(self):
        pass

    def delete_product(self):
        pass

    def form(self, title:str, function):
        pass

