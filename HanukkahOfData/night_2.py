import csv

def getter(filename, pk):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return {line[pk]:line for line in reader}

def night_2():
    customers = getter('5784/noahs-customers.csv', 'customerid')
    orders = getter('5784/noahs-orders.csv', 'orderid')
    order_items = getter('5784/noahs-orders_items.csv', 'orderid')
    products = getter('5784/noahs-products.csv', 'sku')

    filtered_customers = {k:v for k,v in customers.items() if v['name'].split()[0].startswith('J') and v['name'].split()[1].startswith('P')}
    filtered_orders = {k:v for k,v in orders.items() if v['ordered'].split()[0].split('-')[0] == '2017'}
    filtered_orders = {k:v for k,v in filtered_orders.items() if v['customerid'] in filtered_customers}
    
    filtered_orders = {k:v for k,v in filtered_orders.items() if 'bagel' in products[order_items[k]['sku']]['desc'].lower()}

    assert len(filtered_orders) == 1

    order_id = filtered_orders.popitem()[0]
    return customers[orders[order_id]['customerid']]['phone']



print('Night 2: ', night_2())

