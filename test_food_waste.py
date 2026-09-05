from ranking import calculate_food_waste_score


pantry = [
    "avocado",
    "eggs",
    "spinach",
    "tomatoes"
]

recipe_a = [
    "1 ripe avocado",
    "4 hard-boiled eggs",
    "1 cup fresh spinach",
    "salt to taste"
]

recipe_b = [
    "2 eggs",
    "1 tablespoon olive oil",
    "salt to taste",
    "black pepper to taste"
]


score_a = calculate_food_waste_score(
    recipe_a,
    pantry
)

score_b = calculate_food_waste_score(
    recipe_b,
    pantry
)


print(f"Recipe A food utilization: {score_a}%")
print(f"Recipe B food utilization: {score_b}%")