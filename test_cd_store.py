def test_successful_purchase():
    warehouse = CDWarehouse()
    warehouse.add_cd_in_stock("The Wall", 5)
    warehouse.set_search_enabled(True)
    warehouse.purchase("The Wall", "567983465892798", 2)
    assert warehouse.get_stock("The Wall") == 3
