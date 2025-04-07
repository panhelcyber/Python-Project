menu={
    "pizza":100,
    "cofee":80,
    "cake":220,
    "tea":20,
}

print("Welcome to panhel restraunt.\n")
for item,price in menu.items():
    print(f"{item}:{price}RS")

order_total =0;

while True:
    item=str(input("select your item: "))
    if item in menu:
        order_total+=menu[item]
        print(f"your item {item} is select")
    else:
        print(f"Your selected item {item} is not in our list")

    another_order=input("Would you like to add another item: (yes/no)")
    if another_order.lower()!='yes':
        break

print(f"You have to pay total amount {order_total}RS ")


