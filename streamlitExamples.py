import streamlit as st

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.rawpixel.com/image_600/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm0yMThiYXRjaDUta2F0aWUtMTIuanBn.jpg");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to add ingredient to cache
@st.cache(allow_output_mutation=True)
def add_ingredient(ingredient, ingredients):
    ingredients.append(ingredient)
    return ingredients

# Function to get ingredients from cache
@st.cache(allow_output_mutation=True)
def get_ingredients(ingredients):
    return ingredients

def recipe_upload():
    st.title("The Kitchen - Recipe Upload")
    st.write("Upload your recipe details below:")

    # Input fields for recipe details
    recipe_name = st.text_input("Recipe Name")
    ingredients = st.text_area("Ingredients (one ingredient per line)")
    recipe_instructions = st.text_area("Recipe Instructions")

    # File uploader for recipe photo
    st.write("Upload a photo of the recipe:")
    uploaded_photo = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

    # Submit button
    if st.button("Upload Recipe"):
        # Validate and process the form data
        if recipe_name and ingredients and recipe_instructions and uploaded_photo:
            st.success("Recipe uploaded successfully!")
            # You can add code here to save the recipe details and uploaded photo to a database or perform other actions
        else:
            st.error("Please fill out all fields.")

def user_profile():
    st.title("The Kitchen - User Profile")
    st.write("Please fill out your profile details below:")

    # Input fields for user profile
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")
    
    # Profile picture upload
    st.write("Upload your profile picture:")
    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

    # Submit button
    if st.button("Submit"):
        # Validate and process the form data
        if username and password and name and email and phone_number:
            st.success("Profile updated successfully!")
            # You can add code here to save the profile details and uploaded picture to a database or perform other actions
        else:
            st.error("Please fill out all fields.")

def login():
    st.title("The Kitchen - Login")
    st.write("Please log in with your username and password:")

    # Input fields for login
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Submit button
    if st.button("Login"):
        # Validate username and password
        if username == "example_user" and password == "example_password":
            st.success("Login successful!")
            # You can add code here to redirect to the user profile page or perform other actions after successful login
        else:
            st.error("Invalid username or password.")

def saved_recipes():
    st.title("The Kitchen - Saved Recipes")
    # Search bar for saved recipes
    search_query = st.text_input("Search for Saved Recipes", "")
    st.write("You searched for saved recipes:", search_query)
    # Add saved recipes list or grid here

def search_recipes():
    st.title("The Kitchen - Search Recipes")
    st.write("Type in and add your ingredients to search for recipes:")

    # Get current list of ingredients from cache
    ingredients = get_ingredients([])

    # Input field to type in ingredients
    ingredient = st.text_input("Add Ingredient")

    # Button to add ingredient
    if st.button("Add"):
        if ingredient:
            ingredients = add_ingredient(ingredient, ingredients.copy())
            st.write("Added ingredient:", ingredient)
        else:
            st.warning("Please enter an ingredient.")

    # Input field to add food preferences
    preferences = st.text_input("Add Food Preferences")

    # Button to search for recipes
    if st.button("Search"):
        # Generate and display recipe based on the added ingredients and preferences
        if ingredients:
            st.success("Generating recipe based on ingredients:")
            st.write("Ingredients:", ingredients)  # Placeholder for actual recipe generation
            if preferences:
                st.write("Food Preferences:", preferences)  # Placeholder for food preferences
        else:
            st.warning("Please add ingredients before searching for recipes.")

def homepage():
    st.title("The Kitchen - Home")
    st.write("Welcome to The Kitchen. Please log in or explore our recipes.")

def main():
    st.sidebar.title("Navigation")
    menu = ["Home", "Login", "User Profile", "Saved Recipes", "Search Recipes", "Recipe Upload"]
    choice = st.sidebar.selectbox("Go to", menu)
    
    if choice == "Home":
        homepage()
    elif choice == "Login":
        login()
    elif choice == "User Profile":
        user_profile()
    elif choice == "Saved Recipes":
        saved_recipes()
    elif choice == "Search Recipes":
        search_recipes()
    elif choice == "Recipe Upload":
        recipe_upload()

if __name__ == "__main__":
    main()
