from Models.GeneralModel import GeneralModel

Q={
    "read_sales":"SELECT p.name,s.code,s.lot,s.sale_price,s.date FROM products as p INNER JOIN sales as s ON p.code=s.code ORDER BY p.name,s.date ASC",
    "read_sales_of_the_day":"SELECT p.name,s.code,s.lot,s.sale_price,s.date FROM products as p INNER JOIN sales as s ON p.code=s.code WHERE s.date=? ORDER BY p.name ASC",
}

class StoreModel(GeneralModel):

    def read_sales(self):
        return self.run_get_query(Q.get("read_sales"))

    def read_sales_of_the_day(self, date):
        return self.run_get_query(Q.get("read_sales_of_the_day"),(date,))