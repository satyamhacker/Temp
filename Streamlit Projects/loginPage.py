import streamlit as st
import requests
import re

# Set the title of the app
st.title("Login Form")

# Function to check if password is strong
def is_strong_password(password):
    # if len(password) < 8:
    #     return False, "Password must be at least 8 characters long."
    # if not re.search(r"[A-Z]", password):
    #     return False, "Password must contain at least one uppercase letter."
    # if not re.search(r"[a-z]", password):
    #     return False, "Password must contain at least one lowercase letter."
    # if not re.search(r"\d", password):
    #     return False, "Password must contain at least one digit."
    # if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    #     return False, "Password must contain at least one special character."
     return True, ""

# Create a form with email and password fields
with st.form(key='login_form'):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button(label="Signup")

# Handle form submission
if submit_button:
    if not email or not password:
        st.error("Please enter both email and password.")
    elif '@' not in email:
        st.error("Please enter a valid email address with '@'.")
    else:
        is_valid_password, message = is_strong_password(password)
        if not is_valid_password:
             st.error(message)
            
        else:
            # Prepare the payload
            payload = {
                'email': email,
                'password': password
            }
            
            # Send POST request to the Express server
            try:
                response = requests.post("http://localhost:3000/login", json=payload)
                if response.status_code == 201:
                    st.success(f"You are Login Successfully");
                    print(response)
                else:
                    st.error(f"Error: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
