from Models.GeneralModel import GeneralModel
from Models.ProductsModel import ProductsModel

Q={
    "register_sale":"INSERT INTO sales(code,lot,sale_price) VALUES (?,?,?)",
}

class SalesModel(GeneralModel):

    def __init__(self):
        self.__ProductsModel=ProductsModel()

    def register_sale(self, code:str, lot:int):
        product=self.__ProductsModel.read_product(code)
        if product!=[]:
            if lot<=product[0][5]:
                final_price=product[0][4]*lot
                resp=self.run_set_query(Q.get('register_sale'),(code,lot,final_price))
                if type(resp)==int:
                    status="Success" if (resp>0) else "No se realizó la venta"
                else:
                    status=resp
            else:
                status="No hay existencia suficiente para la venta"
        else:
            status="No existe ese producto"
        return status

