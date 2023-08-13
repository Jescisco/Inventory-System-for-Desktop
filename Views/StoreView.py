from customtkinter import *
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from Controllers.StoreController import StoreController
from Resources.Custom_window import CustomToplevel
from Resources.Validations import Validations
cp = '#0D55B4'
cs= '#91C1FF'

class StoreView(CustomToplevel,Validations):

    def __init__(self, app):
        self.app=app
        self.__StoreController=StoreController()
        self.app.geometry("975x550")

    def store(self, main):
        pass