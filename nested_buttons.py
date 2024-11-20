import streamlit as st

def main():
    # Title for the Streamlit App
    st.title("Text Reversing App with Feedback")

    # Text input box
    user_input = st.text_input("Enter some text:")

    # Session state to store reversed text and feedback state
    if 'reversed_text' not in st.session_state:
        st.session_state.reversed_text = None
    if 'feedback_given' not in st.session_state:
        st.session_state.feedback_given = False
    if 'feedback' not in st.session_state:
        st.session_state.feedback = None

    # Reverse Button
    if st.button("Reverse Text"):
        st.session_state.reversed_text = user_input[::-1]
        st.session_state.feedback_given = False
        st.session_state.feedback = None

    # Display reversed text if available
    if st.session_state.reversed_text:
        st.write("Reversed Text:", st.session_state.reversed_text)

        # Feedback Buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍 Thumbs Up"):
                st.session_state.feedback_given = True
                st.session_state.feedback = "Thumbs Up"
        with col2:
            if st.button("👎 Thumbs Down"):
                st.session_state.feedback_given = True
                st.session_state.feedback = "Thumbs Down"

        # Display feedback if given
        if st.session_state.feedback_given and st.session_state.feedback:
            st.write(f"You selected: {st.session_state.feedback}")

if __name__ == "__main__":
    main()
