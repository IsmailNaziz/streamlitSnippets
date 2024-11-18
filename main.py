import streamlit as st

# Sample texts for each expander
texts = [
    "Text to copy in expander 1.",
    "Text to copy in expander 2.",
    "Text to copy in expander 3."
]


# Function to create unique HTML and JavaScript for each button
def copy_to_clipboard_js(text, button_id):
    return f"""
        <button id="{button_id}" 
                style="background-color: #FF5733; color: white; padding: 10px; border: none; cursor: pointer;"
                onclick="navigator.clipboard.writeText('{text}').then(() => {{
                    document.getElementById('{button_id}').style.backgroundColor = '#28A745';
                    document.getElementById('{button_id}').innerText = 'copié !';
                }});">
            Copier
        </button>
    """


# Display multiple expanders, each with a copy-to-clipboard button
for i, text in enumerate(texts, start=1):
    expander_label = f"Expander {i}"
    button_id = f"copy_button_{i}"

    with st.expander(expander_label):
        st.write(f"Text to copy: {text}")
        button_html = copy_to_clipboard_js(text, button_id)
        st.components.v1.html(button_html, height=40)