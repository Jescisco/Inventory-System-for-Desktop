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
        pass