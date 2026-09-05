from mock_recipes import create_mock_recipes
from ranking import rank_recipes


# Ingredients the user has
pantry = [
    "rice",
    "eggs",
    "spinach",
    "tomatoes"
]


# Get our sample recipes
recipes = create_mock_recipes(pantry)


# Rank the recipes
ranked_recipes = rank_recipes(
    recipes,
    pantry
)


print()
print("🥕 PantryPilot Recommendations")
print("--------------------------------")


for position, item in enumerate(ranked_recipes, start=1):
    recipe = item["recipe"]
    score = item["score"]
    missing = item["missing_ingredients"]

    print()
    print(f"{position}. {recipe.name}")
    print(f"   Pantry match: {score}%")
    print(f"   Cooking time: {recipe.cooking_time} minutes")
    print(f"   Difficulty: {recipe.difficulty}")
    print(f"   Missing: {missing}")
