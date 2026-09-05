import streamlit as st

from ai_service import generate_gemini_recipes
from vegetarian_filter import filter_vegetarian_recipes
from ranking import rank_recipes




# -----------------------------------------
# Page configuration
# -----------------------------------------

st.set_page_config(
    page_title="PantryPilot",
    page_icon="🥕",
    layout="centered"
)


# -----------------------------------------
# Header
# -----------------------------------------

st.title("🥕 PantryPilot")

st.write(
    "Your vegetarian recipe assistant."
)

st.write(
    "Tell PantryPilot what ingredients you have, "
    "and we'll find recipes that make the most of them."
)

st.divider()


# -----------------------------------------
# Sidebar controls
# -----------------------------------------

st.sidebar.header("⚙️ Recipe Preferences")

max_time = st.sidebar.slider(
    "Maximum cooking time (minutes)",
    min_value=10,
    max_value=60,
    value=30,
    step=5
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Any", "Easy", "Medium", "Hard"]
)

st.sidebar.divider()

st.sidebar.write("🥬 **Dietary preference**")

st.sidebar.success(
    "Vegetarian recipes only"
)
st.sidebar.info( "🤖 AI: Google Gemini" )

minimize_waste = st.sidebar.checkbox(
    "♻️ Minimize food waste",
    value=True
)




# -----------------------------------------
# Ingredient input
# -----------------------------------------

ingredients_text = st.text_input(
    "What ingredients do you have?",
    placeholder="rice, eggs, spinach, tomatoes"
)


# -----------------------------------------
# Find recipes
# -----------------------------------------

if st.button("✨ Find Recipes"):

    if not ingredients_text.strip():

        st.warning(
            "Please enter at least one ingredient."
        )

    else:

        # Convert input into a clean list
        pantry = [
            ingredient.strip().lower()
            for ingredient in ingredients_text.split(",")
            if ingredient.strip()
        ]
    with st.spinner("🤖 PantryPilot is creating your recipes..."):

        # Generate recipe candidates
        recipes = generate_gemini_recipes(pantry)

        # Make sure only vegetarian recipes continue
        recipes = filter_vegetarian_recipes(recipes)


        # -----------------------------------------
        # Apply cooking-time filter
        # -----------------------------------------

        recipes = [
            recipe
            for recipe in recipes
            if recipe.cooking_time <= max_time
        ]

        # -----------------------------------------
        # Apply difficulty filter
        # -----------------------------------------

        if difficulty != "Any":

            recipes = [
                recipe
                for recipe in recipes
                if recipe.difficulty == difficulty
            ]

        # -----------------------------------------
        # Handle no matching recipes
        # -----------------------------------------

        if not recipes:

            st.warning(
                "No recipes matched your preferences. "
                "Try increasing the cooking time or "
                "changing the difficulty."
            )

        else:

            # Rank recipes
            ranked_recipes = rank_recipes(
                recipes,
                pantry,
                minimize_waste=minimize_waste
            )

            st.subheader(
                "🍽️ Your Recipe Matches"
            )

            # -----------------------------------------
            # Display recipes
            # -----------------------------------------

            for position, item in enumerate(
                ranked_recipes,
                start=1
            ):

                recipe = item["recipe"]
                score = item["score"]
                missing = item["missing_ingredients"]
                pantry_score = item["pantry_score"]
                waste_score = item["waste_score"]

                st.divider()

                # Recipe title
                if position == 1:

                    st.subheader(
                        f"🥇 {recipe.name}"
                    )

                elif position == 2:

                    st.subheader(
                        f"🥈 {recipe.name}"
                    )

                elif position == 3:

                    st.subheader(
                        f"🥉 {recipe.name}"
                    )

                else:

                    st.subheader(
                        f"{position}. {recipe.name}"
                    )

                # Description
                st.write(
                    recipe.description
                )

                # Recipe metrics
                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.metric(
                        "Pantry Match",
                        f"{pantry_score}%"
                    )

                with col2:
                    st.metric(
                         "Food Utilization",
                         f"{waste_score}%"
                        )


                with col3:

                    st.metric(
                        "Time",
                        f"{recipe.cooking_time} min"
                    )

                with col4:

                    st.metric(
                        "Difficulty",
                        recipe.difficulty
                    )

                # Ingredients
                st.write(
                    "### 🥕 Ingredients"
                )

                for ingredient in recipe.ingredients:

                    if ingredient in pantry:

                        st.write(
                            f"✅ {ingredient}"
                        )

                    else:

                        st.write(
                            f"🛒 {ingredient}"
                        )

                # Missing ingredients
                if missing:

                    st.info(
                        "🛒 You'll need: "
                        + ", ".join(missing)
                    )

                else:

                    st.success(
                        "🎉 You already have everything!"
                    )

                # Instructions
                with st.expander(
                    "👩‍🍳 Show cooking instructions"
                ):

                    for step_number, step in enumerate(
                        recipe.instructions,
                        start=1
                    ):

                        st.write(
                            f"**{step_number}.** {step}"
                        )

