#docstring Question 6
"""This program defines a class 'Dish' and a class 'Cookbook' to manage a collection
of dishes. It allows adding, viewing, searching, updating, and removing dishes 
using a menu-driven approach."""

print(__doc__)
print()

class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions

class Cookbook:
    def __init__(self):
        self.dishes = []

    def add_dishes(self,dish):
        self.dishes.append(dish)
        print("Dish added successfully")
    
    def show_dishes(self):
        if not self.dishes:
            print("No dishes available,")
        for num in self.dishes:
            print(f"ID          : {num.dish_id}")
            print(f"Name        : {num.dish_name}")
            print(f"Ingredients : {num.ingredients}")
            print(f"Instructions: {num.instructions}")

    def search_dishes(self, name):
        found = False
        for num in self.dishes:
            if num.dish_name == name:
                print(f"Dish Found : {num.dish_name}")
                found = True
        if not found:
            print("Dish not found!")
    
    def remove_dishes(self, dish_id):
        for num in self.dishes:
            if num.dish_id == dish_id:
                self.dishes.remove(num)
                print("Dish removed successfully.")
                return
        print("Invalid dish ID.")
    
    def update_dishes(self, dish_id):
        for num in self.dishes:
            if num.dish_id == dish_id:
                num.dish_name = input("Enter new name: ")
                num.ingredients = input("Enter new ingredients: ")
                num.instructions = input("Enter new instructions: ")
                print("Dish updated successfully.")
                return
        print("Invalid dish ID.")
cookbook = Cookbook()



while True:
    print("\nSelect an option: ")
    print(f"1. Add dishes")
    print(f"2. Show all dishes")
    print(f"3. Remove a dish")
    print(f"4. Update a dish")
    print(f"5. Search a dish")
    print("6. Exit")

    opt = int(input("Enter your choice(1-5):  "))
    if opt == 1:
        rng = int(input("Enter the no.of dishes you want to input:"))
        for i in range(rng):
            id= int(input("Enter dish id:"))
            name = input("Enter dish name:")
            ingredients = input("Enter ingredients :")
            instructions = input("Enter instructions:")
            dish = Dish(id, name, ingredients, instructions)
            cookbook.add_dishes(dish)
    elif opt == 2:
        cookbook.show_dishes()
    elif opt == 3:
        dish_id = int(input("Enter dish ID to remove: "))
        cookbook.remove_dishes(dish_id)
    elif opt == 4:
        dish_id = int(input("Enter dish ID to update: "))
        cookbook.update_dishes(dish_id)
    elif opt == 5:
        name = input("Enter dish name to search: ")
        cookbook.search_dishes(name)
    elif opt == 6:
        break
    else:
        print(f"Invalid input!")
        break