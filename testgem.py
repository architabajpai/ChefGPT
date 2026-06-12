from utils.gemini_helper import (
    generate_recipe_suggestions,
    generate_full_recipe
)

suggestions = generate_recipe_suggestions(
    ingredients="rice, eggs, onions",
    meal_type="Dinner",
    cuisine="Chinese",
    servings=2,
    dietary_preference="No Preference",
    difficulty="Easy",
    appliances="Stove"
)

print("SUGGESTIONS:")
print(suggestions)

print("\n\n")

recipe = generate_full_recipe(
    dish_name="Egg Fried Rice",
    ingredients="rice, eggs, onions",
    servings=2,
    dietary_preference="No Preference",
    appliances="Stove"
)

print("FULL RECIPE:")
print(recipe)