import streamlit as st
from utils.supabase_helper import get_user_history

st.set_page_config(
    page_title="Recipe History",
    page_icon="📜"
)

st.title("📜 Recipe History")

username = st.text_input(
    "Enter your username"
)

if username:

    history = get_user_history(username)

    if history:

        st.success(
            f"Found {len(history)} recipes!"
        )

        for recipe in history:

            with st.expander(
                f"{recipe['recipe_name']} "
                f"({recipe['created_at'][:10]})"
            ):

                st.write(
                    f"**Cuisine:** "
                    f"{recipe['cuisine']}"
                )

                st.write(
                    f"**Meal Type:** "
                    f"{recipe['meal_type']}"
                )

                st.write(
                    f"**Servings:** "
                    f"{recipe['servings']}"
                )

                st.markdown(
                    recipe["recipe_content"]
                )

    else:

        st.info(
            "No recipes found."
        )