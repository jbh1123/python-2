class TaxMan:
    def __init__(self, list_of_items, percent_tax) -> None:
        self.items = list_of_items
        self.percent = float(percent_tax.rstrip('%'))/100

    
    def calc_total(self):
        list_of_prices = [item['price'] for item in self.items]
        total = sum(list_of_prices)
        total += total*self.percent
        self.__total = total

    def get_total(self):
        return self.__total
