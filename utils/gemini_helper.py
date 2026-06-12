import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = st.secrets.get(
    "GEMINI_API_KEY",
    os.getenv("GEMINI_API_KEY")
)

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)


def generate_recipe_suggestions(
    ingredients,
    meal_type,
    cuisine,
    servings,
    dietary_preference,
    difficulty,
    appliances
):

    prompt = f"""
You are ChefGPT, an expert chef.

Generate EXACTLY 3 recipe suggestions.

User Information:

Ingredients Available:
{ingredients}

Meal Type:
{meal_type}

Cuisine:
{cuisine}

Servings:
{servings}

Dietary Preference:
{dietary_preference}

Difficulty:
{difficulty}

Available Appliances:
{appliances}

IMPORTANT RULES:

1. Use pantry ingredients as much as possible.
2. Missing ingredients should be CHEAP and COMMON.
3. Match cuisine preference.
4. Match dietary preferences strictly.
5. Match difficulty level.
6. Return ONLY this format:

RECIPE 1:
NAME: <recipe name>
DESCRIPTION: <brief description>

RECIPE 2:
NAME: <recipe name>
DESCRIPTION: <brief description>

RECIPE 3:
NAME: <recipe name>
DESCRIPTION: <brief description>
"""

    response = model.generate_content(prompt)

    return response.text

def generate_full_recipe(
    dish_name,
    ingredients,
    servings,
    dietary_preference,
    appliances
):

    prompt = f"""
You are ChefGPT.

Generate a complete recipe.

Dish:
{dish_name}

Available Ingredients:
{ingredients}

Servings:
{servings}

Dietary Preference:
{dietary_preference}

Available Appliances:
{appliances}

Include:

1. Brief overview

2. Ingredients Needed
- exact quantities

3. Missing Ingredients
- inexpensive alternatives

4. Appliances Required

5. Step-by-step instructions

6. Nutritional Information:
- Calories
- Protein
- Carbohydrates
- Fat

7. Cooking Tips

Return in Markdown format.
"""

    response = model.generate_content(prompt)

    return response.text

def parse_recipe_suggestions(text):

    recipes = []

    pattern = r"NAME:\s*(.*?)\nDESCRIPTION:\s*(.*?)(?=\nRECIPE|\Z)"

    matches = re.findall(
        pattern,
        text,
        re.DOTALL
    )

    for match in matches:

        recipes.append(
            {
                "name": match[0].strip(),
                "description": match[1].strip()
            }
        )

    return recipes

def generate_full_recipe(
    dish_name,
    ingredients,
    servings,
    dietary_preference,
    appliances
):

    prompt = f"""
You are ChefGPT, an expert chef.

Generate a detailed recipe for:

Dish: {dish_name}

Available Ingredients:
{ingredients}

Servings:
{servings}

Dietary Preference:
{dietary_preference}

Available Appliances:
{appliances}

IMPORTANT:
- Prioritize using the available ingredients.
- Any missing ingredients should be inexpensive and commonly available.

Return the recipe in EXACTLY this format:

## Overview
Brief description of the dish.

## Ingredients Needed
- ingredient with quantity

## Missing Ingredients
- inexpensive missing ingredient

## Appliances Required
- appliance

## Step-by-Step Instructions
1. Step one
2. Step two

## Nutritional Information
Calories: X kcal
Protein: X g
Carbohydrates: X g
Fat: X g

## Chef Tips
Helpful cooking tips.
"""

    response = model.generate_content(prompt)

    return response.text