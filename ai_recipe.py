import os
from dotenv import load_dotenv
from openai import OpenAI, APIError, RateLimitError

# Load the variables from our .env file
load_dotenv()

# Get our API key
api_key = os.getenv("OPENAI_API_KEY")

# Create the AI client
client = OpenAI(api_key=api_key)


def generate_recipes(ingredients):
    """
    Ask the AI to create three vegetarian recipes
    using the ingredients provided.
    """

    ingredient_text = ", ".join(ingredients)

    prompt = f"""
You are PantryPilot, a vegetarian recipe assistant.

The user has these ingredients:

{ingredient_text}

Create THREE different vegetarian recipes.

Important rules:
- Do NOT use meat.
- Do NOT use chicken.
- Do NOT use beef.
- Do NOT use pork.
- Do NOT use fish.
- Do NOT use seafood.
- Try to use as many of the user's ingredients as reasonably possible.
- Keep the recipes practical for a beginner cook.

For each recipe, provide:
1. Recipe name
2. Short description
3. Ingredients
4. Cooking time
5. Difficulty
6. Step-by-step instructions

Clearly separate the three recipes.
"""

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text

    except RateLimitError:
        return (
            "⚠️ PantryPilot couldn't contact the AI because "
            "your API account has no credits available."
        )

    except APIError as error:
        return f"⚠️ The AI service returned an error: {error}"


    return response.output_text
