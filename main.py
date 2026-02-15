import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

### Data ###

# recipes = {
#     "small": {
#         "ingredients": {
#             "bread": 2,  ## slice
#             "ham": 4,  ## slice
#             "cheese": 4,  ## ounces
#         },
#         "cost": 1.75,
#     },
#     "medium": {
#         "ingredients": {
#             "bread": 4,  ## slice
#             "ham": 6,  ## slice
#             "cheese": 8,  ## ounces
#         },
#         "cost": 3.25,
#     },
#     "large": {
#         "ingredients": {
#             "bread": 6,  ## slice
#             "ham": 8,  ## slice
#             "cheese": 12,  ## ounces
#         },
#         "cost": 5.5,
#     }
# }
#
# resources = {
#     "bread": 12,  ## slice
#     "ham": 18,  ## slice
#     "cheese": 24,  ## ounces
# }


### Complete functions ###

# class SandwichMachine:
#
#     def __init__(self, machine_resources):
#         """Receives resources as input.
#            Hint: bind input variable to self variable"""
#         self.machine_resources = machine_resources


### Make an instance of SandwichMachine class and write the rest of the codes ###

# machine = SandwichMachine(resources)
is_on = True

while (is_on):
    userInput = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if (userInput == "off"):
        is_on = False
        print("Machine is now off")

    elif (userInput == "report"):
        print("Bread: " + str(sandwich_maker_instance.machine_resources["bread"]) + " slice(s).")
        print("Ham: " + str(sandwich_maker_instance.machine_resources["ham"]) + " slice(s).")
        print("Cheese: " + str(sandwich_maker_instance.machine_resources["cheese"]) + " ounces(s).")

    elif (userInput == "small"):
        recipe = recipes["small"]
        if (sandwich_maker_instance.check_resources(recipe["ingredients"])):
            payment = cashier_instance.process_coins()
            if (cashier_instance.transaction_result(payment, recipe["cost"])):
                sandwich_maker_instance.make_sandwich("small", recipe["ingredients"])
                print(userInput + " sandwich is ready. Bon appetit!")

    elif (userInput == "medium"):
        recipe = recipes["medium"]
        if (sandwich_maker_instance.check_resources(recipe["ingredients"])):
            payment = cashier_instance.process_coins()
            if (cashier_instance.transaction_result(payment, recipe["cost"])):
                sandwich_maker_instance.make_sandwich("medium", recipe["ingredients"])
                print(userInput + " sandwich is ready. Bon appetit!")

    elif (userInput == "large"):
        recipe = recipes["large"]
        if (sandwich_maker_instance.check_resources(recipe["ingredients"])):
            payment = cashier_instance.process_coins()
            if (cashier_instance.transaction_result(payment, recipe["cost"])):
                sandwich_maker_instance.make_sandwich("large", recipe["ingredients"])
                print(userInput + " sandwich is ready. Bon appetit!")
    else:
        print("Invalid input.")