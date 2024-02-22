# Sean Price rwa1 assignment
import time
#user is input from user
user = ''
#form dictionary ( office items) key=item value= price
office={'desktop computer' : 600, 'monitor': 200, 'mouse': 15, \
    'keyboard': 30, 'office chair':70, 'desk' :150, 'pens': 8,\
        'copy paper' : 50, 'printer':200, 'file cabinet' :200}   
#while loop to continously update dictonary
while user != 'q' :
    # shows list of current items and prices
    print('\n {Item : dollar value}')
    print('\n',office)
    
    #instructs user on how to modify dictionary
    print('\n instruction keys: \n a=add a product \n r=remove a product \n e=edit a price \n q=quit')
    #interpret user input
    user = input()

    if user == 'a':
        #ask for product and price from user
        print('\n input prduct name to add only')
        product = input()
        print('\n input price to add')
        price = input()
        #test to make sure price is a number
        if price.isnumeric() is False:
            #returns to begining if input is not a number
            print('\n error: please only input numbers \n')
            time.sleep(2)
        else:
            #turn price into integer and update dictionary
            print('\n adding %s with price %s' %(product, price))
            office.update({product :int(price)})
        
    elif user == 'r':
        #ask for product name by user
        print('\n input product name to be removed')
        product = input()
        #test if product is in dictionary
        try: 
            #remove product from dictionary
            print('\n removing %s ' %product)
            office.pop(product) 
        except KeyError: 
            #returns to begining if product doesnt exist in dict
            print('\n product not found')
            time.sleep(2)
            
    elif user == 'e':
        #ask for product name
        print('\n input product to price change')
        product = input()
        #test if product is in dictionary, returns None if product not found
        price = office.get(product)
        if price is not None:
            #ask for the new price
            print('\n input new price')
            price = input()
            # make sure price is a number
            if price.isnumeric() is False:
                # returns to beginning if price is not a number
                print('\n error: please only input numbers \n')
                time.sleep(2)
            else:
                #turn price into integer and update dictionary
                print('\n changing price of %s to %s' %(product, price))
                office.update({product :int(price)})
        else:
            #returns to beginning if product is not in dictionary
            print('\n product not found')
            time.sleep(2)
    elif user == 'q':
        #ends loop
        print('\n quitting.......')
    else :
        #restart loop if unrecognized input
        print('\n error: please use defined instruction keys \n')
        time.sleep(2)
        
   