menu = ['apple', 'cake', 'brownie', 'coffee', 'tea']

stock = {'apple' : 5, 
         'cake' : 5, 
         'brownie' : 8, 
         'coffee' : 2, 
         'tea' : 10}
#Dictionary using values from menu key:values pairs indicate the stock amount of the items from menu
price = {'apple' : 2, 
         'cake' : 5, 
         'brownie' : 4.5,
         'coffee' : 2, 
         'tea' : 1.5}
# Price of each item from the menu 

total_stock = 0 #Starts the total_stock value at 0
for item in menu: #Allows items to be removed from menu - Prevenets that menu item from appearing in calculation  
    menu_item = stock[item] * price[item] #value of each menu_item currently in stock. matches key:value items between stock and price 
    total_stock += menu_item #for each item in the menu list, adds the value from stock * price to total_stock

print (f"The total value of remaining stock is £{total_stock}") #prints the value of the total_stock variable in an easy to understand output. 