import streamlit as st

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"

st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation buttons with Unicode symbols
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("\u2795"):  # Heavy Plus Sign
        result = calculate(num1, num2, '+')
with col2:
    if st.button("\u2796"):  # Heavy Minus Sign
        result = calculate(num1, num2, '-')
with col3:
    if st.button("\u2716"):  # Multiplication X
        result = calculate(num1, num2, '*')
with col4:
    if st.button("\u2797"):  # Heavy Division Sign
        result = calculate(num1, num2, '/')

# Display result
if 'result' in locals():
    st.success(f"Result: {result}")

# Add a note about the symbols
st.write("Button symbols: ➕ (add), ➖ (subtract), ✖️ (multiply), ➗ (divide)")