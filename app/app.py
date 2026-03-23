import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Smart Recipe Recommender", layout="wide")

# Load data
df = pd.read_csv("data/recipes.csv")

# App title
st.title("Smart Recipe Recommender")
st.write("Enter the ingredients you have at home, separated by commas.")

# User input
user_input = st.text_input("Example: rice, tomato, onion")

if user_input:
    user_ingredients = [item.strip().lower() for item in user_input.split(",") if item.strip()]

    matched_recipes = []

    for _, row in df.iterrows():
        recipe_ingredients = [item.strip().lower() for item in row["ingredients"].split(",")]

        matched_count = len(set(user_ingredients) & set(recipe_ingredients))
        total_recipe_ingredients = len(recipe_ingredients)
        match_percentage = round((matched_count / total_recipe_ingredients) * 100, 2)

        missing_ingredients = list(set(recipe_ingredients) - set(user_ingredients))
        available_ingredients = list(set(recipe_ingredients) & set(user_ingredients))

        matched_recipes.append({
            "Recipe Name": row["recipe_name"],
            "Cuisine": row["cuisine"],
            "Cook Time": row["cook_time"],
            "Difficulty": row["difficulty"],
            "Calories": row["calories"],
            "Match %": match_percentage,
            "Available Ingredients": ", ".join(sorted(available_ingredients)),
            "Missing Ingredients": ", ".join(sorted(missing_ingredients))
        })

    results_df = pd.DataFrame(matched_recipes)
    results_df = results_df.sort_values(by="Match %", ascending=False)

    exact_matches = results_df[results_df["Match %"] == 100]
    partial_matches = results_df[(results_df["Match %"] < 100) & (results_df["Match %"] >= 40)]

    if not exact_matches.empty:
        st.subheader("Recipes You Can Make Right Now")
        st.dataframe(exact_matches, use_container_width=True)

    if not partial_matches.empty:
        st.subheader("Recipes You Can Almost Make")
        st.dataframe(partial_matches, use_container_width=True)

    if exact_matches.empty and partial_matches.empty:
        st.warning("No good matches found. Try entering more ingredients.")