def get_ingredients(dish, recipes, count_dish):
    for rec_dish, count in recipes.get(dish, {}).items():
        if not rec_dish in list(recipes.keys()):
            if RESULT_DICT.get(rec_dish) is None:
                RESULT_DICT[rec_dish] = count_dish * count
            else:
                RESULT_DICT[rec_dish] += count_dish * count
        else:
            get_ingredients(rec_dish, recipes, count_dish * count)


for _ in range(int(input())):

    n, k, f = map(int, input().split())
    RESULT_DICT = {}

    dishes = []  # блюда
    recipes = {}  # рецепты
    refrigerator = {}  # холодильник

    for _ in range(n):
        dish, count = input().split()
        dishes.append((dish, int(count)))

    # рецепты
    for _ in range(k):
        recipe, count_ingredients = input().split()
        recipes[recipe] = {}

        # ингредиенты
        for _ in range(int(count_ingredients)):
            ingredient, count = input().split()

            recipes[recipe][ingredient] = int(count)

    # холодильник
    for _ in range(f):
        ingredient, count_ingredients = input().split()
        refrigerator[ingredient] = int(count_ingredients)

    # проход по всем блюдам
    for dish, dish_count in dishes:
        get_ingredients(dish, recipes, dish_count)

    for ingredient, count_ingredients in refrigerator.items():
        if RESULT_DICT.get(ingredient) is not None:
            RESULT_DICT[ingredient] -= count_ingredients

            if RESULT_DICT[ingredient] <= 0:
                del RESULT_DICT[ingredient]

    for ingredient, count in sorted(RESULT_DICT.items(), key=lambda x: x[0]):
        print(ingredient, count)
