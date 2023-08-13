from Models.GeneralModel import GeneralModel
from Resources.Includes.Querys import STORE_QUERYS as Q

class StoreModel(GeneralModel):

    def read_sales(self):
        return self.run_get_query(Q.get("read_sales"))

    def read_sales_of_the_day(self, date):
        return self.run_get_query(Q.get("read_sales_of_the_day"),(date,))