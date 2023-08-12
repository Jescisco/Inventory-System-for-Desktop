from customtkinter import *
from tkinter import ttk,messagebox
from Controllers.SalesController import SalesController
from Controllers.ProductsController import ProductsController
from Resources.Custom_window import CustomToplevel
from Resources.Validations import Validations
cp = '#0D55B4'
cs= '#91C1FF'

class SalesView(CustomToplevel,Validations):

    def __init__(self, app):
        self.app=app
        self.__SalesController=SalesController()
        self.__ProductsController=ProductsController()
        self.app.geometry("975x550")

    def sales(self, main):
        title=CTkLabel(self.app, text="Facturación", bg_color=cp, width=974, height=55, font=("", 40))
        title.pack()

        mini_container=CTkFrame(self.app, width=20, height=50)
        mini_container.pack(side=LEFT, padx=30)

        add_button=CTkButton(mini_container, text="Añadir Producto", width=150, height=50, command=self.add_product)
        add_button.pack(pady=10)

        self.search_entry=CTkEntry(mini_container, width=150, height=30)
        self.search_entry.pack()

        delete_button=CTkButton(mini_container, text="Eliminar", width=150, height=50, command=self.delete_product)
        delete_button.pack(pady=10)

        return_button=CTkButton(mini_container, text="Volver", width=150, height=50, command=self.register_sale)
        return_button.pack(pady=10)

        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background=cs, relief="flat")
        style.map("Treeview.Heading", background=[('active',cs)])

        self.grid = ttk.Treeview(self.app, columns=("#1","#2","#3","#4"), show="headings")
        self.grid.place(x=255, y=80, width=700, height=450)

        self.grid.column("#0", width=0, anchor=CENTER)
        self.grid.column("#1",width=30, anchor=CENTER)
        self.grid.column("#2",width=45, anchor=CENTER)
        self.grid.column("#3",width=45, anchor=CENTER)
        self.grid.column("#4",width=45, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="Código", anchor=CENTER)
        self.grid.heading("#2", text="Nombre", anchor=CENTER)
        self.grid.heading("#3", text="Precio", anchor=CENTER)
        self.grid.heading("#4", text="Cantidad", anchor=CENTER)

    def add_product(self):
        code=self.search_entry.get()
        if code!="":
            product=self.__ProductsController.read_product(code)
            i=-1
            if product!=[]:
                self.grid.insert('', i, text=product[0][0], values=(product[0][2],product[0][1],product[0][4],1))
            else:
                messagebox.showerror(title="Error",message="No existe ese producto")
        else:
            messagebox.showwarning(title="Alerta",message="Ingrese algún código, por favor")
        self.search_entry.delete(0, END)

    def delete_product(self):
        try:
            product=self.grid.selection()
            self.grid.delete(product)
        except IndexError:
            messagebox.showinfo(title="Alerta", message="Elija un registro, por favor")
            return

    def register_sale(self):
        for item in self.grid.get_children():
            valores=self.grid.item(item, "values")
            status=self.__SalesController.register_sale(valores[0],valores[3])
            print(status)
            if status=="Success":
                continue
            else:
                messagebox.showerror(title="Error",message="Ocurrió un error")
                return