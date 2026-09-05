import re


def normalize_ingredient(ingredient):
    """
    Convert an ingredient into a simple base ingredient
    for pantry matching.

    Example:
        "4 hard-boiled eggs" -> "egg"
        "1 ripe avocado" -> "avocado"
        "2 cups cooked rice" -> "rice"
    """

    ingredient = ingredient.lower().strip()

    # Remove quantities such as:
    # 2, 1.5, 1/2, etc.
    ingredient = re.sub(
        r"\b\d+(?:[./]\d+)?\b",
        "",
        ingredient
    )

    # Remove common measurement words
    measurements = [
        "cup",
        "cups",
        "tablespoon",
        "tablespoons",
        "tbsp",
        "teaspoon",
        "teaspoons",
        "tsp",
        "ounce",
        "ounces",
        "oz",
        "pound",
        "pounds",
        "lb",
        "lbs",
        "gram",
        "grams",
        "g",
        "kilogram",
        "kilograms",
        "kg"
    ]

    words = ingredient.split()

    words = [
        word
        for word in words
        if word not in measurements
    ]

    ingredient = " ".join(words)

    # Remove common recipe phrases
    phrases_to_remove = [
    "to taste",
    "as needed",
    "for serving",
    ]

    for phrase in phrases_to_remove:
        ingredient = ingredient.replace(
        phrase, ""
        
    )

    # Remove preparation words and descriptions.
    # These don't change the basic pantry ingredient.
    descriptors = [
        # Preparation phrases
        "hard-boiled",
        "hardboiled",
        "soft-boiled",
        "softboiled",

        # Preparation methods
        "boiled",
        "cooked",
        "uncooked",
        "scrambled",
        "fried",
        "baked",
        "roasted",
        "grilled",
        "steamed",

        # Cutting/preparation
        "chopped",
        "diced",
        "sliced",
        "minced",
        "shredded",
        "grated",
        "crushed",
        "mashed",
        "halved",

        # Descriptions
        "fresh",
        "frozen",
        "roughly",
        "finely",
        "thinly",
        "ripe",
        "large",
        "medium",
        "small",
        "whole",

        # Important: "hard" and "soft" must also
        # be removed when they are left behind
        # by phrases such as "hard-boiled".
        "hard",
        "soft"
    ]   

    for descriptor in descriptors:
        ingredient = ingredient.replace(
            descriptor,
            ""
        )

    # Remove punctuation
    ingredient = re.sub(
        r"[^\w\s]",
        " ",
        ingredient
    )

    # Clean extra spaces
    ingredient = " ".join(
        ingredient.split()
    )

    # Handle common plural forms
    if ingredient.endswith("ies"):
        ingredient = ingredient[:-3] + "y"

    elif ingredient.endswith("oes"):
        ingredient = ingredient[:-2]

    elif ingredient.endswith("s") and not ingredient.endswith("ss"):
        ingredient = ingredient[:-1]

    return ingredient
