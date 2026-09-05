from models import Recipe
from ranking import rank_recipes


# -----------------------------------------
# Fixed pantry for reproducible testing
# -----------------------------------------

pantry = [
    "rice",
    "eggs",
    "spinach",
    "tomatoes",
    "avocado"
]


# -----------------------------------------
# Fixed recipes
# -----------------------------------------

recipe_a = Recipe(
    name="Simple Egg Rice",
    description="A simple recipe that uses only a small portion of the pantry.",
    ingredients=[
        "2 cups cooked rice",
        "2 eggs",
        "salt to taste",
        "black pepper to taste",
        "olive oil"
    ],
    cooking_time=15,
    difficulty="Easy",
    instructions=[
        "Cook the ingredients.",
        "Serve warm."
    ]
)


recipe_b = Recipe(
    name="Vegetable Power Bowl",
    description="A recipe designed to use most of the user's pantry.",
    ingredients=[
        "1 avocado",
        "2 eggs",
        "1 cup spinach",
        "1 tomato",
        "1 cup cooked rice",
        "1 tablespoon tahini",
        "1 tablespoon lemon juice",
        "salt to taste"
    ],
    cooking_time=20,
    difficulty="Easy",
    instructions=[
        "Prepare the ingredients.",
        "Combine and serve."
    ]
)

recipes = [
    recipe_a,
    recipe_b
]


# -----------------------------------------
# Test 1: Normal ranking
# -----------------------------------------

print("\n" + "=" * 50)
print("WITHOUT FOOD-WASTE OPTIMIZATION")
print("=" * 50)

normal_ranking = rank_recipes(
    recipes,
    pantry,
    minimize_waste=False
)

for position, item in enumerate(
    normal_ranking,
    start=1
):
    print(
        f"{position}. {item['recipe'].name}"
    )
    print(
        f"   Pantry Match: "
        f"{item['pantry_score']}%"
    )
    print(
        f"   Food Utilization: "
        f"{item['waste_score']}%"
    )
    print(
        f"   Final Score: "
        f"{item['score']}"
    )


# -----------------------------------------
# Test 2: Food-waste optimization enabled
# -----------------------------------------

print("\n" + "=" * 50)
print("WITH FOOD-WASTE OPTIMIZATION")
print("=" * 50)

waste_ranking = rank_recipes(
    recipes,
    pantry,
    minimize_waste=True
)

for position, item in enumerate(
    waste_ranking,
    start=1
):
    print(
        f"{position}. {item['recipe'].name}"
    )
    print(
        f"   Pantry Match: "
        f"{item['pantry_score']}%"
    )
    print(
        f"   Food Utilization: "
        f"{item['waste_score']}%"
    )
    print(
        f"   Final Score: "
        f"{item['score']}"
    )