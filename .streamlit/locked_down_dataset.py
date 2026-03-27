import streamlit as st

# This will now work because of the settings in your screenshot
if st.user.email == "zss@trustpilot.com":
    st.write("Hello, Admin! Loading the restricted dataset now...")
    # show_private_data()
else:
    st.write(f"Hello {st.user.email}, you have viewer access.")
    # show_limited_data()
