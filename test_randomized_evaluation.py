import random

from models import Recipe
from meal_planner import (
    build_meal_plan,
    get_shopping_list_for_recipes
)
from ranking import rank_recipes


# ==================================================
# INGREDIENT POOL
# ==================================================

INGREDIENT_POOL = [
    "rice",
    "pasta",
    "eggs",
    "spinach",
    "tomatoes",
    "avocado",
    "potatoes",
    "chickpeas",
    "onion",
    "garlic",
    "olive oil",
    "soy sauce",
    "lemon juice",
    "cumin",
    "cheese",
    "yogurt",
    "bell pepper",
    "carrots",
    "beans",
    "tahini",
]


# ==================================================
# GENERATE RANDOM RECIPE
# ==================================================

def generate_random_recipe(
    recipe_number
):
    """
    Create a random vegetarian recipe
    using ingredients from the pool.
    """

    num_ingredients = random.randint(
        3,
        6
    )

    ingredients = random.sample(
        INGREDIENT_POOL,
        num_ingredients
    )

    return Recipe(
        name=f"Recipe {recipe_number}",
        description="Randomly generated test recipe.",
        ingredients=ingredients,
        cooking_time=random.randint(
            10,
            45
        ),
        difficulty=random.choice(
            [
                "Easy",
                "Medium",
                "Hard"
            ]
        ),
        instructions=[]
    )


# ==================================================
# GENERATE RANDOM SCENARIO
# ==================================================

def generate_random_scenario():

    """
    Generate a random pantry and
    a set of candidate recipes.
    """

    pantry_size = random.randint(
        4,
        8
    )

    pantry = random.sample(
        INGREDIENT_POOL,
        pantry_size
    )

    recipes = []

    for i in range(8):

        recipe = generate_random_recipe(
            i + 1
        )

        recipes.append(recipe)

    return pantry, recipes


# ==================================================
# EVALUATE ONE SCENARIO
# ==================================================
def evaluate_random_scenario():

    pantry, recipes = (
        generate_random_scenario()
    )

    num_meals = 3

    # ==============================================
    # 1. NAIVE BASELINE
    #
    # Simply choose the first 3 recipes.
    # ==============================================

    naive_recipes = recipes[:num_meals]

    naive_results = (
        get_shopping_list_for_recipes(
            naive_recipes,
            pantry
        )
    )

    naive_cost = (
        naive_results[
            "unique_ingredients_to_buy"
        ]
    )

    # ==============================================
    # 2. INDIVIDUAL RECIPE RANKING
    #
    # Rank recipes independently using PantryPilot's
    # existing scoring algorithm, then select the
    # top 3 recipes.
    # ==============================================

    ranked_recipes = rank_recipes(
        recipes,
        pantry,
        minimize_waste=False
    )

    individual_recipes = [
        item["recipe"]
        for item in ranked_recipes[:num_meals]
    ]

    individual_results = (
        get_shopping_list_for_recipes(
            individual_recipes,
            pantry
        )
    )

    individual_cost = (
        individual_results[
            "unique_ingredients_to_buy"
        ]
    )

    # ==============================================
    # 3. GREEDY MULTI-RECIPE OPTIMIZATION
    # ==============================================

    greedy_results = (
        build_meal_plan(
            recipes,
            pantry,
            num_meals=num_meals
        )
    )

    greedy_cost = (
        greedy_results[
            "unique_ingredients_to_buy"
        ]
    )

    # ==============================================
    # RETURN RESULTS
    # ==============================================

    return {
        "naive_cost": naive_cost,
        "individual_cost": individual_cost,
        "greedy_cost": greedy_cost
    }


# ==================================================
# RUN RANDOMIZED EVALUATION
# ==================================================

NUM_SCENARIOS = 100

results = []

for _ in range(NUM_SCENARIOS):

    result = (
        evaluate_random_scenario()
    )

    results.append(result)

# ==================================================
# CALCULATE RESULTS
# ==================================================

total_naive = sum(
    result["naive_cost"]
    for result in results
)

total_individual = sum(
    result["individual_cost"]
    for result in results
)

total_greedy = sum(
    result["greedy_cost"]
    for result in results
)


# --------------------------------------------------
# AVERAGES
# --------------------------------------------------

average_naive = (
    total_naive / NUM_SCENARIOS
)

average_individual = (
    total_individual / NUM_SCENARIOS
)

average_greedy = (
    total_greedy / NUM_SCENARIOS
)


# --------------------------------------------------
# IMPROVEMENT VS NAIVE
# --------------------------------------------------

naive_saved = (
    total_naive
    - total_greedy
)

if total_naive > 0:

    naive_improvement = (
        naive_saved
        / total_naive
    ) * 100

else:

    naive_improvement = 0


# --------------------------------------------------
# IMPROVEMENT VS INDIVIDUAL RANKING
# --------------------------------------------------

individual_saved = (
    total_individual
    - total_greedy
)

if total_individual > 0:

    individual_improvement = (
        individual_saved
        / total_individual
    ) * 100

else:

    individual_improvement = 0


# --------------------------------------------------
# WIN / TIE / LOSS VS INDIVIDUAL RANKING
# --------------------------------------------------

wins = sum(
    1
    for result in results
    if result["greedy_cost"]
    < result["individual_cost"]
)

ties = sum(
    1
    for result in results
    if result["greedy_cost"]
    == result["individual_cost"]
)

losses = sum(
    1
    for result in results
    if result["greedy_cost"]
    > result["individual_cost"]
)


# ==================================================
# DISPLAY RESULTS
# ==================================================

print("\n" + "=" * 60)
print("THREE-WAY RANDOMIZED ALGORITHM EVALUATION")
print("=" * 60)

print(
    f"\nScenarios tested: "
    f"{NUM_SCENARIOS}"
)

print("\nAVERAGE UNIQUE INGREDIENTS TO BUY")

print(
    f"Naive baseline: "
    f"{average_naive:.2f}"
)

print(
    f"Individual ranking: "
    f"{average_individual:.2f}"
)

print(
    f"Greedy optimization: "
    f"{average_greedy:.2f}"
)


print("\nTOTAL UNIQUE INGREDIENTS TO BUY")

print(
    f"Naive baseline: "
    f"{total_naive}"
)

print(
    f"Individual ranking: "
    f"{total_individual}"
)

print(
    f"Greedy optimization: "
    f"{total_greedy}"
)


print("\nGREEDY VS NAIVE")

print(
    f"Ingredients saved: "
    f"{naive_saved}"
)

print(
    f"Reduction: "
    f"{naive_improvement:.1f}%"
)


print("\nGREEDY VS INDIVIDUAL RANKING")

print(
    f"Ingredients saved: "
    f"{individual_saved}"
)

print(
    f"Reduction: "
    f"{individual_improvement:.1f}%"
)


print("\nGREEDY PERFORMANCE VS INDIVIDUAL RANKING")

print(
    f"Wins: "
    f"{wins}"
)

print(
    f"Ties: "
    f"{ties}"
)

print(
    f"Losses: "
    f"{losses}"
)