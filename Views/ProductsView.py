from customtkinter import *
from tkinter import ttk
from Resources.Custom_window import CustomToplevel
from Controllers.ProductsController import ProductsController
cp = '#0D55B4'
cs= '#91C1FF'

class ProductsView(CustomToplevel):

    def __init__(self, app):
        self.app=app
        self.__ProductsController=ProductsController()
        self.app.geometry("975x550")

    def products(self):

        title=CTkLabel(self.app, text="Productos", bg_color=cp, width=974, height=55, font=("", 40))
        title.pack()

        miniContainer = CTkFrame(self.app, width=20, height=50)
        miniContainer.pack(side=LEFT, padx=30)

        btnRegister = CTkButton(miniContainer, text="Registrar", command=self.form, width=150, height=50)
        btnRegister.pack(pady=10)
        btnEdit = CTkButton(miniContainer, text="Editar", width=150, height=50)
        btnEdit.pack()
        btnDelete = CTkButton(miniContainer, text="Eliminar", width=150, height=50)
        btnDelete.pack(pady=10)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background=cs, relief="flat")
        style.map("Treeview.Heading", background=[('active',cs)])

        self.grid = ttk.Treeview(self.app, columns=("#1","#2","#3","#4","#5"), show="headings")
        self.grid.place(x=275, y=120, width=600, height=380)

        self.grid.column("#0", width=0, anchor=CENTER)
        self.grid.column("#1",width=50, anchor=CENTER)
        self.grid.column("#2",width=35, anchor=CENTER)
        self.grid.column("#3",width=30, anchor=CENTER)
        self.grid.column("#4",width=30, anchor=CENTER)
        self.grid.column("#5",width=25, anchor=CENTER)

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

    def form(self):
        x= CustomToplevel(self.app)
        x.geometry("274x350")
        title = CTkLabel(x, text="Registrar", bg_color=cp, width=274, height=35, font=("", 20))
        title.pack()
        entryName = CTkEntry(x, placeholder_text='Nombre', width=140, height=40)
        entryName.pack(pady=8)
        entryPP = CTkEntry(x, placeholder_text='Precio de Compra', width=140, height=40)
        entryPP.pack()
        entryPV = CTkEntry(x, placeholder_text='Precio de Venta', width=140, height=40)
        entryPV.pack(pady=8)
        amount = CTkEntry(x, placeholder_text='Existencia', width=140, height=40)
        amount.pack()
        code = CTkEntry(x, placeholder_text='Codigo', width=140, height=40)
        code.pack(pady=8)
        btnSend = CTkButton(x, text='Enviar', width=140, height=40)
        btnSend.pack(pady=10)
        

