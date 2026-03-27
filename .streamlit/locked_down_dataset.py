
import streamlit as st

# 1. AUTHENTICATION LAYER (The Gatekeeper)
# This part handles the login. You'd use a library or SSO here.
# For this example, let's assume 'user_email' comes from your Auth provider.
user_email = get_logged_in_user_email() 

# 2. THE RESTRICTION CHECK
allowed_users = ["zss@trustpilot.com", "analyst@company.com"]

if user_email not in allowed_users:
    st.error("🚫 Access Denied: Your email is not on the authorized list.")
    st.stop() # Execution stops here for unauthorized users

# 3. THE PROTECTED CONTENT
# Everything below this line is only visible to the people in your list.
st.title("Internal Financial Dashboard")
st.write("Welcome back!", user_email)
# load_sensitive_data() ...
