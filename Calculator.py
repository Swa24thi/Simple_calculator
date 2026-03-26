from selectors import SelectSelector

import streamlit as st

st.title("🔢🧮 Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Select a function:",["Add","Subtract","Multiply","Divide","Percentage"])
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2  if num2 != 0 else "Can't divide by zero"
    elif operation == "Percentage":
        result = num1 % num2 if num2 != 0 else "Can't divide by zero"
    st.success(f"Result: {result}")