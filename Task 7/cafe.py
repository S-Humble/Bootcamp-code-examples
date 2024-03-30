menu = ['apple', 'cake', 'brownie', 'coffee', 'tea']

stock = {'apple' : 5, 
         'cake' : 5, 
         'brownie' : 8, 
         'coffee' : 2, 
         'tea' : 10}

price = {'apple' : 2, 
         'cake' : 5, 
         'brownie' : 4.5,
         'coffee' : 2, 
         'tea' : 1.5}

total_stock = {item: stock[item] * price[item] for item in stock if item in menu}
#creates new dictionary containing keys based on menu and multiplication of the values from price and stock
#uses items() method
#if item removed from menu, stock controll doesn't represent it even if it is in either dictionary
apple_value = (stock['apple'] * price['apple'])
# I need to multiply the value from stock with the value from price
#total_stock = (stock.values() * price.values())



print (f"The value of {menu} is {total_stock}")