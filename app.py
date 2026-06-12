import streamlit as st
from utils.gemini_helper import (
    generate_recipe_suggestions,
    parse_recipe_suggestions,
    generate_full_recipe
)

from utils.supabase_helper import save_recipe
from utils.pdf_generator import (
    generate_recipe_pdf
)

if "full_recipe" not in st.session_state:
    st.session_state.full_recipe = None

if "recipe_saved" not in st.session_state:
    st.session_state.recipe_saved = False
# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="ChefGPT",
    page_icon="🍳",
    layout="wide"
)

# ---------------- INITIALIZE SESSION STATE ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

if "step" not in st.session_state:
    st.session_state.step = "username"

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

if "recipes" not in st.session_state:
    st.session_state.recipes = []

if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = None

# ---------------- APP HEADER ---------------- #

st.title("🍳 ChefGPT")
st.subheader("AI Powered Recipe Generator Based on Your Pantry")

# ---------------- BOT QUESTIONS ---------------- #

questions = {
    "username": "👋 Welcome to ChefGPT! What should I call you? (Choose a username)",

    "ingredients": """🛒 What ingredients do you currently have?

Example:
- eggs
- rice
- onions
- tomatoes""",

    "meal_type": """🍽️ What type of meal are you looking for?

Choose one:
- Breakfast
- Lunch
- Dinner
- Dessert""",

    "cuisine": """🌍 What cuisine do you prefer?

Examples:
- Indian
- Chinese
- Japanese
- Italian
- Mexican
- Any""",

    "servings": "👥 How many people will be eating?",

    "dietary": """🥗 Any dietary preferences?

Choose one:
- Vegetarian
- Vegan
- Jain
- High Protein
- No Preference""",

    "difficulty": """👨‍🍳 Preferred difficulty level?

Choose one:
- Easy
- Medium
- Hard""",

    "appliances": """🔌 What appliances do you have?

Examples:
- Stove
- Oven
- Microwave
- Air Fryer
- Blender
- Rice Cooker"""
}

# ---------------- INITIAL BOT MESSAGE ---------------- #

if len(st.session_state.messages) == 0:
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": questions["username"]
        }
    )
    st.rerun()

# ---------------- DISPLAY CHAT HISTORY ---------------- #

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- USER INPUT ---------------- #

user_input = st.chat_input("Type your answer here...")

if user_input:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    current_step = st.session_state.step

    # Save user responses
    if current_step == "username":
        st.session_state.user_data["username"] = user_input
        st.session_state.step = "ingredients"

    elif current_step == "ingredients":
        st.session_state.user_data["ingredients"] = user_input
        st.session_state.step = "meal_type"

    elif current_step == "meal_type":
        st.session_state.user_data["meal_type"] = user_input
        st.session_state.step = "cuisine"

    elif current_step == "cuisine":
        st.session_state.user_data["cuisine"] = user_input
        st.session_state.step = "servings"

    elif current_step == "servings":
        st.session_state.user_data["servings"] = user_input
        st.session_state.step = "dietary"

    elif current_step == "dietary":
        st.session_state.user_data["dietary"] = user_input
        st.session_state.step = "difficulty"

    elif current_step == "difficulty":
        st.session_state.user_data["difficulty"] = user_input
        st.session_state.step = "appliances"

    elif current_step == "appliances":
        st.session_state.user_data["appliances"] = user_input
        st.session_state.step = "completed"

    # Continue asking questions
    if st.session_state.step != "completed":

        next_question = questions[st.session_state.step]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": next_question
            }
        )

    else:

        summary = f"""
### Perfect! Here's what I gathered:

- Username: {st.session_state.user_data['username']}
- Ingredients: {st.session_state.user_data['ingredients']}
- Meal Type: {st.session_state.user_data['meal_type']}
- Cuisine: {st.session_state.user_data['cuisine']}
- Servings: {st.session_state.user_data['servings']}
- Dietary Preference: {st.session_state.user_data['dietary']}
- Difficulty: {st.session_state.user_data['difficulty']}
- Appliances: {st.session_state.user_data['appliances']}

🍳 Generating recipe suggestions...
"""

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": summary
            }
        )

        # Generate recipes ONLY after all questions are answered
        if not st.session_state.recipes:

            with st.spinner("Generating recipe ideas..."):

                suggestions = generate_recipe_suggestions(
                    ingredients=st.session_state.user_data["ingredients"],
                    meal_type=st.session_state.user_data["meal_type"],
                    cuisine=st.session_state.user_data["cuisine"],
                    servings=st.session_state.user_data["servings"],
                    dietary_preference=st.session_state.user_data["dietary"],
                    difficulty=st.session_state.user_data["difficulty"],
                    appliances=st.session_state.user_data["appliances"]
                )

                st.session_state.recipes = (
                    parse_recipe_suggestions(suggestions)
                )

    st.rerun()

# ---------------- DISPLAY RECIPE SUGGESTIONS ---------------- #

if (
    st.session_state.step == "completed"
    and st.session_state.recipes
):

    st.divider()

    st.header("🍳 Recipe Suggestions")

    for recipe in st.session_state.recipes:

        with st.container(border=True):

            st.subheader(recipe["name"])

            st.write(recipe["description"])

            if st.button(
            f"Select {recipe['name']}",
            key=recipe["name"]):
                

                st.session_state.selected_recipe = recipe["name"]

                with st.spinner("Generating detailed recipe..."):

                    recipe_text = generate_full_recipe(
                        dish_name=recipe["name"],
                        ingredients=st.session_state.user_data["ingredients"],
                        servings=st.session_state.user_data["servings"],
                        dietary_preference=st.session_state.user_data["dietary"],
                        appliances=st.session_state.user_data["appliances"]
                    )

                    st.session_state.full_recipe = recipe_text

                st.rerun()

# ---------------- DISPLAY SELECTED RECIPE ---------------- #

if st.session_state.selected_recipe:

    st.success(
        f"Selected Recipe: {st.session_state.selected_recipe}"
    )

if st.session_state.full_recipe:

    st.divider()

    st.header(
        f"🍽️ {st.session_state.selected_recipe}"
    )

    st.markdown(
        st.session_state.full_recipe
    )
if (
    st.session_state.selected_recipe is not None
    and st.session_state.full_recipe is not None
):

    pdf = generate_recipe_pdf(
        st.session_state.selected_recipe,
        st.session_state.full_recipe
    )

    st.download_button(
        label="📥 Download Recipe PDF",
        data=pdf,
        file_name=f"{st.session_state.selected_recipe}.pdf",
        mime="application/pdf"
    )

if (
    st.session_state.full_recipe
    and not st.session_state.recipe_saved
):

    try:

        save_recipe(
            username=st.session_state.user_data["username"],
            recipe_name=st.session_state.selected_recipe,
            meal_type=st.session_state.user_data["meal_type"],
            cuisine=st.session_state.user_data["cuisine"],
            servings=int(
                st.session_state.user_data["servings"]
            ),
            dietary_preference=st.session_state.user_data["dietary"],
            difficulty=st.session_state.user_data["difficulty"],
            ingredients=st.session_state.user_data["ingredients"],
            missing_ingredients="See recipe details",
            appliances=st.session_state.user_data["appliances"],
            recipe_content=st.session_state.full_recipe,
            nutrition_info="Included in recipe"
        )

        st.session_state.recipe_saved = True

        st.success(
            "✅ Recipe saved to history!"
        )

    except Exception as e:

        st.error(
            f"Failed to save recipe: {e}"
        )
# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("Current Session")

    if st.session_state.user_data:
        st.json(st.session_state.user_data)

    if st.button("🔄 Reset Conversation"):

        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.rerun()