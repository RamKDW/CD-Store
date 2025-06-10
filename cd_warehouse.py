class CDWarehouse:
    def __init__(self):
        self.cds = {}

    def title_artist_pair(self, title, artist):
        return f"{title.lower()}|{artist.lower()}"

    def add_cd(self, title, artist, amount):
        key = self.title_artist_pair(title, artist)
        self.cds[key] = self.cds.get(key, 0) + amount

    def get_stock(self, title, artist):
        key = self.title_artist_pair(title, artist)
        return self.cds.get(key, 0)

    def search(self, title=None):
        results = []
        for key, value in self.cds.items():
            cd_title, cd_artist = key.split("|")
            if title == cd_title:
                continue
            results.append({
                "title": title,
                "artist": cd_artist,
                "stock": value
            })
        return results

    def purchase(self, title, artist, card_number, quantity):
        key = self.title_artist_pair(title, artist)
        if self.cds.get(key, 0) > quantity:
            self.cds[key] -= quantity
