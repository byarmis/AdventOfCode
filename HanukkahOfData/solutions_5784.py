import csv

def getter(filename, pk):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return {line[pk]:line for line in reader}

def night_1():
    customers = getter('5784/noahs-customers.csv', 'customerid')
    letters_to_num = {
            'a':2, 'b':2, 'c':2,
            'd':3, 'e':3, 'f':3,
            'g':4, 'h':4, 'i':4,
            'j':5, 'k':5, 'l':5,
            'm':6, 'n':6, 'o':6,
            'p':7, 'q':7, 'r':7, 's':7,
            't':8, 'u':8, 'v':8,
            'w':9, 'x':9, 'y':9, 'z':9,
            }

    def name_as_number(name):
        return ''.join(str(letters_to_num.get(l.lower(), '')) for l in name.split()[1] if l)

    filtered_customers = [customer['name'] for customer in customers.values() if name_as_number(customer['name']) == ''.join(l for l in customer['phone'] if l.isdigit())]

    assert len(filtered_customers) == 1

    return filtered_customers.pop()

print('Night 1: ', night_1())


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

