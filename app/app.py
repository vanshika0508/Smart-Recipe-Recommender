import streamlit as st
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="Smart Recipe Recommender",
    page_icon="🍲",
    layout="wide"
)

# -------------------------------
# Load dataset
# -------------------------------
df = pd.read_csv("data/recipes.csv")

# -------------------------------
# Title and intro
# -------------------------------
st.title("🍲 Smart Recipe Recommender")
st.write("Find recipes you can make using ingredients already available at home.")

with st.expander("About this project"):
    st.write(
        """
        This app recommends recipes based on ingredients entered by the user.
        It also includes simple data analytics features such as:
        - ingredient frequency analysis
        - recipe distribution by cuisine
        - recipe distribution by difficulty
        - exact and partial ingredient matching
        """
    )

# -------------------------------
# Sidebar filters
# -------------------------------
st.sidebar.header("Filter Recipes")

selected_cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    ["All"] + sorted(df["cuisine"].unique().tolist())
)

selected_difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["All"] + sorted(df["difficulty"].unique().tolist())
)

# Apply filters
filtered_df = df.copy()

if selected_cuisine != "All":
    filtered_df = filtered_df[filtered_df["cuisine"] == selected_cuisine]

if selected_difficulty != "All":
    filtered_df = filtered_df[filtered_df["difficulty"] == selected_difficulty]

# -------------------------------
# User input
# -------------------------------
user_input = st.text_input(
    "Enter ingredients separated by commas",
    placeholder="Example: rice, tomato, onion, oil, salt"
)

if user_input:
    user_ingredients = [item.strip().lower() for item in user_input.split(",") if item.strip()]
    matched_recipes = []

    for _, row in filtered_df.iterrows():
        recipe_ingredients = [item.strip().lower() for item in row["ingredients"].split(",")]

        matched_count = len(set(user_ingredients) & set(recipe_ingredients))
        total_recipe_ingredients = len(recipe_ingredients)
        match_percentage = round((matched_count / total_recipe_ingredients) * 100, 2)

        missing_ingredients = list(set(recipe_ingredients) - set(user_ingredients))
        available_ingredients = list(set(recipe_ingredients) & set(user_ingredients))

        matched_recipes.append({
            "Recipe Name": row["recipe_name"],
            "Cuisine": row["cuisine"],
            "Cook Time (mins)": row["cook_time"],
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

    # -------------------------------
    # Metrics row
    # -------------------------------
    st.subheader("Match Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Recipes Checked", len(results_df))
    col2.metric("Exact Matches", len(exact_matches))
    col3.metric("Partial Matches", len(partial_matches))
    col4.metric("Ingredients Entered", len(user_ingredients))

    # -------------------------------
    # Top recipe highlight
    # -------------------------------
    if not results_df.empty:
        top_recipe = results_df.iloc[0]
        st.subheader("Top Recommended Recipe")
        st.success(
            f"{top_recipe['Recipe Name']} | Match: {top_recipe['Match %']}% | "
            f"Cuisine: {top_recipe['Cuisine']} | Difficulty: {top_recipe['Difficulty']} | "
            f"Cook Time: {top_recipe['Cook Time (mins)']} mins"
        )

    # -------------------------------
    # Exact and partial results
    # -------------------------------
    if not exact_matches.empty:
        st.subheader("Recipes You Can Make Right Now")
        st.dataframe(exact_matches, use_container_width=True)

    if not partial_matches.empty:
        st.subheader("Recipes You Can Almost Make")
        st.dataframe(partial_matches, use_container_width=True)

    if exact_matches.empty and partial_matches.empty:
        st.warning("No good matches found. Try entering more ingredients or changing the filters.")

# -------------------------------
# Analytics section
# -------------------------------
st.subheader("Recipe Dataset Insights")

# Build ingredient counts
all_ingredients = []
for ingredients in df["ingredients"]:
    all_ingredients.extend([item.strip().lower() for item in ingredients.split(",")])

ingredient_counts = Counter(all_ingredients)
top_ingredients = pd.DataFrame(ingredient_counts.items(), columns=["Ingredient", "Count"])
top_ingredients = top_ingredients.sort_values(by="Count", ascending=False).head(10)

# Cuisine and difficulty counts
cuisine_counts = df["cuisine"].value_counts()
difficulty_counts = df["difficulty"].value_counts()

# Show charts in columns
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    ax1.bar(top_ingredients["Ingredient"], top_ingredients["Count"])
    ax1.set_title("Top 10 Most Common Ingredients")
    ax1.set_xlabel("Ingredient")
    ax1.set_ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig1)

with chart_col2:
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    ax2.bar(cuisine_counts.index, cuisine_counts.values)
    ax2.set_title("Recipes by Cuisine")
    ax2.set_xlabel("Cuisine")
    ax2.set_ylabel("Number of Recipes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig2)

# Third chart full width
fig3, ax3 = plt.subplots(figsize=(7, 4))
ax3.bar(difficulty_counts.index, difficulty_counts.values)
ax3.set_title("Recipes by Difficulty")
ax3.set_xlabel("Difficulty")
ax3.set_ylabel("Count")
plt.tight_layout()
st.pyplot(fig3)

# -------------------------------
# Footer note
# -------------------------------
st.markdown("---")
st.caption("Built with Python, Pandas, Streamlit, and Matplotlib.")