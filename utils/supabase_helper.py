from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# Function to save a recipe
def save_recipe(
    username,
    recipe_name,
    meal_type,
    cuisine,
    servings,
    dietary_preference,
    difficulty,
    ingredients,
    missing_ingredients,
    appliances,
    recipe_content,
    nutrition_info
):

    data = {
        "username": username,
        "recipe_name": recipe_name,
        "meal_type": meal_type,
        "cuisine": cuisine,
        "servings": servings,
        "dietary_preference": dietary_preference,
        "difficulty": difficulty,
        "ingredients": ingredients,
        "missing_ingredients": missing_ingredients,
        "appliances": appliances,
        "recipe_content": recipe_content,
        "nutrition_info": nutrition_info
    }

    response = (
        supabase
        .table("recipes")
        .insert(data)
        .execute()
    )

    return response

# Function to retrieve a user's recipe history
def get_user_history(username):

    response = (
        supabase
        .table("recipes")
        .select("*")
        .eq("username", username)
        .order("created_at", desc=True)
        .execute()
    )

    return response.data

# Function to delete a recipe
def delete_recipe(recipe_id):

    response = (
        supabase
        .table("recipes")
        .delete()
        .eq("id", recipe_id)
        .execute()
    )

    return response