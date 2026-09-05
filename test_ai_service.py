from ai_service import generate_mock_ai_recipes
from vegetarian_filter import filter_vegetarian_recipes


ingredients = [
    "rice",
    "eggs",
    "spinach",
    "tomatoes"
]


# Generate recipes
recipes = generate_mock_ai_recipes(
    ingredients
)


print("Recipes generated:", len(recipes))


# Apply vegetarian filter
vegetarian_recipes = filter_vegetarian_recipes(
    recipes
)


print(
    "Vegetarian recipes:",
    len(vegetarian_recipes)
)


for recipe in vegetarian_recipes:

    print()
    print(recipe.name)
    print(recipe.ingredients)
