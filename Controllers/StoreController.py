from Models.StoreModel import StoreModel

class StoreController(StoreModel):

    def read_sales(self):
        return super().read_sales()

    def read_sales_of_the_day(self, date):
        return super().read_sales_of_the_day(date)