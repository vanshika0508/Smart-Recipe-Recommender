import streamlit as st
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Smart Recipe Recommender",
    page_icon="🍲",
    layout="wide"
)

# Load dataset
df = pd.read_csv("data/recipes.csv")

# Full recipe details
recipe_details = {
    "Tomato Rice": {
        "ingredients": ["rice", "tomato", "onion", "oil", "salt"],
        "steps": [
            "Cook the rice and keep it aside.",
            "Heat oil in a pan and add chopped onion.",
            "Add chopped tomato and cook until soft.",
            "Add salt and mix well.",
            "Add cooked rice and mix everything together.",
            "Cook for 2 to 3 minutes and serve hot."
        ]
    },
    "Veg Fried Rice": {
        "ingredients": ["rice", "carrot", "beans", "onion", "soy sauce", "oil", "salt"],
        "steps": [
            "Cook the rice and let it cool.",
            "Heat oil in a pan and sauté onion.",
            "Add carrot and beans and cook for a few minutes.",
            "Add soy sauce and salt.",
            "Add cooked rice and mix well.",
            "Cook for 2 to 3 minutes and serve."
        ]
    },
    "Aloo Tikki": {
        "ingredients": ["potato", "onion", "salt", "oil", "spices"],
        "steps": [
            "Boil and mash the potatoes.",
            "Add chopped onion, salt, and spices.",
            "Mix everything well and shape into small patties.",
            "Heat oil on a pan.",
            "Cook both sides until golden brown.",
            "Serve hot."
        ]
    },
    "Cheese Sandwich": {
        "ingredients": ["bread", "cheese", "butter"],
        "steps": [
            "Spread butter on the bread slices.",
            "Place cheese between two slices.",
            "Toast on a pan or sandwich maker until golden.",
            "Serve warm."
        ]
    },
    "Omelette": {
        "ingredients": ["egg", "onion", "salt", "oil"],
        "steps": [
            "Beat the eggs in a bowl.",
            "Add chopped onion and salt.",
            "Heat oil in a pan.",
            "Pour the egg mixture into the pan.",
            "Cook both sides until done.",
            "Serve hot."
        ]
    },
    "Pasta Arrabiata": {
        "ingredients": ["pasta", "tomato", "garlic", "oil", "salt", "chili flakes"],
        "steps": [
            "Boil the pasta and keep aside.",
            "Heat oil in a pan and sauté garlic.",
            "Add chopped tomato and cook into a sauce.",
            "Add salt and chili flakes.",
            "Add boiled pasta and mix well.",
            "Cook for 2 minutes and serve."
        ]
    },
    "Masala Maggi": {
        "ingredients": ["noodles", "onion", "tomato", "oil", "salt", "spices"],
        "steps": [
            "Heat oil in a pan and sauté onion.",
            "Add tomato and cook until soft.",
            "Add spices and a little salt.",
            "Add water and bring it to a boil.",
            "Add noodles and cook until done.",
            "Serve hot."
        ]
    },
    "Paneer Bhurji": {
        "ingredients": ["paneer", "onion", "tomato", "oil", "salt", "spices"],
        "steps": [
            "Heat oil in a pan.",
            "Add onion and cook until soft.",
            "Add tomato and spices and cook well.",
            "Crumble paneer and add it to the pan.",
            "Mix well and cook for 3 to 4 minutes.",
            "Serve hot."
        ]
    },
    "Potato Cheese Bowl": {
        "ingredients": ["potato", "cheese", "butter", "salt", "pepper"],
        "steps": [
            "Boil or cook the potato until soft.",
            "Mash it with butter.",
            "Add salt and pepper.",
            "Top with cheese.",
            "Serve warm."
        ]
    },
    "Garlic Rice": {
        "ingredients": ["rice", "garlic", "oil", "salt"],
        "steps": [
            "Cook the rice and keep aside.",
            "Heat oil in a pan and sauté garlic.",
            "Add salt and cooked rice.",
            "Mix well and cook for 2 minutes.",
            "Serve hot."
        ]
    },
    "Jeera Rice": {
        "ingredients": ["rice", "cumin", "oil", "salt"],
        "steps": [
            "Cook the rice and keep aside.",
            "Heat oil and add cumin.",
            "Add cooked rice and salt.",
            "Mix well and cook for 2 minutes.",
            "Serve hot."
        ]
    },
    "Poha": {
        "ingredients": ["poha", "onion", "oil", "salt", "peas", "turmeric"],
        "steps": [
            "Wash poha lightly and keep aside.",
            "Heat oil and cook onion.",
            "Add peas, turmeric, and salt.",
            "Add poha and mix gently.",
            "Cook for 2 to 3 minutes and serve."
        ]
    },
    "Upma": {
        "ingredients": ["semolina", "onion", "oil", "salt", "mustard seeds", "curry leaves"],
        "steps": [
            "Roast semolina and keep aside.",
            "Heat oil and add mustard seeds and curry leaves.",
            "Add onion and cook.",
            "Add water and salt, then bring to a boil.",
            "Slowly add semolina while stirring.",
            "Cook until thick and serve."
        ]
    },
    "Chana Salad": {
        "ingredients": ["chickpeas", "onion", "tomato", "salt", "lemon"],
        "steps": [
            "Take boiled chickpeas in a bowl.",
            "Add chopped onion and tomato.",
            "Add salt and lemon juice.",
            "Mix well and serve."
        ]
    },
    "Egg Bhurji": {
        "ingredients": ["egg", "onion", "tomato", "oil", "salt", "spices"],
        "steps": [
            "Heat oil in a pan.",
            "Add onion and tomato and cook well.",
            "Add spices and salt.",
            "Add beaten eggs and scramble.",
            "Cook until done and serve hot."
        ]
    },
    "Grilled Cheese": {
        "ingredients": ["bread", "cheese", "butter"],
        "steps": [
            "Butter the bread slices.",
            "Place cheese between the slices.",
            "Grill until crisp and golden.",
            "Serve hot."
        ]
    },
    "French Toast": {
        "ingredients": ["bread", "egg", "milk", "butter"],
        "steps": [
            "Beat egg and milk together.",
            "Dip bread slices in the mixture.",
            "Cook on a buttered pan until golden on both sides.",
            "Serve warm."
        ]
    },
    "Mashed Potato": {
        "ingredients": ["potato", "butter", "salt", "pepper"],
        "steps": [
            "Boil potatoes until soft.",
            "Mash with butter.",
            "Add salt and pepper.",
            "Mix well and serve."
        ]
    },
    "Veg Sandwich": {
        "ingredients": ["bread", "tomato", "onion", "butter", "cucumber"],
        "steps": [
            "Spread butter on bread.",
            "Add sliced tomato, onion, and cucumber.",
            "Close the sandwich and serve."
        ]
    },
    "Mac and Cheese": {
        "ingredients": ["pasta", "cheese", "butter", "milk", "salt"],
        "steps": [
            "Boil pasta and keep aside.",
            "Heat butter and add milk.",
            "Add cheese and salt.",
            "Mix until creamy.",
            "Add pasta and stir well.",
            "Serve hot."
        ]
    },
    "White Sauce Pasta": {
        "ingredients": ["pasta", "milk", "butter", "flour", "salt", "pepper"],
        "steps": [
            "Boil pasta and keep aside.",
            "Heat butter and add flour.",
            "Slowly add milk and stir.",
            "Add salt and pepper.",
            "Add pasta and mix well.",
            "Serve warm."
        ]
    },
    "Aglio e Olio": {
        "ingredients": ["pasta", "garlic", "oil", "salt", "chili flakes"],
        "steps": [
            "Boil pasta and keep aside.",
            "Heat oil and sauté garlic.",
            "Add chili flakes and salt.",
            "Add pasta and toss well.",
            "Serve hot."
        ]
    },
    "Bruschetta": {
        "ingredients": ["bread", "tomato", "garlic", "oil", "salt"],
        "steps": [
            "Toast the bread slices.",
            "Mix chopped tomato, garlic, oil, and salt.",
            "Top the bread with the mixture.",
            "Serve immediately."
        ]
    },
    "Margherita Toast": {
        "ingredients": ["bread", "cheese", "tomato", "oregano", "butter"],
        "steps": [
            "Butter the bread.",
            "Add tomato and cheese on top.",
            "Sprinkle oregano.",
            "Toast until cheese melts.",
            "Serve hot."
        ]
    },
    "Rice Bowl": {
        "ingredients": ["rice", "carrot", "beans", "salt", "oil"],
        "steps": [
            "Cook rice and keep aside.",
            "Cook carrot and beans in oil.",
            "Add salt.",
            "Mix vegetables with rice.",
            "Serve hot."
        ]
    },
    "Noodles Stir Fry": {
        "ingredients": ["noodles", "carrot", "beans", "onion", "soy sauce", "oil", "salt"],
        "steps": [
            "Boil noodles and keep aside.",
            "Heat oil and sauté onion.",
            "Add carrot and beans.",
            "Add soy sauce and salt.",
            "Add noodles and toss well.",
            "Serve hot."
        ]
    },
    "Garlic Noodles": {
        "ingredients": ["noodles", "garlic", "oil", "salt", "soy sauce"],
        "steps": [
            "Boil noodles and keep aside.",
            "Heat oil and sauté garlic.",
            "Add soy sauce and salt.",
            "Add noodles and mix well.",
            "Serve hot."
        ]
    },
    "Egg Fried Rice": {
        "ingredients": ["rice", "egg", "onion", "soy sauce", "oil", "salt"],
        "steps": [
            "Cook rice and keep aside.",
            "Scramble egg in oil and keep aside.",
            "Cook onion in the same pan.",
            "Add soy sauce, salt, rice, and egg.",
            "Mix well and serve."
        ]
    },
    "Vegetable Soup": {
        "ingredients": ["carrot", "beans", "tomato", "salt", "pepper", "garlic"],
        "steps": [
            "Add chopped vegetables to a pot.",
            "Add water, salt, pepper, and garlic.",
            "Cook until vegetables are soft.",
            "Serve hot."
        ]
    },
    "Tomato Soup": {
        "ingredients": ["tomato", "garlic", "butter", "salt", "pepper"],
        "steps": [
            "Cook tomato and garlic until soft.",
            "Blend into a smooth mixture.",
            "Heat with butter, salt, and pepper.",
            "Serve warm."
        ]
    },
    "Cheese Omelette": {
        "ingredients": ["egg", "cheese", "butter", "salt", "pepper"],
        "steps": [
            "Beat eggs with salt and pepper.",
            "Heat butter in a pan.",
            "Pour eggs into the pan.",
            "Add cheese on top.",
            "Fold and cook until done.",
            "Serve hot."
        ]
    },
    "Boiled Egg Salad": {
        "ingredients": ["egg", "onion", "tomato", "salt", "pepper"],
        "steps": [
            "Boil the eggs and chop them.",
            "Add chopped onion and tomato.",
            "Season with salt and pepper.",
            "Mix well and serve."
        ]
    },
    "Paneer Sandwich": {
        "ingredients": ["bread", "paneer", "butter", "onion", "tomato"],
        "steps": [
            "Spread butter on bread slices.",
            "Add paneer, onion, and tomato.",
            "Close the sandwich and toast if desired.",
            "Serve warm."
        ]
    },
    "Aloo Paratha": {
        "ingredients": ["potato", "flour", "oil", "salt", "spices"],
        "steps": [
            "Make dough with flour and water.",
            "Boil and mash potato with salt and spices.",
            "Stuff potato mixture into the dough.",
            "Roll it gently.",
            "Cook on a pan with oil until golden.",
            "Serve hot."
        ]
    },
    "Curd Rice": {
        "ingredients": ["rice", "curd", "salt", "mustard seeds", "curry leaves"],
        "steps": [
            "Cook rice and let it cool.",
            "Mix rice with curd and salt.",
            "Prepare tempering with mustard seeds and curry leaves.",
            "Add tempering to rice.",
            "Serve."
        ]
    },
    "Lemon Rice": {
        "ingredients": ["rice", "lemon", "oil", "salt", "mustard seeds", "curry leaves"],
        "steps": [
            "Cook rice and keep aside.",
            "Heat oil and add mustard seeds and curry leaves.",
            "Add salt and lemon juice.",
            "Mix with rice and serve."
        ]
    },
    "Fried Potato": {
        "ingredients": ["potato", "oil", "salt", "pepper"],
        "steps": [
            "Cut potato into small pieces.",
            "Heat oil in a pan.",
            "Cook potato until crisp.",
            "Add salt and pepper.",
            "Serve hot."
        ]
    },
    "Paneer Rice Bowl": {
        "ingredients": ["rice", "paneer", "onion", "tomato", "salt", "oil"],
        "steps": [
            "Cook rice and keep aside.",
            "Heat oil and cook onion and tomato.",
            "Add paneer and salt.",
            "Mix in the rice.",
            "Cook for 2 minutes and serve."
        ]
    },
    "Cheesy Pasta": {
        "ingredients": ["pasta", "cheese", "milk", "butter", "salt"],
        "steps": [
            "Boil pasta and keep aside.",
            "Heat butter and milk.",
            "Add cheese and salt.",
            "Mix until smooth.",
            "Add pasta and stir well.",
            "Serve warm."
        ]
    },
    "Simple Salad": {
        "ingredients": ["tomato", "onion", "cucumber", "salt", "lemon"],
        "steps": [
            "Chop all vegetables.",
            "Add salt and lemon juice.",
            "Mix well and serve fresh."
        ]
    }
}

# Title and intro
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

# Sidebar filters
st.sidebar.header("Filter Recipes")

selected_cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    ["All"] + sorted(df["cuisine"].unique().tolist())
)

selected_difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["All"] + sorted(df["difficulty"].unique().tolist())
)

filtered_df = df.copy()

if selected_cuisine != "All":
    filtered_df = filtered_df[filtered_df["cuisine"] == selected_cuisine]

if selected_difficulty != "All":
    filtered_df = filtered_df[filtered_df["difficulty"] == selected_difficulty]

# User input
user_input = st.text_input(
    "Enter ingredients separated by commas",
    placeholder="Example: rice, tomato, onion, oil, salt"
)

selected_recipe_name = None

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
    results_df = results_df.sort_values(by="Match %", ascending=False).reset_index(drop=True)

    exact_matches = results_df[results_df["Match %"] == 100].reset_index(drop=True)
    partial_matches = results_df[(results_df["Match %"] < 100) & (results_df["Match %"] >= 40)].reset_index(drop=True)

    st.subheader("Match Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Recipes Checked", len(results_df))
    col2.metric("Exact Matches", len(exact_matches))
    col3.metric("Partial Matches", len(partial_matches))
    col4.metric("Ingredients Entered", len(user_ingredients))

    if not results_df.empty:
        top_recipe = results_df.iloc[0]
        st.subheader("Top Recommended Recipe")
        st.success(
            f"{top_recipe['Recipe Name']} | Match: {top_recipe['Match %']}% | "
            f"Cuisine: {top_recipe['Cuisine']} | Difficulty: {top_recipe['Difficulty']} | "
            f"Cook Time: {top_recipe['Cook Time (mins)']} mins"
        )

    if not exact_matches.empty:
        st.subheader("Recipes You Can Make Right Now")
        exact_event = st.dataframe(
            exact_matches,
            use_container_width=True,
            hide_index=True,
            on_select="rerun",
            selection_mode="single-row",
            key="exact_table"
        )
        if exact_event.selection.rows:
            selected_recipe_name = exact_matches.iloc[exact_event.selection.rows[0]]["Recipe Name"]

    if not partial_matches.empty:
        st.subheader("Recipes You Can Almost Make")
        partial_event = st.dataframe(
            partial_matches,
            use_container_width=True,
            hide_index=True,
            on_select="rerun",
            selection_mode="single-row",
            key="partial_table"
        )
        if partial_event.selection.rows:
            selected_recipe_name = partial_matches.iloc[partial_event.selection.rows[0]]["Recipe Name"]

    if exact_matches.empty and partial_matches.empty:
        st.warning("No good matches found. Try entering more ingredients or changing the filters.")

# Show selected recipe details
if selected_recipe_name:
    st.subheader(f"Full Recipe: {selected_recipe_name}")
    details = recipe_details.get(selected_recipe_name)

    if details:
        st.markdown("**Ingredients:**")
        for ingredient in details["ingredients"]:
            st.write(f"- {ingredient}")

        st.markdown("**Steps:**")
        for i, step in enumerate(details["steps"], start=1):
            st.write(f"{i}. {step}")
    else:
        st.info("Full recipe steps are not available yet for this item.")

# Analytics section
st.subheader("Recipe Dataset Insights")

all_ingredients = []
for ingredients in df["ingredients"]:
    all_ingredients.extend([item.strip().lower() for item in ingredients.split(",")])

ingredient_counts = Counter(all_ingredients)
top_ingredients = pd.DataFrame(ingredient_counts.items(), columns=["Ingredient", "Count"])
top_ingredients = top_ingredients.sort_values(by="Count", ascending=False).head(10)

cuisine_counts = df["cuisine"].value_counts()
difficulty_counts = df["difficulty"].value_counts()

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

fig3, ax3 = plt.subplots(figsize=(7, 4))
ax3.bar(difficulty_counts.index, difficulty_counts.values)
ax3.set_title("Recipes by Difficulty")
ax3.set_xlabel("Difficulty")
ax3.set_ylabel("Count")
plt.tight_layout()
st.pyplot(fig3)

st.markdown("---")
st.caption("Built with Python, Pandas, Streamlit, and Matplotlib.")