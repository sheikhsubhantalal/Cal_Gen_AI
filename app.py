import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Instructions
st.write("This is a basic calculator app. Select an operation and input two numbers.")

# Taking user input for numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Dropdown for operation selection
operation = st.selectbox("Choose operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculation based on the selected operation
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"

# Display the result
st.write(f"The result of {operation.lower()} is: {result}")
