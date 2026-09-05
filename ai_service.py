import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

from models import Recipe




# Load environment variables
load_dotenv()


# Create Gemini client
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def generate_gemini_recipes(ingredients):
    """
    Ask Gemini to generate three vegetarian recipes
    using structured JSON output.
    """

    ingredient_text = ", ".join(ingredients)

    prompt = f"""
You are PantryPilot, a vegetarian recipe assistant.

The user currently has these ingredients:

{ingredient_text}

Generate THREE different vegetarian recipes.

Rules:

- Every recipe must be vegetarian.
- Never use meat, chicken, beef, pork, fish, or seafood.
- Try to use as many of the user's ingredients as reasonably possible.
- Recipes should be practical for a beginner cook.
- Avoid unusual ingredients.
- Give realistic cooking times.
- Difficulty must be exactly Easy, Medium, or Hard.

Return the recipes using the requested JSON structure.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema={
                "type": "object",
                "properties": {
                    "recipes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "description": {
                                    "type": "string"
                                },
                                "ingredients": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "cooking_time": {
                                    "type": "integer"
                                },
                                "difficulty": {
                                    "type": "string"
                                },
                                "instructions": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                }
                            },
                            "required": [
                                "name",
                                "description",
                                "ingredients",
                                "cooking_time",
                                "difficulty",
                                "instructions"
                            ]
                        }
                    }
                },
                "required": [
                    "recipes"
                ]
            }
        )
    )

    # Gemini should now return valid JSON
    data = json.loads(response.text)

    recipes = []

    for recipe_data in data["recipes"]:

        recipe = Recipe(
            name=recipe_data["name"],
            description=recipe_data["description"],
            ingredients=recipe_data["ingredients"],
            cooking_time=recipe_data["cooking_time"],
            difficulty=recipe_data["difficulty"],
            instructions=recipe_data["instructions"]
        )

        recipes.append(recipe)

    return recipes


# Gemini should return JSON, but AI responses
# can occasionally contain extra characters.

    raw_response = response.text.strip()

    decoder = json.JSONDecoder()

    try:

        data, end_index = decoder.raw_decode(
            raw_response
        )

    except json.JSONDecodeError as error:

        print("Gemini returned invalid JSON:")
        print(raw_response)

        raise ValueError(
            "Could not parse Gemini's response as JSON."
        ) from error





    recipes = []

    for recipe_data in data["recipes"]:

        recipe = Recipe(
            name=recipe_data["name"],
            description=recipe_data["description"],
            ingredients=recipe_data["ingredients"],
            cooking_time=recipe_data["cooking_time"],
            difficulty=recipe_data["difficulty"],
            instructions=recipe_data["instructions"]
        )

        recipes.append(recipe)

    return recipes
