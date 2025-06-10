class CDWarehouse:
    def __init__(self):
        self.cds = {}

    def add_cd(self, title, artist, amount):
        key = f"{title.lower()}|{artist.lower()}"
        self.cds[key] = self.cds.get(key, 0) + amount

    def get_stock(self, title, artist):
        key = f"{title.lower()}|{artist.lower()}"
        return self.cds.get(key, 0)
