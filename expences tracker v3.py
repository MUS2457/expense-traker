from datetime import datetime
import json

def average(numbers):
    if not numbers:
        return 0
    return round(sum(numbers) / len(numbers), 1)


expences = {}
total_category = {}

while True :
    product = input(" your product name ,'done' to calculate or 'exit' to exit the program : ")
    if product.lower().strip() == 'exit' :
        print("the program is now closed !")
        break
    if product.lower().strip() == 'done' :
        break
    if product == "" :
        print("please enter a valid name !")

    category = input(" the category of your product").strip()

    while True :
        try :
            price = int(input(" the price of the product : "))
            break
        except ValueError :
            print("please enter only number !")

    expences[product] = {"category" : category, "price" : price}     

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")   

if expences :
    sum_price = sum(amount["price"] for amount in expences.values())
    max_product = max(expences, key = lambda p : expences[p]["price"]) 
    min_product = min(expences, key = lambda p : expences[p]["price"])   

for product_name, info in expences.items():

    category = info["category"]
    price = info["price"]

    if category in total_category :
        total_category[category] += price
    else :
        total_category[category]  = price


data = {"sum of price" : sum_price , "most expensive product" : max_product,
        "the price of most expensive product" : expences[max_product]["price"],
        "most cheap product" : min_product, "the price of most cheap product" : expences[min_product]["price"],
        "average" : average([amount["price"] for amount in expences.values()]), "calculate the sum price by category" : total_category,
         "number of categories": len(total_category),"sum by category": total_category
}

with open("expence tracker v3.txt", "w") as f :
    for pro,info in expences.items() :
        f.write(f" the product : {pro}, category : {info['category']}, price : {info['price']}")
    
    f.write(" 💰 SHOPPING SUMMARY:\n")                 
    f.write("\n-------------------------\n")
    f.write(f" the date and time : {timestamp}\n")
    f.write(f" Most expensive product : {max_product} with a price of : {expences[max_product]["price"]} ¥ \n")
    f.write(f" Most cheap product : {min_product} with a price of : {expences[min_product]["price"]} ¥ \n")
    f.write(f" Average price : {average([amount["price"] for amount in expences.values()])} ¥ \n")
    f.write(f" number of products  : {len(expences)} \n")
    f.write(f"Number of categories: {len(total_category)}\n")
    for cat,pri in sorted(total_category.items()) :
        f.write(f" {cat} : {pri} ¥ ")
    f.write("\n---------------------------\n\n")

with open("expence tracker v3.json","w") as j :
    json.dump(data, j, indent = 4)

print(json.dumps(data,indent = 4))


