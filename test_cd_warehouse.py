from cd_warehouse import CDWarehouse


def test_add_cd():
    store = CDWarehouse()
    store.add_cd("Baby Shark", "Pinkfong", 10)
    assert store.get_stock("Baby Shark", "Pinkfong") == 10
