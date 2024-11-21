import streamlit as st

# Define your multiline text
non_copiable_text = """
This is an example of non-copiable text.
It supports:

- Multiple lines
- Special characters: @, #, $, %, &, *
- Indentations and formatting.
"""

# HTML and CSS for non-copiable text
non_copiable_html = f"""
<div style="
    user-select: none; 
    -webkit-user-select: none; 
    -moz-user-select: none; 
    -ms-user-select: none; 
    white-space: pre-wrap; 
    word-wrap: break-word; 
    font-family: Arial, sans-serif; 
    font-size: 16px; 
    line-height: 1.5; 
    padding: 10px; 
    border: 1px solid #ddd; 
    border-radius: 5px; 
    background-color: #f9f9f9; 
    color: #333; 
">
{non_copiable_text}
</div>
"""

# Display the text in Streamlit
st.markdown(non_copiable_html, unsafe_allow_html=True)
