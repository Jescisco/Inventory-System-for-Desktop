from Models.GeneralModel import GeneralModel
from Models.ProductsModel import ProductsModel
from Resources.Includes.Querys import SALES_QUERYS as Q

class SalesModel(GeneralModel):

    def __init__(self):
        self.__ProductsModel=ProductsModel()

    def register_sale(self, code:str, lot:int):
        product=self.__ProductsModel.read_product(code)
        if product!=[]:
            if self.run_get_query(Q.get("verify_product"),(code,))==[]:
                #Insertar Venta del Producto en el día
                resp=self.run_set_query(Q.get("register_sale"),(code,lot,product[0][4]))
                if type(resp)==int:
                    if resp>0:
                        resp=self.__ProductsModel.substract_product_existence(product[0][0])
                        status="Success" if (resp=="Success") else "No se insertó"
                    else:
                        status="No se insertó"
                else:
                    status=resp
            else:
                #Actualizar Venta del Producto en el día
                resp=self.run_set_query(Q.get("update_sale"),(lot,product[0][4],code))
                if type(resp)==int:
                    if resp>0:
                        resp=self.__ProductsModel.substract_product_existence(product[0][0])
                        status="Success" if (resp=="Success") else "No se insertó"
                    else:
                        status="No se insertó"
                else:
                    status=resp
        else:
            status="No existe ese producto"
        return status

