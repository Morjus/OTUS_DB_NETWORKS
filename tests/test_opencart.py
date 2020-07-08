import datetime


def test_create_product(connect):
    """Создание продукта, добавить проверку, что сущность удалена, добавлена и изменена в БД"""
    product = {
        'model': 'Nokia',
        'sku': '',
        'upc': '',
        'ean': '',
        'jan': '',
        'isbn': '',
        'mpn': '',
        'location': '',
        'quantity': 939,
        'stock_status_id': 7,
        'image': '',
        'manufacturer_id': 5,
        'shipping': 1,
        'price': '100.0000',
        'points': 200,
        'tax_class_id': 9,
        'date_available': datetime.date(2009, 2, 3).strftime('%Y-%m-%d %H:%M:%S'),
        'weight': '146.40000000',
        'weight_class_id': 2,
        'length': '0E-8',
        'width': '0E-8',
        'height': '0E-8',
        'length_class_id': 1,
        'subtract': 1,
        'minimum': 1,
        'sort_order': 0,
        'status': 1,
        'viewed': 10,
        'date_added': datetime.datetime(2009, 2, 3, 16, 6, 50).strftime('%Y-%m-%d %H:%M:%S'),
        'date_modified': datetime.datetime(2011, 9, 30, 1, 5, 39).strftime('%Y-%m-%d %H:%M:%S')
    }
    connect.insert_entity("oc_product", product)
    response = connect.select_entity("oc_product", "model='Nokia'")
    assert response[0][1] == "Nokia", "Product is not created!"


def test_update_product(connect):
    """Изменение продукта, добавить проверку, что сущность удалена, добавлена и изменена в БД"""
    product = {
        'model': 'Motorolla',
        'sku': '',
        'upc': '',
        'ean': '',
        'jan': '',
        'isbn': '',
        'mpn': '',
        'location': '',
        'quantity': 939,
        'stock_status_id': 7,
        'image': '',
        'manufacturer_id': 5,
        'shipping': 1,
        'price': '100.0000',
        'points': 200,
        'tax_class_id': 9,
        'date_available': datetime.date(2009, 2, 3).strftime('%Y-%m-%d %H:%M:%S'),
        'weight': '146.40000000',
        'weight_class_id': 2,
        'length': '0E-8',
        'width': '0E-8',
        'height': '0E-8',
        'length_class_id': 1,
        'subtract': 1,
        'minimum': 1,
        'sort_order': 0,
        'status': 1,
        'viewed': 10,
        'date_added': datetime.datetime(2009, 2, 3, 16, 6, 50).strftime('%Y-%m-%d %H:%M:%S'),
        'date_modified': datetime.datetime(2011, 9, 30, 1, 5, 39).strftime('%Y-%m-%d %H:%M:%S')
    }
    connect.update_entity("oc_product", "model='Nokia'", product)
    response = connect.select_entity("oc_product", "model='Motorolla'")
    assert response[0][1] == "Motorolla", "Product is not upadated!"


def test_delete_product(connect, data):
    """Удаление продукта, добавить проверку, что сущность удалена, добавлена и изменена в БД"""
    connect.delete_rows("oc_product", "product_id=104")
    response = connect.select_entity("oc_product", "product_id=104")
    assert response == [], "Product is not deleted!"
