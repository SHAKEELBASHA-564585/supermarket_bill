from datetime import datetime

items = {
    "sugar": 10,
    "salt": 2,
    "wheat": 30
}

total_amount = 0
bill = ""
user = input("enter your name = ")

def generate_bill():
    print("\n\n")
    print("----------------------============================= shakeel super market =============================----------------------")
    print("\n")
    print(f"\tHello {user}","\t"*7,"date : ",datetime.now())
    if(len(bill) != 0):
        print("\n")
        print("\t\t\t" + "item" + "\t\t\t" + "quantity(kg)" + " \t\t\t" + "price" + "\n")
        print(bill)
        print("\t"*10,"total_amount = ",total_amount)
        print("\n\n")
    else:
        print("\t\t\t\t\t\tno items are selected")

while True:
    print()
    for key in items:
        print(key)
    print("calculate")
    print("exit")
    item = input("select any item : ")
    if item == "calculate":
        generate_bill()
    elif item == "exit":
        generate_bill()
        exit()
    else:
        quantity = int(input("how much quantity you want ? "))
        if items.get(item,-1) != -1:
            total_amount += items.get(item) * quantity
            bill += "\t\t\t" + item + "\t\t\t" + str(quantity) + "kg" + " \t\t\t\t" + str(items.get(item) * quantity) + "\n"
        else:
            print("invalid option")