message = """
    Welcome to Zomato
      SUBWAY OFFERS

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
amount = int(input("Enter Total Amount: "))
#promo_code = input("Enter Promo Code: ")


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

for check_coupon in all_coupons:
    if amount >= check_coupon["minimum_order_size"]:
        #print("Valid Coupon:", check_coupon["coupon"])
        #Calculate Max Off
        discount = amount * check_coupon["percent_off"]
        if discount >= check_coupon["cap"]:
            discount = check_coupon["cap"] + check_coupon["cashback"]

        print("Max Discount with coupon", check_coupon["coupon"], "is \u20b9", discount, "with cashback \u20b9", check_coupon["cashback"])
    elif amount < 159:
        print("minimum cart value for discount is: \u20b9", 159)
        break

promo_code = input("Enter Promo Code: ").upper()

discount = 0

for check_coupon in all_coupons:
    if amount >= 159 and promo_code == check_coupon["coupon"]:
        discount = amount * check_coupon["percent_off"]
        if discount >= check_coupon["cap"]:
            discount = check_coupon["cap"]
        amount_to_pay = amount - discount
        print("Amount to pay: \u20b9", amount_to_pay)

if discount == 0:
    print(promo_code, "NOT Valid")






