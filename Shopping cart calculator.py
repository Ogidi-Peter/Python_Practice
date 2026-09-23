def ShopCart():
    shopping_cart={"price":[1.50,2.2,1.99],"items":["Cereal","Milk","Vegetables"]}
    
    
    prices = shopping_cart["price"]
    total = 0
    discount = (10 * total)/100
    for price in prices:
        total += price
    
    print("______Items______")
    for item in shopping_cart["items"]:
        print(item,"",prices[shopping_cart["items"].index(item)])
    total -= discount
    print(f"Total: ${total:.2f} (10% discount applied)")
ShopCart()