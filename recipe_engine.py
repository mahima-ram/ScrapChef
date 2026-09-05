def create_recipe_ideas(ingredients):
    """
    Create vegetarian recipe ideas based on the ingredients provided.
    """

    recipes = []

    # Check whether we have rice
    if "rice" in ingredients:
        recipes.append("🥗 Vegetarian Fried Rice")

    # Check whether we have pasta
    if "pasta" in ingredients:
        recipes.append("🍝 Vegetable Pasta")

    # Check whether we have eggs
    if "eggs" in ingredients:
        recipes.append("🍳 Vegetable Egg Scramble")

    # Check whether we have potatoes
    if "potatoes" in ingredients:
        recipes.append("🥔 Loaded Vegetable Potatoes")

    # If we don't recognize any ingredients
    if len(recipes) == 0:
        recipes.append("🥕 Mixed Vegetable Bowl")

    return recipes

