from recipe_engine import create_recipe_ideas

print("🥕 Welcome to PantryPilot!")
print("Your vegetarian AI recipe assistant.")
print()

# Ask the user what ingredients they have
ingredients = input("What ingredients do you have? ")

# Turn the user's answer into a list
ingredient_list = ingredients.split(",")

# Remove extra spaces and convert everything to lowercase
ingredient_list = [
    ingredient.strip().lower()
    for ingredient in ingredient_list
]

print()
print("Great! Here's what you have:")

for ingredient in ingredient_list:
    print(f"✓ {ingredient}")

# Generate recipe ideas
recipes = create_recipe_ideas(ingredient_list)

print()
print("🍽️ Here are some recipe ideas:")

for recipe in recipes:
    print(f"• {recipe}")
