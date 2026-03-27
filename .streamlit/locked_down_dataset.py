import streamlit as st

# This gets the email of the person currently viewing the app
# Note: This only works on Streamlit Cloud for Private apps
user_email = st.user.email 

allowed_users = ["zss@trustpilot.com", "analyst@company.com"]

if user_email not in allowed_users:
    st.error(f"🚫 Access Denied. {user_email} is not authorized.")
    st.stop()

st.success("Welcome! You have access to the restricted data.")
# Your sensitive data code goes here...
