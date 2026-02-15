import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()



### Complete functions ###

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