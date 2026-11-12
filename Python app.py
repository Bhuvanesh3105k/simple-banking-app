%%writefile app.py

import streamlit as st


# Initialize balance in session state if it doesn't exist
if 'balance' not in st.session_state:
    st.session_state.balance = 0

class D:
    def add_amount(self, user):
        if user > 0:
            st.session_state.balance += user
            st.success(f"${user} successfully credited to your account")

    def check_balance(self):
        st.info(f"Current Balance: ${st.session_state.balance}")

    def send_amount(self, user):
        if user <= 0:
            st.warning("Please enter a positive amount")
        elif user > st.session_state.balance:
            st.error("Insufficient funds")
        else:
            st.session_state.balance -= user
            st.success(f"${user} transaction successfully completed")

# Create an instance of the D class
amount = D()

# Streamlit App Layout
st.title("Simple Banking App")

# Select option from sidebar
choice = st.sidebar.selectbox(
    "Select an option",
    ["Add Amount", "Check Balance", "Send Amount"]
)

# Add Amount Option
if choice == "Add Amount":
    st.subheader("Add Money to Your Account")
    user_input = st.number_input("Enter the amount to add", min_value=0)
    if st.button("Add Amount"):
        amount.add_amount(user_input)

# Check Balance Option
elif choice == "Check Balance":
    st.subheader("Check Your Balance")
    if st.button("Check Balance"):
        amount.check_balance()

# Send Amount Option
elif choice == "Send Amount":
    st.subheader("Send Money from Your Account")
    user_input = st.number_input("Enter the amount to send", min_value=0)
    if st.button("Send Amount"):
        amount.send_amount(user_input)
