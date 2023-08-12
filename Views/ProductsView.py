from customtkinter import *
from tkinter import ttk,messagebox
from Controllers.ProductsController import ProductsController
from Resources.Custom_window import CustomToplevel
from Resources.Validations import Validations
cp = '#0D55B4'
cs= '#91C1FF'

class ProductsView(CustomToplevel,Validations):

    def __init__(self, app):
        self.app=app
        self.__ProductsController=ProductsController()
        self.app.geometry("975x550")

    def products(self, main):
        title=CTkLabel(self.app, text="Productos", bg_color=cp, width=974, height=55, font=("", 40))
        title.pack()

        mini_container=CTkFrame(self.app, width=20, height=50)
        mini_container.pack(side=LEFT, padx=30)

        add_button=CTkButton(mini_container, text="Registrar", width=150, height=50, command=self.add_product_form)
        add_button.pack(pady=10)

        edit_button=CTkButton(mini_container, text="Editar", width=150, height=50, command=self.edit_product_form)
        edit_button.pack()

        delete_button=CTkButton(mini_container, text="Eliminar", width=150, height=50, command=self.delete_product)
        delete_button.pack(pady=10)

        add_quantity_button=CTkButton(mini_container, text="Añadir Existencia", width=150, height=50, command=self.add_existence_form)
        add_quantity_button.pack()

        CTkLabel(mini_container, text="").pack()

        CTkLabel(mini_container, text="Buscar por codigo").pack()
        self.search_entry=CTkEntry(mini_container, width=150, height=30)
        self.search_entry.pack()

        search_button=CTkButton(mini_container, text="Buscar", width=150, height=50, command=self.search_product)
        search_button.pack(pady=5)

        return_button=CTkButton(mini_container, text="Volver", width=150, height=50, command=main)
        return_button.pack(pady=10)

        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background=cs, relief="flat")
        style.map("Treeview.Heading", background=[('active',cs)])

        self.grid = ttk.Treeview(self.app, columns=("#1","#2","#3","#4","#5"), show="headings")
        self.grid.place(x=255, y=80, width=700, height=450)

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
        self.products_form("Añadir", self.add_product)

    def add_product(self):
        name=self.name_entry.get()
        code=self.code_entry.get()
        p_p=self.p_p_entry.get()
        s_p=self.s_p_entry.get()
        amount=self.amount_entry.get()

        if self.validate_entrys(name,code,p_p,s_p,amount):
            status=self.__ProductsController.create_product(name,code,p_p,s_p,amount)
            if status=="Success":
                messagebox.showinfo(title="Ok", message="Insertado")
                self.form.destroy()
                self.get_products()
            else:
                messagebox.showerror(title="Error", message=status)
        else:
            messagebox.showerror(title="Alerta", message="Campos vacíos")

    def edit_product_form(self):
        try:
            code=self.grid.item(self.grid.selection())["values"][1]
        except IndexError:
            messagebox.showinfo(title="Alerta", message="Elija un registro, por favor")
            return
        data_update=self.__ProductsController.read_product(code)
        self.products_form("Actualizar", self.edit_product)
        self.id=data_update[0][0]
        self.name_entry.insert(0, data_update[0][1])
        self.code_entry.insert(0, data_update[0][2])
        self.p_p_entry.insert(0, data_update[0][3])
        self.s_p_entry.insert(0, data_update[0][4])
        self.amount_entry.insert(0, data_update[0][5])

    def edit_product(self):
        id=self.id
        name=self.name_entry.get()
        code=self.code_entry.get()
        p_p=self.p_p_entry.get()
        s_p=self.s_p_entry.get()
        amount=self.amount_entry.get()

        if self.validate_entrys(name,code,p_p,s_p,amount,id):
            status=self.__ProductsController.update_product(id,name,code,p_p,s_p,amount)
            if status=="Success":
                messagebox.showinfo(title="Ok", message="Actualizado")
                self.form.destroy()
                self.get_products()
            else:
                messagebox.showerror(title="Error", message=status)
        else:
            messagebox.showwarning(title="Alerta", message="Campos vacíos")

    def delete_product(self):
        id=self.grid.item(self.grid.selection())["text"]
        if id=="":
            messagebox.showwarning(title="Alerta", message="Elija un registro, por favor")
            return
        if messagebox.askquestion(title="Alerta", message="Desea eliminar")=="yes":
            status=self.__ProductsController.delete_product(id)
            if status=="Success":
                messagebox.showinfo(title="Ok", message="Eliminado Correctamente")
                self.get_products()
            else:
                messagebox.showerror(title="Error", message=status)
        else:
            return

    def search_product(self):
        if self.validate_entrys(self.search_entry.get())!="":
            data=self.__ProductsController.read_product(self.search_entry.get())
            self.get_products(data)
        else:
            self.get_products()

    def products_form(self, title:str, function):
        self.form=CustomToplevel(self.app)
        self.form.geometry("274x450")

        title=CTkLabel(self.form, text=f"{title} Producto", bg_color=cp, width=274, height=35, font=("", 20))
        title.pack()

        validate_alphanumerics=self.form.register(self.validate_len_and_alphanumerics)
        validate_numerics=self.form.register(self.validate_len_and_numerics)

        CTkLabel(self.form, text="Nombre").pack()
        self.name_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_alphanumerics, '%P', 100), justify=CENTER)
        self.name_entry.pack()
        self.name_entry.focus()
        CTkLabel(self.form, text="Codigo de Barra").pack()
        self.code_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_numerics, '%P', 30), justify=CENTER)
        self.code_entry.pack()
        CTkLabel(self.form, text="Precio compra").pack()
        self.p_p_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_numerics, '%P', 10), justify=CENTER)
        self.p_p_entry.pack()
        CTkLabel(self.form, text="Precio Venta").pack()
        self.s_p_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_numerics, '%P', 10), justify=CENTER)
        self.s_p_entry.pack()
        CTkLabel(self.form, text="Existencia").pack()
        self.amount_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_numerics, '%P', 10), justify=CENTER)
        self.amount_entry.pack()

        submit=CTkButton(self.form, text='Enviar', width=140, height=40, command=function)
        submit.pack(pady=15)

    def add_existence_form(self):
        try:
            code=self.grid.item(self.grid.selection())["values"][1]
        except IndexError:
            messagebox.showinfo(title="Alerta", message="Elija un registro, por favor")
            return

        data=self.__ProductsController.read_product(code)
        self.form=CustomToplevel(self.app)
        self.form.geometry("274x160")

        title=CTkLabel(self.form, text="Añadir Existencia", bg_color=cp, width=274, height=35, font=("", 20))
        title.pack()

        validate_numerics=self.form.register(self.validate_len_and_numerics)

        self.amount_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_numerics, '%P', 10), justify=CENTER)
        self.amount_entry.pack(pady=15)
        self.amount_entry.insert(0, data[0][5])

        send_Button = CTkButton(self.form, width=140, height=40, text='Agregar')
        send_Button.pack()
