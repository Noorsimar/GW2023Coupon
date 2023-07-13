from Session7 import Menu, Dish

"""
    Zomato Cart
"""



def valid_coupons(amount):
    welcome50 = {"coupon": "WELCOME50",
                 "percent_off": .50,
                 "cap": 100,
                 "minimum_order_size": 159,
                 "cashback": 0}

    zompaytm = {"coupon": "ZOMPAYTM",
                "percent_off": .20,
                "cap": 50,
                "minimum_order_size": 299,
                "cashback": 25}

    rainy = {"coupon": "RAINY",
             "percent_off": .30,
             "cap": 200,
             "minimum_order_size": 499,
             "cashback": 0}

    all_coupons = [welcome50, zompaytm, rainy]
    print(f"Based on Amount: {amount}")
    for check_coupon in all_coupons:
        if amount >= check_coupon["minimum_order_size"]:
            # Calculate Max Off
            discount = amount * check_coupon["percent_off"]
            if discount >= check_coupon["cap"]:
                discount = check_coupon["cap"] + check_coupon["cashback"]
            print("``````````Valid Coupons/Max Discounts````````````")
            print("Max Discount with coupon", check_coupon["coupon"], "is \u20b9", discount, "with cashback \u20b9",
                  check_coupon["cashback"])

        elif amount < 159:
            print(f"No Coupons Available.\nMinimum cart value for Discount Coupon is: \u20b9", 159)
            break

    promo_code = input("\nEnter Promo Code: ").upper()

    discount = 0

    for check_coupon in all_coupons:
        if amount >= 159 and promo_code == check_coupon["coupon"]:
            discount = amount * check_coupon["percent_off"]
            if discount >= check_coupon["cap"]:
                discount = check_coupon["cap"]
            amount_to_pay = amount - discount
            print("Amount to pay: \u20b9", amount_to_pay)

    if discount == 0:
        print(promo_code, "Coupon NOT Valid")


class Cart:
    def __init__(self, item_ids=[], quantities=[], price=[], dishes=[]):
        self.item_ids = item_ids
        self.quantities = quantities
        self.dishes = dishes
        self.price = price


    def show(self):
        print("Food ID:", self.item_ids)
        print("Cart Dishes:", end=" ")
        for item in self.item_ids:
            print(self.dishes[item].name, end=", ")
        print("\nCart Quantities:", self.quantities)

    def calculate_cart(self):
        return sum(self.price)

def main():
    dish1 = Dish(name="Dal Makhani", price=350, rating=4.5)
    dish2 = Dish(name="Paneer Do Pyaza", price=450, rating=5.0)
    dish3 = Dish(name="Noodles", price=250, rating=3.8)
    dish4 = Dish(name="Burger", price=100, rating=4.1)
    dish5 = Dish(name="Fries", price=90, rating=4.8)
    dish6 = Dish(name="Parantha", price=40, rating=4.2)
    dish7 = Dish(name="Cola", price=50, rating=4.7)

    # List of Objects :)
    dishes = [dish1, dish2, dish3, dish4, dish5, dish6, dish7]

    menu = Menu(title="Mix Delight", num_of_dishes=len(dishes), dishes=dishes)

    print("MENU:")
    menu.show()

    item_names = []
    quantities = []
    item_ids = []
    price = []

    while True:
        item_id = int(input("Enter Dish ID to add in Cart: "))
        quantity = int(input("Enter Dish Quantity: "))

        item_names.append(dishes[item_id].name)
        quantities.append(quantity)
        price.append(dishes[item_id].price * quantity)
        item_ids.append(item_id)

        print(price)

        choice = input("Do You wish to add more items? (yes/no)")
        if choice == "no":
            break

    cart1 = Cart(item_ids, quantities, price, dishes)
    amount = cart1.calculate_cart()


    #amount = sum(price)
    print("\n$ $ $ $ $ $ $ $\nYOUR CART")
    cart1.show()
    print("TOTAL AMOUNT: \u20b9", amount)
    print("$ $ $ $ $ $ $ $\n")


    message = """
        Welcome to Zomato Coupons
        Today's Offers:

        WELCOME50
        Get 50% OFF up to ₹100
        Valid on total value of items worth ₹159 or more.


        ZOMPAYTM
        Get 20% OFF up to ₹50 and ₹25 Paytm cashback using Paytm
        Valid on total value of items worth ₹299 or more.

        RAINY
        Get 30% OFF up to ₹200.
        Valid on total value of items worth ₹499 or more.


    """

    print(message)
    valid_coupons(amount)




if __name__ == "__main__":
    main()


# Assignment: Implement the same program Using OOPS from Session7 and Session7A

