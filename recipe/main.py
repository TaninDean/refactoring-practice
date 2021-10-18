from recipe import Recipe

if __name__ == '__main__':
    recipe1 = Recipe("Coffee with sugar")
    recipe1.create_recipe(4, 2, 0, 30)
    print(recipe1)

    recipe2 = Recipe("Latte")
    recipe2.create_recipe(3, 2, 1, 40)
    print(recipe2)


    recipe3 = Recipe("Hot Chocolate")
    recipe3.create_recipe(0, 3, 2, 4, 30)
    print(recipe3)
    