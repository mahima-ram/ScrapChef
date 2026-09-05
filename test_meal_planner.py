from models import Recipe
from meal_planner import (build_meal_plan, get_shopping_list_for_recipes)



# -----------------------------------------
# Fixed pantry
# -----------------------------------------

pantry = [
    "rice",
    "eggs",
    "spinach",
    "tomatoes",
    "avocado"
]


# -----------------------------------------
# Fixed candidate recipes
# -----------------------------------------

recipe_a = Recipe(
    name="Egg Fried Rice",
    description="Rice and eggs with garlic.",
    ingredients=[
        "rice",
        "eggs",
        "garlic",
        "soy sauce"
    ],
    cooking_time=15,
    difficulty="Easy",
    instructions=[
        "Cook the ingredients."
    ]
)


recipe_b = Recipe(
    name="Spinach Tomato Bowl",
    description="A vegetable bowl with garlic.",
    ingredients=[
        "spinach",
        "tomatoes",
        "garlic",
        "olive oil"
    ],
    cooking_time=15,
    difficulty="Easy",
    instructions=[
        "Cook the ingredients."
    ]
)


recipe_c = Recipe(
    name="Avocado Rice Bowl",
    description="Rice and avocado with lemon.",
    ingredients=[
        "rice",
        "avocado",
        "lemon juice"
    ],
    cooking_time=10,
    difficulty="Easy",
    instructions=[
        "Combine the ingredients."
    ]
)


recipe_d = Recipe(
    name="Simple Egg Bowl",
    description="Eggs with avocado.",
    ingredients=[
        "eggs",
        "avocado",
        "garlic"
    ],
    cooking_time=10,
    difficulty="Easy",
    instructions=[
        "Prepare and serve."
    ]
)


recipes = [
    recipe_a,
    recipe_b,
    recipe_c,
    recipe_d
]

# -----------------------------------------
# BASELINE
# Select the first 3 recipes without
# optimizing for shared ingredients
# -----------------------------------------

baseline_recipes = recipes[:3]

baseline_results = (
    get_shopping_list_for_recipes(
        baseline_recipes,
        pantry
    )
)

# -----------------------------------------
# Build a 3-meal plan
# -----------------------------------------

meal_plan = build_meal_plan(
    recipes,
    pantry,
    num_meals=3
)


# -----------------------------------------
# Display results
# -----------------------------------------

print("\n" + "=" * 50)
print("GREEDY MEAL PLAN")
print("=" * 50)

for position, recipe in enumerate(
    meal_plan["selected_recipes"],
    start=1
):

    print(
        f"{position}. {recipe.name}"
    )


print("\nShopping List:")

if meal_plan["shopping_list"]:

    for ingredient in meal_plan[
        "shopping_list"
    ]:

        print(
            f"- {ingredient}"
        )

else:

    print(
        "Nothing needed!"
    )


print(
    "\nUnique ingredients to buy:",
    meal_plan[
        "unique_ingredients_to_buy"
    ]
)

print("\n" + "=" * 50)
print("BASELINE VS GREEDY COMPARISON")
print("=" * 50)

print("\nBaseline Recipes:")

for recipe in baseline_recipes:

    print(
        f"- {recipe.name}"
    )

print(
    "\nBaseline unique ingredients to buy:",
    baseline_results[
        "unique_ingredients_to_buy"
    ]
)

print(
    "Greedy unique ingredients to buy:",
    meal_plan[
        "unique_ingredients_to_buy"
    ]
)

improvement = (
    baseline_results[
        "unique_ingredients_to_buy"
    ]
    -
    meal_plan[
        "unique_ingredients_to_buy"
    ]
)

print(
    "Ingredients saved by greedy algorithm:",
    improvement
)