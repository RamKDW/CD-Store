from cd_warehouse import CDWarehouse


def test_add_cd():
    store = CDWarehouse()
    store.add_cd("Baby Shark", "Pinkfong", 10)
    assert store.get_stock("Baby Shark", "Pinkfong") == 10


def test_search_by_title():
    store = CDWarehouse()
    store.add_cd("Dangerous", "Michael Jackson", 5)
    results = store.search(title="Dangerous")
    assert len(results) == 1
