from Models.SalesModel import SalesModel

class SalesController(SalesModel):

    def register_sale(self, code:str, lot:int, price:int):
        return super().register_sale(code,lot,price)