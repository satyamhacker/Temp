import streamlit as st
import requests
import re

# Set the title of the app
st.title("Login Form")


# Create a form with email and password fields
with st.form(key='login_form'):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button(label="Login")

# Handle form submission
if submit_button:
    if not email or not password:
        st.error("Please enter both email and password.")
    elif '@' not in email:
        st.error("Please enter a valid email address with '@'.")
   
            
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
                    st.info(f"your jwt token is ====>"+str(response.json()))
                    print("Login response",response.json())
                else:
                    print(f"Error: {response.status_code}")
                    st.error(f"Error: Incorrect Email or Password")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
