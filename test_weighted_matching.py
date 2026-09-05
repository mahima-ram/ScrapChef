from ranking import (
    calculate_pantry_match,
    get_ingredient_weight
)
from ingredient_utils import normalize_ingredient


pantry = [
    "avocado",
    "eggs"
]

recipe_ingredients = [
    "4 hard-boiled eggs",
    "1 ripe avocado",
    "1 tablespoon lemon juice",
    "1 tablespoon Greek yogurt",
    "salt to taste",
    "black pepper to taste"
]


print("\nINGREDIENT BREAKDOWN")
print("-" * 40)

normalized_pantry = {
    normalize_ingredient(item)
    for item in pantry
}

for item in recipe_ingredients:

    normalized = normalize_ingredient(item)

    weight = get_ingredient_weight(
        normalized
    )

    has_ingredient = normalized in normalized_pantry

    status = "MATCH" if has_ingredient else "MISSING"

    print(
        f"{item:<35} "
        f"→ {normalized:<20} "
        f"Weight: {weight} "
        f"[{status}]"
    )


score = calculate_pantry_match(
    recipe_ingredients,
    pantry
)

print("\n" + "-" * 40)
print(f"FINAL WEIGHTED SCORE: {score}%")