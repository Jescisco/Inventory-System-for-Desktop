from customtkinter import *
cp = '#0D55B4'
class MainView():
    def __init__(self, app):
        self.app = app

        title = CTkLabel(self.app, text="Inventario", bg_color=cp, width=574, height=55, font=("", 40))
        title.pack()

        frame = CTkFrame(self.app, bg_color='transparent', height=500, width=400)
        frame.pack(pady=70)

        btn1 = CTkButton(frame, text='Productos', height=50, width= 150)
        btn1.pack(pady=10)
        btn2 = CTkButton(frame, text='Ventas', height=50, width= 150)
        btn2.pack(pady=10)


        