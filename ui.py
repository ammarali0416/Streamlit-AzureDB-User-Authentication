import streamlit as st

# Create a dictionary to store user information (username and password)
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# Define a function for user signup
def signup():
    st.subheader("Sign Up")
    new_username = st.text_input("Create a new username")
    new_password = st.text_input("Create a password", type="password")
    if st.button("Sign Up"):
        if new_username and new_password:
            st.session_state.user_data[new_username] = new_password
            st.success("You have successfully signed up!")
        else:
            st.warning("Please enter both a username and a password.")

# Define a function for user login
def login():
    st.subheader("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        if username in st.session_state.user_data and st.session_state.user_data[username] == password:
            st.success(f"Welcome, {username}!")
        else:
            st.error("Incorrect username or password. Please try again.")

# Main application
st.title("Study Buddy")

# Create a dropdown to select action (Sign Up or Log In)
selected_action = st.selectbox("Select an action:", ["Sign Up", "Log In"])

if selected_action == "Sign Up":
    signup()
elif selected_action == "Log In":
    login()