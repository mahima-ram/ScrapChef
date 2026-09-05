from ingredient_utils import normalize_ingredient


def get_normalized_recipe_ingredients(recipe):
    """
    Return a set of normalized ingredients
    used by a recipe.
    """

    return {
        normalize_ingredient(ingredient)
        for ingredient in recipe.ingredients
        if normalize_ingredient(ingredient)
    }


def get_normalized_pantry(pantry):
    """
    Convert the user's pantry into a normalized set.
    """

    return {
        normalize_ingredient(ingredient)
        for ingredient in pantry
        if normalize_ingredient(ingredient)
    }


def get_missing_ingredients(recipe, available_ingredients):
    """
    Find which ingredients are needed for a recipe
    but are not currently available.
    """

    recipe_ingredients = (
        get_normalized_recipe_ingredients(recipe)
    )

    return (
        recipe_ingredients
        - available_ingredients
    )


def calculate_recipe_value(
    recipe,
    pantry,
    available_ingredients
):
    """
    Calculate the value of adding a recipe
    to the current meal plan.

    Rewards:
    - Using ingredients from the user's pantry
    - Reusing ingredients already available

    Penalizes:
    - Introducing new ingredients that must be bought
    """

    recipe_ingredients = (
        get_normalized_recipe_ingredients(recipe)
    )

    normalized_pantry = (
        get_normalized_pantry(pantry)
    )

    # Ingredients from the original pantry
    pantry_used = (
        recipe_ingredients
        & normalized_pantry
    )

    # Ingredients already available because they
    # are either in the pantry or were purchased
    already_available = (
        recipe_ingredients
        & available_ingredients
    )

    # New ingredients this recipe would introduce
    new_ingredients = (
        recipe_ingredients
        - available_ingredients
    )

    # Greedy heuristic
    #
    # Reward pantry usage
    # Reward ingredient reuse
    # Penalize expanding the shopping list

    score = (
        3 * len(pantry_used)
        + 1 * len(already_available - pantry_used)
        - 2 * len(new_ingredients)
    )

    return score, new_ingredients


def build_meal_plan(
    recipes,
    pantry,
    num_meals=3
):
    """
    Build a multi-recipe meal plan using a
    greedy optimization heuristic.

    The algorithm repeatedly selects the recipe
    with the highest marginal value.

    Goal:
    - Maximize pantry utilization
    - Encourage ingredient reuse
    - Minimize new unique ingredients required
    """

    normalized_pantry = (
        get_normalized_pantry(pantry)
    )

    # Ingredients currently available.
    # Starts with the user's pantry.
    available_ingredients = (
        normalized_pantry.copy()
    )

    remaining_recipes = recipes.copy()

    selected_recipes = []

    shopping_list = set()

    while (
        len(selected_recipes) < num_meals
        and remaining_recipes
    ):

        best_recipe = None
        best_score = float("-inf")
        best_new_ingredients = set()

        # Evaluate every recipe not yet selected
        for recipe in remaining_recipes:

            score, new_ingredients = (
                calculate_recipe_value(
                    recipe,
                    pantry,
                    available_ingredients
                )
            )

            if score > best_score:

                best_recipe = recipe
                best_score = score
                best_new_ingredients = (
                    new_ingredients
                )

        # Add the best recipe to the meal plan
        selected_recipes.append(
            best_recipe
        )

        # Add only genuinely new ingredients
        # to the shopping list
        shopping_list.update(
            best_new_ingredients
        )

        # Once an ingredient is purchased,
        # it can be reused by future recipes
        available_ingredients.update(
            get_normalized_recipe_ingredients(
                best_recipe
            )
        )

        # Prevent selecting the same recipe twice
        remaining_recipes.remove(
            best_recipe
        )

    return {
        "selected_recipes": selected_recipes,
        "shopping_list": sorted(
            shopping_list
        ),
        "unique_ingredients_to_buy": len(
            shopping_list
        ),
    }

def get_shopping_list_for_recipes(
    recipes,
    pantry
):
    """
    Calculate the unique ingredients needed
    to make a group of recipes.
    """

    normalized_pantry = (
        get_normalized_pantry(pantry)
    )

    shopping_list = set()

    for recipe in recipes:

        recipe_ingredients = (
            get_normalized_recipe_ingredients(
                recipe
            )
        )

        missing_ingredients = (
            recipe_ingredients
            - normalized_pantry
        )

        shopping_list.update(
            missing_ingredients
        )

    return {
        "shopping_list": sorted(
            shopping_list
        ),
        "unique_ingredients_to_buy": len(
            shopping_list
        ),
    }
