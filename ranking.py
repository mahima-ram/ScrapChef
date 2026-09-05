from ingredient_utils import normalize_ingredient

# Common pantry staples have less impact on the score
PANTRY_STAPLES = {
    "salt",
    "black pepper",
    "pepper",
    "oil",
    "olive oil",
    "vegetable oil",
    "water",
}

# Ingredients that are important, but usually secondary
SECONDARY_INGREDIENTS = {
    "garlic",
    "onion",
    "lemon",
    "lemon juice",
    "lime",
    "lime juice",
    "butter",
    "cheese",
    "yogurt",
    "greek yogurt",
    "soy sauce",
    "vinegar",
}

def get_ingredient_weight(ingredient):
    """
    Return an importance weight for an ingredient.
    """

    normalized = normalize_ingredient(ingredient)

    if normalized in PANTRY_STAPLES:
        return 0.5

    if normalized in SECONDARY_INGREDIENTS:
        return 2.0

    return 3.0

def calculate_pantry_match(recipe_ingredients, pantry):
    """
    Calculate a weighted pantry match percentage.

    Main ingredients matter more than pantry staples.
    """

    normalized_pantry = {
        normalize_ingredient(item)
        for item in pantry
    }

    total_weight = 0
    matched_weight = 0

    for item in recipe_ingredients:

        normalized_item = normalize_ingredient(item)

        # Skip empty ingredients
        if not normalized_item:
            continue

        weight = get_ingredient_weight(normalized_item)

        total_weight += weight

        if normalized_item in normalized_pantry:
            matched_weight += weight

    if total_weight == 0:
        return 0

    score = (
        matched_weight / total_weight
    ) * 100

    return round(score)

def calculate_food_waste_score(recipe_ingredients, pantry):
    """
    Calculate how much of the user's pantry
    is used by the recipe.

    A higher score means the recipe uses more
    of the ingredients the user already has.
    """

    normalized_pantry = {
        normalize_ingredient(item)
        for item in pantry
    }

    normalized_recipe = {
        normalize_ingredient(item)
        for item in recipe_ingredients
        if normalize_ingredient(item)
    }

    if not normalized_pantry:
        return 0

    used_ingredients = (
        normalized_pantry
        & normalized_recipe
    )

    score = (
        len(used_ingredients)
        / len(normalized_pantry)
    ) * 100

    return round(score)


def find_missing_ingredients(recipe_ingredients, pantry):
    """
    Find ingredients required by the recipe
    that the user does not already have.
    """

    normalized_pantry = {
        normalize_ingredient(item)
        for item in pantry
    }

    missing = []

    for ingredient in recipe_ingredients:

        normalized_ingredient = normalize_ingredient(
            ingredient
        )

        if normalized_ingredient not in normalized_pantry:
            missing.append(ingredient)

    return missing

def rank_recipes(
    recipes,
    pantry,
    max_time=None,
    preferred_difficulty=None,
    minimize_waste=False
):
    """
    Rank recipes using multiple factors.

    Factors:
    - Weighted pantry match
    - Food utilization / waste reduction
    - Cooking time preference
    - Difficulty preference
    """

    ranked = []

    for recipe in recipes:

        # 1. How much of the recipe can the user make?
        pantry_score = calculate_pantry_match(
            recipe.ingredients,
            pantry
        )

        # 2. How much of the user's pantry does the recipe use?
        waste_score = calculate_food_waste_score(
            recipe.ingredients,
            pantry
        )

        missing_ingredients = find_missing_ingredients(
            recipe.ingredients,
            pantry
        )

        # Start with pantry match as the main score
        final_score = pantry_score

        # If the user wants to minimize food waste,
        # give food utilization additional importance
        if minimize_waste:
            final_score = (
                0.7 * pantry_score
                + 0.3 * waste_score
            )

        # Apply cooking time preference
        if max_time is not None:
            if recipe.cooking_time <= max_time:
                final_score += 5
            else:
                final_score -= 10

        # Apply difficulty preference
        if preferred_difficulty is not None:
            if recipe.difficulty.lower() == preferred_difficulty.lower():
                final_score += 5

        ranked.append(
            {
                "recipe": recipe,
                "score": round(final_score),
                "pantry_score": pantry_score,
                "waste_score": waste_score,
                "missing_ingredients": missing_ingredients,
            }
        )

    ranked.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return ranked



