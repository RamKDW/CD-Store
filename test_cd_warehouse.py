from cd_warehouse import CDWarehouse
from unittest.mock import Mock


def test_add_cd():
    store = CDWarehouse()
    store.add_cd("Baby Shark", "Pinkfong", 10)
    assert store.get_stock("Baby Shark", "Pinkfong") == 10


def test_search_by_title():
    store = CDWarehouse()
    store.add_cd("Dangerous", "Michael Jackson", 5)
    results = store.search(title="Dangerous")
    assert len(results) == 1


def test_purchase_cd():
    store = CDWarehouse()
    store.add_cd("ABC Songs", "Weekend", 3)
    print(store.cds)
    store.purchase("ABC Songs", "Weekend", 2763876487, 1)
    assert store.get_stock("ABC Songs", "Weekend") == 2


def test_add_multiple_cds():
    store = CDWarehouse()
    store.add_cd("Baby Shark", "Pinkfog", 5)
    store.add_cd("Baby Shark", "Pinkfog", 8)
    assert store.get_stock("Baby Shark", "Pinkfog") == 13


def test_notify_charts_on_purchase():
    store = CDWarehouse()
    store.add_cd("ABCD Songs", "Weekend", 10)

    mocking_chart = Mock()
    mocking_chart.notify_sale = Mock()
    store.chart = mocking_chart

    store.purchase("ABCD Songs", "Weekend", 67987588786, 3)
    mocking_chart.notify_sale.assert_called_once_with(
        "ABCD Songs", "Weekend", 3)
