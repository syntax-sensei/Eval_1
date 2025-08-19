import streamlit as st

def login_page():
    st.title("Login to Your App")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if check_login(username, password):  
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

def check_login(username, password):
    
    return username == "admin" and password == "password"

if __name__ == "__main__":
    login_page()