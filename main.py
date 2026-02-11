import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = #####
cashier_instance = ######

### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if self.machine_resources[ingredient] < ingredients[ingredient]:
                print("Sorry, there is not enough " + ingredient)
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        total = int(input("how many dollars?: ")) * 1.0
        total += int(input("how many half dollars?: ")) * 0.5
        total += int(input("how many quarters?: ")) * 0.25
        total += int(input("how many nickels?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if (coins >= cost):
            change = round(coins - cost, 2)
            print("Here is $" + str(change) + " in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient in order_ingredients:
            self.machine_resources[ingredient] -= order_ingredients[ingredient]

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)
is_on = True

while (is_on):
    userInput = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if (userInput == "off"):
        is_on = False
        print("Machine is now off")

    elif (userInput == "report"):
        print("Bread: " + str(machine.machine_resources["bread"]) + " slice(s).")
        print("Ham: " + str(machine.machine_resources["ham"]) + " slice(s).")
        print("Cheese: " + str(machine.machine_resources["cheese"]) + " ounces(s).")

    elif (userInput == "small"):
        recipe = recipes["small"]
        if (machine.check_resources(recipe["ingredients"])):
            payment = machine.process_coins()
            if (machine.transaction_result(payment, recipe["cost"])):
                machine.make_sandwich("small", recipe["ingredients"])
                print(userInput + " sandwich is ready. Bon appetit!")

    elif (userInput == "medium"):
        recipe = recipes["medium"]
        if (machine.check_resources(recipe["ingredients"])):
            payment = machine.process_coins()
            if (machine.transaction_result(payment, recipe["cost"])):
                machine.make_sandwich("medium", recipe["ingredients"])
                print(userInput + " sandwich is ready. Bon appetit!")

    elif (userInput == "large"):
        recipe = recipes["large"]
        if (machine.check_resources(recipe["ingredients"])):
            payment = machine.process_coins()
            if (machine.transaction_result(payment, recipe["cost"])):
                machine.make_sandwich("large", recipe["ingredients"])
                print(userInput + " sandwich is ready. Bon appetit!")
    else:
        print("Invalid input.")