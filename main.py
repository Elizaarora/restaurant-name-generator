# main.py
import streamlit as st
import restaurant_helper

st.title("🍽️ Restaurant Name & Menu Generator")

cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ("Indian", "Italian", "Mexican", "Arabic", "American", "Japanese")
)

if cuisine:
    response = restaurant_helper.generate_restaurant_name_and_items(cuisine)

    st.header(f"🏷️ {response['restaurant_name'].strip()}")
    st.subheader("📋 Menu Items:")

    menu_items = response["menu_items"].strip().split(",")
    for item in menu_items:
        st.write("•", item.strip())
