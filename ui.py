import streamlit as st

# Define the Streamlit app
def app():
    # Add a title
    st.title('Welcome to my app!')

    # Get the user's name
    name = st.text_input('Enter your name:')

    # Print a greeting message
    st.write('Hello,', name, '!')
