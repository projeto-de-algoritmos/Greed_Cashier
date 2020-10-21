import json, random
import pprint


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

def get_total_price(my_products):
    total_price = 0.0
    for key, value in my_products.items():
        split = value[0][1].split('.')
        integer = int(split[0])
        decimal = int(split[1])
        total_price += (integer * 100 + decimal) * value[-1]
    return total_price

def cashier_algorithm(coins, total):
    d = {}
    for i in coins:
        d[i] = 0
    for i in range(0, len(coins)):
        while total >= coins[i]:
            d[coins[i]] += 1
            total -= coins[i]
    return d

def minimizing_coins_using_dp(coins, change):
    inf = int(1e9)
    dp = [0] * (change + 1)
    dp[0] = 0
    for i in range(1, change + 1):
        dp[i] = inf
        for j in range(len(coins)):
            if i >= int(coins[j]) and dp[i - int(coins[j])] + 1 < dp[i]:
                dp[i] = dp[i - int(coins[j])] + 1
    return inf if dp[change] == inf else dp[change]

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
            pp = pprint.PrettyPrinter(indent=8)
            pp.pprint(products)
        elif option == '2':
            pp = pprint.PrettyPrinter(indent=8)
            pp.pprint(my_products)
        elif option == '3':
            pp = pprint.PrettyPrinter(indent=8)
            pp.pprint(products)
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
            except KeyError:
                print('Enter the valid option, please')
        elif option == '5':
            total_price = get_total_price(my_products)
            print('The total price of your purchase is: $ %d' % (total_price // 100) + '.' + '%d' % (total_price % 100))
        elif option == '6':
            inp = float(input('Enter the amount you\'ll give to make the payment: ')) * 100.0
            total_price = get_total_price(my_products)
            if inp < total_price:
                print('Sorry, you don\'t have enough money to pay')
            else:
                change = inp - total_price
                quantity_of_coins = cashier_algorithm(coins, change)
                new_coins = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
                new_quantity_of_coins = dict(zip(new_coins, list(quantity_of_coins.values())))
                print('The change of money is: $ %d' % (change // 100) + '.' + '%d' % (change % 100))
                mn_coins = 0
                for key, value in new_quantity_of_coins.items():
                    if value >= 1:
                        mn_coins += value
                        print('%d' % value + ' coin(s) of $ ' + str(key))
                print('and the minimum number of coins is: %d' % mn_coins)

                print('However, the cashier\'s algorithm does not work for all cases and, therefore, dynamic programming is used to minimize the number of coins, which is the optimal solution to the problem.')
                mcud = minimizing_coins_using_dp(coins, int(change))
                print('The minimum number of coins using dp is: %d' % mcud)
                if mcud < mn_coins:
                    print('In this case, the dp works and the cashier\'s greed algorithm doesn\'t work')
                else:
                    print('The cashier\'s greed algorithm and the algorithm using dp for minimize the number of coins does work for this case')
                print('-----------------------------------------------------------------------------------------------------------------------')
        else:
            print('Thanks!')
            loop_condition = False
                
if __name__ == '__main__':
    main()