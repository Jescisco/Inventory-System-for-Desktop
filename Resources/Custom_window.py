from customtkinter import *

class CustomToplevel(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grab_set()  # Deshabilitar la interacción con otros elementos
        self.attributes("-topmost", True)  # Mantener la ventana en la parte superior
        self.wait_visibility()  # Esperar a que la ventana sea visible
        self.focus_force()  # Darle el enfoque a la ventana
        self.bind("<Button>", self.disable_window)  # Capturar los clics fuera de la ventana

    def disable_window(self, event):
        pass








