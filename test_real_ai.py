from ai_service import generate_gemini_recipes


ingredients = [
    "rice",
    "eggs",
    "spinach",
    "tomatoes"
]


print("🤖 Asking Gemini for recipes...")

recipes = generate_gemini_recipes(
    ingredients
)


print()
print(f"Gemini generated {len(recipes)} recipes.")

for number, recipe in enumerate(
    recipes,
    start=1
):

    print()
    print(f"{number}. {recipe.name}")
    print(
        f"   Time: {recipe.cooking_time} minutes"
    )
    print(
        f"   Difficulty: {recipe.difficulty}"
    )
    print(
        f"   Ingredients: "
        f"{', '.join(recipe.ingredients)}"
    )
