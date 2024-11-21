import json

import streamlit as st

txt = 'Text with "double quotes" and \'single quotes\' in expander 1.',
non_selectable_text = f"""
<div style="user-select: none; -webkit-user-select: none; -ms-user-select: none;">
    {json.dumps(txt)}
</div>
"""

st.markdown(non_selectable_text, unsafe_allow_html=True)
