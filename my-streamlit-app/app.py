import streamlit as st

# Title of your app
st.title("My First Streamlit App! 🚀")

# Add a header
st.header("Welcome!")

# Add some text
st.write("This is my first web app. Pretty cool, right?")

# Add a text input
name = st.text_input("What's your name?")

# Display personalized message
if name:
    st.write(f"Hello, {name}! Nice to meet you! 👋")

# Add a slider
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You are {age} years old")

# Add a button
if st.button("Click me!"):
    st.balloons()
    st.success("You clicked the button! 🎉")