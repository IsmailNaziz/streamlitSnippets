import streamlit as st

# Function to handle the change event
def on_text_change():
    # Access the updated value from session_state
    new_value = st.session_state.text_input
    # Perform any operation with the updated value
    st.write(f"The new value is: {new_value}")

# Ensure session state is initialized
if "text_value" not in st.session_state:
    st.session_state["text_value"] = ""

# Streamlit text input with state and on_change handler
st.text_input(
    "Enter text:",
    key="text_input",  # Automatically binds to session_state["text_input"]
    on_change=on_text_change  # Triggered when the text changes
)

# Display the current value of the text_input for confirmation
st.write("Current state value:", st.session_state.text_input)
