from vegetarian_filter import is_vegetarian


test_cases = [
    ["rice", "spinach", "eggs"],
    ["rice", "chicken breast", "spinach"],
    ["vegetables", "beef broth"],
    ["rice", "fish sauce"],
    ["pasta", "tomatoes", "cheese"],
    ["vegetable broth", "carrots", "potatoes"],
]


for ingredients in test_cases:

    result = is_vegetarian(ingredients)

    print(
        f"{ingredients} → {result}"
    )

