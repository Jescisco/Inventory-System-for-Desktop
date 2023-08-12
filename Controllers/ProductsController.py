from Models.ProductsModel import ProductsModel

class ProductsController(ProductsModel):

    def create_product(self, name:str, code:str, purchase_price:int, sale_price:int, existence:str):
        return super().create_product(name,code,purchase_price,sale_price,existence)

    def read_product(self, code:str=""):
        return super().read_product(code)

    def update_product(self, id:int, name:str, code:str, purchase_price:int, sale_price:int, existence:str):
        return super().update_product(id,name,code,purchase_price,sale_price,existence)

    def delete_product(self, id:int):
        return super().delete_product(id)

    def add_product_existence(self, id:int, existence:int):
        return super().add_product_existence(id, existence)

    def search_products(self, search:str):
        return super().search_products(search)