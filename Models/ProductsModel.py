from Models.GeneralModel import GeneralModel

Q={
    "create_product":"INSERT INTO products(name,code,purchase_price,sale_price,existence) VALUES(?,?,?,?,?)",
    "read_product":"SELECT * FROM products WHERE code=?",
    "read_products":"SELECT * FROM products ORDER BY existence ASC",
    "read_update_product":"SELECT * FROM products WHERE id!=? AND code=?",
    "update_product":"UPDATE products SET name=?,code=?,purchase_price=?,sale_price=?,existence=? WHERE id=?",
    "delete_product":"DELETE FROM products WHERE id=?",
    "add_product_existence":"UPDATE products SET existence=? WHERE id=?",
    "substract_product_existence":"UPDATE products SET existence=existence-1 WHERE id=?",
    "search_products":"SELECT * FROM products WHERE name LIKE CONCAT('%',?,'%')"
}

class ProductsModel(GeneralModel):

    def create_product(self, name:str, code:str, purchase_price:int, sale_price:int, existence:str):
        if self.read_product(code)==[]:
            resp=self.run_set_query(Q.get('create_product'),(name.upper(),code,purchase_price,sale_price,existence))
            if type(resp)==int:
                status="Success" if (resp>0) else "No se registró"
            else:
                status=resp
        else:
            status="Ya existe ese código"
        return status

    def read_product(self, code:str=""):
        if code!="":
            return self.run_get_query(Q.get('read_product'),(code,))
        else:
            return self.run_get_query(Q.get('read_products'))

    def update_product(self, id:int, name:str, code:str, purchase_price:int, sale_price:int, existence:str):
        if self.run_get_query(Q.get('read_update_product'),(id,code))==[]:
            resp=self.run_set_query(Q.get('update_product'),(name.upper(),code,purchase_price,sale_price,existence,id))
            if type(resp)==int:
                status="Success" if (resp>0) else "No se actualizó"
            else:
                status=resp
        else:
            status="Ya existe ese código en otro producto"
        return status

    def delete_product(self, id:int):
        resp=self.run_set_query(Q.get("delete_product"),(id,))
        if type(resp)==int:
            status="Success" if (resp>0) else "No se eliminó"
        else:
            status=resp
        return status

    def add_product_existence(self, id:int, existence:int):
        resp=self.run_set_query(Q.get('add_product_existence'),(existence,id))
        if type(resp)==int:
            status="Success" if (resp>0) else "No se insertó"
        else:
            status=resp
        return status

    def substract_product_existence(self, id:int):
        resp=self.run_set_query(Q.get('substract_product_existence'),(id,))
        if type(resp)==int:
            status="Success" if (resp>0) else "No se insertó"
        else:
            status=resp
        return status

    def search_products(self, search:str):
        return self.run_get_query(Q.get("search_products"),(search,))