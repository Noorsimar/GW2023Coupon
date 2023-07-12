# STANDARDIZATION IN OOPS: PayTm:)

# Object and Attributes: Recharge: recharge_type, tel, operator, amount
class Recharge:
    # CONSTRUCTOR
    def __init__(self, recharge_type="", tel="", operator="NULL", amount=10):
        self.recharge_type = recharge_type
        self.tel = tel
        self.operator = operator
        self.amount = amount

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print(id(self))
        print("Recharge Type:", self.recharge_type)
        print("Phone No.:", self.tel)
        print("Operator:", self.operator)
        print("Amount:", self.amount)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")

    def plans(self):
        if self.operator == "Jio":
            print("~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Jio Plan1: 220")
            print("Jio Plan2: 320")
            print("Jio Plan3: 420")
            print("Jio Plan4: 520")
            print("~~~~~~~~~~~~~~~~~~~~~~~~")

        elif self.operator == "Idea":
            print("~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Idea Plan1: 249")
            print("Idea Plan2: 359")
            print("Idea Plan3: 469")
            print("Idea Plan4: 579")
            print("~~~~~~~~~~~~~~~~~~~~~~~~")

        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~")
            print("No Plans for the operator", self.operator)
            print("~~~~~~~~~~~~~~~~~~~~~~~~")

            return False

recharge1 = Recharge()
recharge2 = Recharge("postpaid", 9888888881, "Jio", 200)
recharge3 = Recharge("postpaid", 9666666661, "Idea", 200)
recharge4 = Recharge("prepaid", 9999999999, "Airtel", 200)

recharge1.show()
recharge2.show()
recharge3.show()

recharge1.plans()
recharge2.plans()
recharge3.plans()
recharge4.plans()
