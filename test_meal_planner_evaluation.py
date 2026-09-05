from models import Recipe
from meal_planner import (
    build_meal_plan,
    get_shopping_list_for_recipes
)


def evaluate_scenario(
    scenario_name,
    pantry,
    recipes,
    num_meals=3
):
    """
    Compare a simple baseline against
    the greedy meal-planning algorithm.
    """

    # ------------------------------
    # BASELINE
    # ------------------------------

    baseline_recipes = recipes[:num_meals]

    baseline_results = (
        get_shopping_list_for_recipes(
            baseline_recipes,
            pantry
        )
    )

    # ------------------------------
    # GREEDY ALGORITHM
    # ------------------------------

    greedy_results = (
        build_meal_plan(
            recipes,
            pantry,
            num_meals=num_meals
        )
    )

    baseline_cost = (
        baseline_results[
            "unique_ingredients_to_buy"
        ]
    )

    greedy_cost = (
        greedy_results[
            "unique_ingredients_to_buy"
        ]
    )

    saved = (
        baseline_cost
        - greedy_cost
    )

    if baseline_cost > 0:

        percent_improvement = (
            saved / baseline_cost
        ) * 100

    else:

        percent_improvement = 0

    # ------------------------------
    # DISPLAY RESULTS
    # ------------------------------

    print("\n" + "=" * 60)
    print(f"SCENARIO: {scenario_name}")
    print("=" * 60)

    print(
        f"Baseline ingredients to buy: "
        f"{baseline_cost}"
    )

    print(
        f"Greedy ingredients to buy: "
        f"{greedy_cost}"
    )

    print(
        f"Ingredients saved: "
        f"{saved}"
    )

    print(
        f"Improvement: "
        f"{percent_improvement:.1f}%"
    )

    return {
        "scenario": scenario_name,
        "baseline_cost": baseline_cost,
        "greedy_cost": greedy_cost,
        "saved": saved,
        "improvement": percent_improvement,
    }


# ==================================================
# SCENARIO 1
# ==================================================

pantry_1 = [
    "rice",
    "eggs",
    "spinach",
    "tomatoes",
    "avocado"
]

recipes_1 = [

    Recipe(
        name="Egg Fried Rice",
        description="",
        ingredients=[
            "rice",
            "eggs",
            "garlic",
            "soy sauce"
        ],
        cooking_time=15,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Spinach Tomato Bowl",
        description="",
        ingredients=[
            "spinach",
            "tomatoes",
            "garlic",
            "olive oil"
        ],
        cooking_time=15,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Avocado Rice Bowl",
        description="",
        ingredients=[
            "rice",
            "avocado",
            "lemon juice"
        ],
        cooking_time=10,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Simple Egg Bowl",
        description="",
        ingredients=[
            "eggs",
            "avocado",
            "garlic"
        ],
        cooking_time=10,
        difficulty="Easy",
        instructions=[]
    ),
]


# ==================================================
# SCENARIO 2
# Designed to reward ingredient sharing
# ==================================================

pantry_2 = [
    "pasta",
    "spinach",
    "tomatoes",
    "chickpeas"
]

recipes_2 = [

    Recipe(
        name="Tomato Pasta",
        description="",
        ingredients=[
            "pasta",
            "tomatoes",
            "garlic",
            "olive oil"
        ],
        cooking_time=20,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Spinach Chickpea Bowl",
        description="",
        ingredients=[
            "spinach",
            "chickpeas",
            "lemon juice",
            "cumin"
        ],
        cooking_time=20,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Garlic Spinach Pasta",
        description="",
        ingredients=[
            "pasta",
            "spinach",
            "garlic",
            "olive oil"
        ],
        cooking_time=20,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Chickpea Tomato Stew",
        description="",
        ingredients=[
            "chickpeas",
            "tomatoes",
            "garlic",
            "cumin"
        ],
        cooking_time=25,
        difficulty="Medium",
        instructions=[]
    ),
]


# ==================================================
# SCENARIO 3
# Another ingredient-sharing scenario
# ==================================================

pantry_3 = [
    "rice",
    "potatoes",
    "eggs",
    "spinach"
]

recipes_3 = [

    Recipe(
        name="Potato Egg Hash",
        description="",
        ingredients=[
            "potatoes",
            "eggs",
            "onion",
            "olive oil"
        ],
        cooking_time=20,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Spinach Rice Bowl",
        description="",
        ingredients=[
            "rice",
            "spinach",
            "soy sauce",
            "sesame oil"
        ],
        cooking_time=15,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Garlic Potato Bowl",
        description="",
        ingredients=[
            "potatoes",
            "spinach",
            "garlic",
            "olive oil"
        ],
        cooking_time=20,
        difficulty="Easy",
        instructions=[]
    ),

    Recipe(
        name="Egg Fried Rice",
        description="",
        ingredients=[
            "rice",
            "eggs",
            "garlic",
            "soy sauce"
        ],
        cooking_time=15,
        difficulty="Easy",
        instructions=[]
    ),
]


# ==================================================
# RUN EVALUATION
# ==================================================

results = []

results.append(
    evaluate_scenario(
        "Pantry Sharing",
        pantry_1,
        recipes_1
    )
)

results.append(
    evaluate_scenario(
        "Shared Grocery Ingredients",
        pantry_2,
        recipes_2
    )
)

results.append(
    evaluate_scenario(
        "Meal Combination Optimization",
        pantry_3,
        recipes_3
    )
)


# ==================================================
# SUMMARY
# ==================================================

print("\n" + "=" * 60)
print("OVERALL EVALUATION")
print("=" * 60)

total_baseline = sum(
    result["baseline_cost"]
    for result in results
)

total_greedy = sum(
    result["greedy_cost"]
    for result in results
)

total_saved = (
    total_baseline
    - total_greedy
)

if total_baseline > 0:

    overall_improvement = (
        total_saved / total_baseline
    ) * 100
    average_savings = (
    total_saved / len(results)
    )

    print(
    f"Average ingredients saved per scenario: "
    f"{average_savings:.2f}"
    )

else:

    overall_improvement = 0


print(
    f"Total baseline ingredients: "
    f"{total_baseline}"
)

print(
    f"Total greedy ingredients: "
    f"{total_greedy}"
)

print(
    f"Total ingredients saved: "
    f"{total_saved}"
)

print(
    f"Overall improvement: "
    f"{overall_improvement:.1f}%"
)