import json, random, math


class Product:
    def __init__(self, code, name, price, description, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

def get_data_of_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
    products = {}
    i = 1
    for key in data:
        products[i] = [key['title'], str(key['price']), key['description']]
        i += 1
    return products

def cashier_algorithm(coins, total):
    d = {}
    for i in coins:
        d[i] = 0
    for i in range(0, len(coins)):
        while total >= coins[i]:
            d[coins[i]] += 1
            total -= coins[i]
    return d

def menu():
    print('1 - List all products of the supermarket')
    print('2 - List all products in your cart')
    print('3 - Add a product in your cart')
    print('4 - Remove product from your cart')
    print('5 - Total price of your purchase')
    print('6 - Pay')
    print('0 - Exit')

def main():
    products = get_data_of_json('../data/products.json')
    coins = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    coins = [i * 100 for i in coins]

    my_products = {}
    
    loop_condition = True
    while loop_condition:
        menu()
        option = input('Enter the option: ')
        if option == '1':
            print(products)
        elif option == '2':
            print(my_products)
        elif option == '3':
            print(products)
            try:
                inp = int(input('Enter the code of the item that you want add in your cart: '))
                quantity = int(input('Now, enter the quantity: '))
                my_products[inp] = [products[inp], quantity]
            except KeyError:
                print('Enter the valid option, please')
        elif option == '4':
            try:
                inp = int(input('Enter the code of the item that you want remove from your cart: '))
                del my_products[inp]            
            Except KeyError:
                print('Enter the valid option, please')
        elif option == '5':
            total_price = 0.0
            for key, value in my_products.items():
                split = value[0][1].split('.')
                integer = int(split[0])
                decimal = int(split[1])
                total_price += (integer * 100 + decimal) * value[-1]
            print('The total price of your purchase is: $ %d' % (total_price // 100) + '.' + '%d' % (total_price % 100))

if __name__ == '__main__':
    main()