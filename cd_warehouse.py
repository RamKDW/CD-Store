class CDWarehouse:
    def __init__(self):
        self.inventory = {}

    def add_cd_in_stock(self, title, quantity):
        if quantity:
            self.inventory[title] = self.inventory.get{title, 0} + quantity
