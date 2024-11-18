import streamlit as st
import json  # To safely escape text

# Sample texts for each expander
texts = [
    'Text with "double quotes" and \'single quotes\' in expander 1.',
    'Another "complex" \'example\' in expander 2.',
    'Simple text in expander 3.'
]

# Function to create unique HTML and JavaScript for each button
def copy_to_clipboard_js(text, button_id):
    escaped_text = json.dumps(text)  # Safely escape the text for JavaScript
    return f"""
        <div>
            <button id="{button_id}" 
                    style="background-color: #FF5733; color: white; padding: 10px; border: none; cursor: pointer;">
                Copier
            </button>
            <script>
                document.getElementById("{button_id}").addEventListener("click", function() {{
                    navigator.clipboard.writeText({escaped_text}).then(() => {{
                        const button = document.getElementById("{button_id}");
                        button.style.backgroundColor = '#28A745';
                        button.innerText = 'Copié !';
                        setTimeout(() => {{
                            button.style.backgroundColor = '#FF5733';
                            button.innerText = 'Copier';
                        }}, 2000); // Reset button after 2 seconds
                    }}).catch(err => {{
                        console.error('Could not copy text: ', err);
                    }});
                }}); 
            </script>
        </div>
    """

# Feedback system for each expander
if "feedback" not in st.session_state:
    st.session_state.feedback = {i: None for i in range(len(texts))}

# Display multiple expanders, each with a copy-to-clipboard button and feedback buttons
for i, text in enumerate(texts, start=1):
    expander_label = f"Expander {i}"
    button_id = f"copy_button_{i}"

    with st.expander(expander_label):
        st.write(f"Text to copy: {text}")
        button_html = copy_to_clipboard_js(text, button_id)
        st.components.v1.html(button_html, height=50)

        st.write("Was this answer useful?")
        col1, col2, _, _, _, _ = st.columns(6)
        with col1:
            if st.button("👍", key=f"thumbs_up_{i}"):
                st.session_state.feedback[i - 1] = "Thumbs Up"
                st.success("Thank you for your feedback!")
        with col2:
            if st.button("👎", key=f"thumbs_down_{i}"):
                st.session_state.feedback[i - 1] = "Thumbs Down"
                st.error("Thank you for your feedback!")
