//maintain Glocery list

glocery = {}
gloceryHistory = []

stop = False

while not stop:
    item_name = input("Etner the item name ")
    price = float(input("Price "))
    quantity = int(input("Quantity "))
    brand = input("Brand ")
    
    glocery = {'item': item_name ,'Q': quantity , 'Price':price,'Brand':brand }
    gloceryHistory.append(glocery)
    
    print("want enter another item : ")
    choice = input(" 'y' for yes and 'n' for no ")
    if choice =='n' :
        stop = True

total_item=0
total_cost = 0.0

print()
print("Puchase History")
for i in gloceryHistory:
       print("Brand: {}      Item Name: {}     Price: {}     Quantity : {}".format(i['Brand'],i['item'],i['Price'],i['Q'] ))
       total_item += i['Q']
       total_cost += i['Price']*i['Q']
        
print()

print("Total item = {}".format(total_item))
print("Total Cost = {}".format(total_cost))

brand = []
for i in gloceryHistory:
    brand.append(i['Brand'])

print()
for i in set(brand):
     print("Item Related to Brand '{}' :".format(i))
     for j in gloceryHistory:
        if i == j['Brand']:
            print("Name: {}       Price: {}      Quantity : {}".format(j['item'],j['Price'],j['Q'] ))

    
