import streamlit as st

# Define your multiline text
non_copiable_text = """
This is an example of non-copiable text.
It supports:

- Multiple lines
- Special characters: @, #, $, %, &, *
- Indentations and formatting.

This is a new paragraph with proper line spacing.
"""

# HTML and CSS for non-copiable text
non_copiable_html = f"""
<style>
    .non-copiable {{
        user-select: none; 
        -webkit-user-select: none; 
        -moz-user-select: none; 
        -ms-user-select: none; 
        white-space: pre-wrap; 
        word-wrap: break-word; 
        font-family: inherit; /* Matches Streamlit's default font */
        font-size: inherit; /* Matches Streamlit's font size */
        line-height: inherit; /* Matches Streamlit's default line spacing */
        padding: 0; 
        margin: 0; 
        color: inherit; /* Matches Streamlit's text color */
    }}
</style>
<div class="non-copiable">
{non_copiable_text}
</div>
"""

# Display the text in Streamlit
st.markdown(non_copiable_html, unsafe_allow_html=True)
