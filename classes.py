class Pizza:

    def __init__(self):

        self.style = ""
        self.size = ""
        self.toppings = []

    def add_topping(self, new_topping):

        self.toppings.append(new_topping)

    def print_order(self):

        if len(self.toppings) == 1:
            print(f"I would like a {self.size}, {self.style} pizza with {str(self.toppings[0])}.")
        else:
            print(f"I would like a {self.size}, {self.style} pizza with {' and '.join(self.toppings)}.")



veg_lover = Pizza()

veg_lover.size = "large"
veg_lover.style = "thin crust"
veg_lover.add_topping("tofu")
veg_lover.add_topping("broccoli")

veg_lover.print_order()
