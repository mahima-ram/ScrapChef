from models import Recipe


def create_mock_recipes(pantry):
    """
    Create sample vegetarian recipes for testing.

    This temporarily acts like our AI recipe generator.
    """

    recipes = [
        Recipe(
            name="Vegetable Fried Rice",
            description="A quick and easy fried rice packed with vegetables.",
            ingredients=[
                "rice",
                "eggs",
                "spinach",
                "soy sauce"
            ],
            cooking_time=20,
            difficulty="Easy",
            instructions=[
                "Cook the rice.",
                "Cook the vegetables in a pan.",
                "Add the eggs and scramble them.",
                "Add the rice and soy sauce.",
                "Stir everything together and serve."
            ]
        ),

        Recipe(
            name="Creamy Spinach Pasta",
            description="A simple vegetarian pasta with a creamy spinach sauce.",
            ingredients=[
                "pasta",
                "spinach",
                "cheese",
                "milk"
            ],
            cooking_time=25,
            difficulty="Easy",
            instructions=[
                "Cook the pasta.",
                "Cook the spinach in a pan.",
                "Add milk and cheese.",
                "Mix the sauce with the pasta.",
                "Serve warm."
            ]
        ),

        Recipe(
            name="Vegetable Egg Bowl",
            description="A simple bowl of rice, vegetables, and scrambled eggs.",
            ingredients=[
                "rice",
                "eggs",
                "tomatoes",
                "spinach"
            ],
            cooking_time=15,
            difficulty="Easy",
            instructions=[
                "Cook the rice.",
                "Cook the vegetables.",
                "Scramble the eggs.",
                "Combine everything in a bowl.",
                "Serve immediately."
            ]
        )
    ]

    return recipes
