def shopping(price):  
    '''to define the function called shopping'''
    return price * 2  # to calculate the price for shopping

def rent(price):  
    '''to define the function called rent'''
    return price + price * 25/100  # to calculate the price for rent

def uber(price):  
    '''to define the function called price'''
    return price - price * 50/100  # to calculate the price for uber

def total(shop_price, rent_price, uber_price):  
    '''to define the function called total'''
    print(shopping(shop_price) + rent(rent_price) + uber(uber_price))  # to print the total of those prices 

total(50, 50, 50)  # to call the function