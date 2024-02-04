# total_stock_worth variable is created with an initial value of zero.
# A list is created containing items of the menu. 
# Two dictionaries are created containing the stock and price of each of the items of the menu.
total_stock_worth = 0
menu_items = ['cinnamon bun', 'grilled chicken sandwhich', 'protein salad', 'espresso shot']
stock = {'cinnamon bun' : 50,
         'grilled chicken sandwhich' : 25,
         'protein salad' : 20,
         'espresso shot' : 300}
price = {'cinnamon bun' : 2,
         'grilled chicken sandwhich' : 10.5,
         'protein salad' : 7,
         'espresso shot' : 1.5}

# A for loop is created to calculate the stock worth of every item in the menu.
# All stock worth of every item is added up, being the last figure the total stock worth.
for items in menu_items:
    item_value = (stock[items] * price[items])
    total_stock_worth += item_value
    print(total_stock_worth)

