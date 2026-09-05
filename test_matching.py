from ingredient_utils import normalize_ingredient


test_ingredients = [
    "eggs",
    "4 hard-boiled eggs",
    "avocado",
    "1 ripe avocado",
    "2 cups cooked rice",
    "1 medium tomato",
    "3 fresh spinach leaves",
]


for ingredient in test_ingredients:

    normalized = normalize_ingredient(
        ingredient
    )

    print(
        f"{ingredient:<30} → {normalized}"
    )
