from Resources.Includes.Modules import *
from Resources.Includes.Custom_window import CustomToplevel
from Resources.Includes.Validations import Validations
from Controllers.StoreController import StoreController

class StoreView(CustomToplevel,Validations):

    def __init__(self, app):
        self.app=app
        self.__StoreController=StoreController()
        self.app.geometry("975x550")

    def store(self, main):
        title=CTkLabel(self.app, text="Almacén", bg_color=cp, width=974, height=55, font=("", 40))
        title.pack()

        mini_container=CTkFrame(self.app, width=20, height=50)
        mini_container.pack(side=LEFT, padx=30)

        CTkLabel(mini_container, text="Ventas por Fecha").pack()
        self.search_entry=DateEntry(mini_container)
        self.search_entry.pack()

        search_button=CTkButton(mini_container, text="Buscar", width=150, height=50, command=self.get_sales_of_the_day)
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
        self.grid.heading("#2", text="Código", anchor=CENTER)
        self.grid.heading("#3", text="Cantidad Vendida", anchor=CENTER)
        self.grid.heading("#4", text="Total", anchor=CENTER)
        self.grid.heading("#5", text="Fecha", anchor=CENTER)

        self.get_sales()

    def get_sales(self, data:list=[]):
        childrens=self.grid.get_children()
        for children in childrens:
            self.grid.delete(children)
        if data==[]:
            data=self.__StoreController.read_sales()
        i=0
        for sale in data:
            self.grid.insert('', i, text=[sale[0]], values=(sale[1],sale[2],sale[3],sale[4],sale[5]))
            i+=1

    def get_sales_of_the_day(self):
        date=self.search_entry.get_date()
        data=self.__StoreController.read_sales_of_the_day(date)
        self.get_sales(data)