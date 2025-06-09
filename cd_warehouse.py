class CDWarehouse:
    def __init__(self):
        self.inventory = {}

    def add_cd(self, title, quantity):
        if quantity:
            self.inventory[title] = self.inventory + quantity
        else:
            self.inventory[title] = quantity
