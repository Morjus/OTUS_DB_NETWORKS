import csv
import datetime

from pytest import fixture

from DataBase.mariadb.client import MariadbClient


@fixture(scope='session', name='connect')
def create_connect():
    conn = MariadbClient()
    return conn


@fixture(scope='function', name='data')
def create_data(connect):
    new = []
    with open('data.csv', 'r') as file:
        raws = csv.reader(file, delimiter=';')
        for item in raws:
            for n, i in enumerate(item):
                if i == "''":
                    item[n] = ""
            times = []

            for d in item[17].split("--"):
                times.append(int(d))
            res = datetime.date(times[0], times[1], times[2]).strftime('%Y-%m-%d %H:%M:%S')
            item[17] = res

            for d in item[29].split("--"):
                times.append(int(d))
            res = datetime.date(times[0], times[1], times[2]).strftime('%Y-%m-%d %H:%M:%S')
            item[29]=res

            for d in item[30].split("--"):
                times.append(int(d))
            res = datetime.date(times[0], times[1], times[2]).strftime('%Y-%m-%d %H:%M:%S')
            item[30]=res

            new.append(tuple(item))
    columns = ','.join(['model', 'sku', 'upc', 'ean', 'jan', 'isbn', 'mpn', 'location', 'quantity', 'stock_status_id',
                        'image', 'manufacturer_id', 'shipping', 'price', 'points', 'tax_class_id', 'date_available',
                        'weight', 'weight_class_id', 'length', 'width', 'height', 'length_class_id', 'subtract',
                        'minimum', 'sort_order', 'status', 'viewed', 'date_added', 'date_modified'])
    ins = connect.insert_many_rows('oc_product', columns, new)
    yield ins
    ids = [i[0] for i in new]
    for row in ids:
        connect.delete_rows("oc_product", f'product_id={row}')
