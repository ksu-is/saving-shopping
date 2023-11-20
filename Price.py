def get_price(product, quantity):
    subtotal = price_dict[product] * quantity
    print(product + ':$ ' + str(price_dict[product]) + ' x ' + str(quantity) + ' = ' +str(subtotal))
    return subtotal

def get_discount(bill_price, membership):
    discount = 0
    if bill_price >= 25:
        if membership == 'gold':
            bill_price = bill_price * 0.75
            discount = 25
        elif membership == 'silver':
            bill_price = bill_price * 0.85
            discount = 15
        elif membership == 'bronze':
            bill_price = bill_price * 0.95
            discount = 5
        print(str(discount) + '% off for ' + membership + ' membership at total price no less than $25')
    return bill_price
        

buying_dict = {'chips': 2, 'chicken': 5, 'egg': 20}

price_dict = {'chips': 4, 'fish': 3, 'chicken': 5, 'cabbage': 2, 'egg': 0.2}

bill_price = 0

for key, value in buying_dict.items():
    bill_price += get_price(key, value)


membership = 'gold'


bill_price = get_discount(bill_price, membership)
print('The total price is $' + str(bill_price))

