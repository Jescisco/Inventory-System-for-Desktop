from Resources.Includes.Modules import *
from Resources.Includes.Custom_window import CustomToplevel
from Resources.Includes.Validations import Validations
from Controllers.SalesController import SalesController
from Controllers.ProductsController import ProductsController

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

        self.search_entry=CTkEntry(mini_container, width=150, height=30)
        self.search_entry.pack()

        add_button=CTkButton(mini_container, text="Añadir Producto", width=150, height=50, command=lambda:self.add_product(self.search_entry.get(),1,0))
        add_button.pack(pady=10)

        update_amount_button=CTkButton(mini_container, text="Añadir Cantidad", width=150, height=50, command=self.update_amount_product)
        update_amount_button.pack(pady=10)

        delete_button=CTkButton(mini_container, text="Eliminar", width=150, height=50, command=self.delete_product)
        delete_button.pack(pady=10)

        register_sale_button=CTkButton(mini_container, text="Completar Venta", width=150, height=50, command=self.complete_invoice)
        register_sale_button.pack(pady=10)

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
        self.grid.column("#3",width=45, anchor=CENTER)
        self.grid.column("#4",width=45, anchor=CENTER)
        self.grid.column("#5",width=45, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="Código", anchor=CENTER)
        self.grid.heading("#2", text="Nombre", anchor=CENTER)
        self.grid.heading("#3", text="Precio", anchor=CENTER)
        self.grid.heading("#4", text="Cantidad", anchor=CENTER)
        self.grid.heading("#5", text="Existencia", anchor=CENTER)

    def add_product(self, product, amount:int, option:int, final_price:int=0):
        if product!="":
            product=self.__ProductsController.read_product(product)
            if product[0][5]>=int(amount) and product!=[]:
                if option==0:
                    price=product[0][4]
                if option==1:
                    if int(final_price)==0:
                        price=int(amount)*int(product[0][4])
                    else:
                        price=final_price
                i=0
                self.grid.insert('', i, text=product[0][0], values=(product[0][2],product[0][1],price,amount,product[0][5]))
                i+=1
            else:
                messagebox.showwarning(title="Alerta",message="No hay existencia de ese producto o no existe")
        else:
            messagebox.showwarning(title="Alerta",message="Ingrese algún código, por favor")
        self.search_entry.delete(0, END)

    def update_amount_product(self):
        try:
            row=self.grid.selection()
            code=self.grid.item(self.grid.selection())["values"][0]
            price=self.grid.item(self.grid.selection())["values"][2]
            amount=self.grid.item(self.grid.selection())["values"][3]
            self.form=CustomToplevel(self.app)
            self.form.geometry("274x450")

            title=CTkLabel(self.form, text="Añadir Cantidad", bg_color=cp, width=274, height=35, font=("", 20))
            title.pack()

            validate_numerics=self.form.register(self.validate_len_and_numerics)

            CTkLabel(self.form, text="Cantidad").pack()
            amount_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_numerics, '%P', 100), justify=CENTER)
            amount_entry.pack()
            amount_entry.focus()
            amount_entry.insert(0, amount)

            CTkLabel(self.form, text="Precio").pack()
            price_entry=IntVar()
            price_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_numerics, '%P', 100), justify=CENTER)
            price_entry.pack()
            price_entry.insert(0, price)

            submit_button=CTkButton(self.form, text='Añadir', width=140, height=40, command=lambda:self.update_amount(row,code,amount_entry.get(),price_entry.get(),price))
            submit_button.pack(pady=15)
        except IndexError:
            messagebox.showwarning(title="Alerta", message="Elija un registro, por favor")
            return

    def update_amount(self, row, code, amount, price:int, old_price:int):
        self.grid.delete(row)
        self.form.destroy()
        if int(price)==int(old_price):
            self.add_product(code,amount,1)
        else:
            self.add_product(code,amount,1,price)

    def delete_product(self):
        try:
            product=self.grid.selection()
            self.grid.delete(product)
        except IndexError:
            messagebox.showwarning(title="Alerta", message="Elija un registro, por favor")
            return

    def select_products(self):
        products=[]
        for item in self.grid.get_children():
            products.append(self.grid.item(item, "values"))
        return products

    def complete_invoice(self):
        total_price,products=0,self.select_products()
        for product in products:
            total_price+=int(product[2])

        self.form=CustomToplevel(self.app)
        self.form.geometry("274x450")

        title=CTkLabel(self.form, text="Completar Factura", bg_color=cp, width=274, height=35, font=("", 20))
        title.pack()

        validate_numerics=self.form.register(self.validate_len_and_numerics)

        CTkLabel(self.form, text="Total a Pagar").pack()
        self.total_price_entry=CTkEntry(self.form, width=140, height=40, validate="key", validatecommand=(validate_numerics, '%P', 100), justify=CENTER)
        self.total_price_entry.pack()
        self.total_price_entry.focus()
        self.total_price_entry.insert(0, total_price)

        submit_button=CTkButton(self.form, text='Enviar', width=140, height=40, command=self.save_sales)
        submit_button.pack(pady=15)

    def save_sales(self):
        products=self.select_products()
        for product in products:
            status=self.__SalesController.register_sale(product[0],int(product[3]),product[2])
            if status=="Success":
                continue
            else:
                messagebox.showerror(title="Error",message="Ocurrió un error")
                return
        messagebox.showinfo(title="Ok",message="Venta Completada")
        self.clean_treeview()
        self.form.destroy()

    def clean_treeview(self):
        for children in self.grid.get_children():
            self.grid.delete(children)