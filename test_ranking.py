
from ranking import calculate_match_score


pantry = [
    "rice",
    "eggs",
    "spinach",
    "tomatoes"
]


recipe_ingredients = [
    "rice",
    "eggs",
    "spinach",
    "cheese"
]


score = calculate_match_score(
    recipe_ingredients,
    pantry
)


print(f"Pantry match: {score}%")

