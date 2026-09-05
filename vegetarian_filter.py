# Words and phrases that indicate an ingredient
# is not vegetarian.

NON_VEGETARIAN_KEYWORDS = {
    "chicken",
    "beef",
    "pork",
    "bacon",
    "ham",
    "turkey",
    "lamb",
    "steak",
    "sausage",
    "pepperoni",
    "salami",
    "prosciutto",
    "fish",
    "salmon",
    "tuna",
    "shrimp",
    "prawn",
    "crab",
    "lobster",
    "anchovy",
    "anchovies",
    "meat",
    "seafood",
    "chicken broth",
    "chicken stock",
    "beef broth",
    "beef stock",
    "fish sauce",
    "oyster sauce",
}

def is_vegetarian(ingredients):
    """
    Check whether all ingredients are vegetarian.

    Returns True if no non-vegetarian ingredient
    is detected.
    """

    for ingredient in ingredients:

        ingredient_lower = ingredient.lower()

        for forbidden_food in NON_VEGETARIAN_KEYWORDS:

            if forbidden_food in ingredient_lower:
                return False

    return True


def filter_vegetarian_recipes(recipes):
    """
    Return only recipes whose ingredients
    are vegetarian.
    """

    vegetarian_recipes = []

    for recipe in recipes:

        if is_vegetarian(recipe.ingredients):
            vegetarian_recipes.append(recipe)

    return vegetarian_recipes


