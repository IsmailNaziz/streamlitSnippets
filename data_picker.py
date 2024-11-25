import streamlit as st
from datetime import date

def date_range_picker():
    # Initialize state
    if "start_date" not in st.session_state:
        st.session_state.start_date = date.today()
    if "end_date" not in st.session_state:
        st.session_state.end_date = date.today()

    # Start date picker
    start_date = st.date_input(
        "Select start date",
        value=st.session_state.start_date,
        key="start_date_picker"
    )

    # End date picker
    end_date = st.date_input(
        "Select end date",
        value=st.session_state.end_date,
        key="end_date_picker"
    )

    # Update session state
    if start_date != st.session_state.start_date:
        st.session_state.start_date = start_date
    if end_date != st.session_state.end_date:
        st.session_state.end_date = end_date

    # Return selected dates
    return st.session_state.start_date, st.session_state.end_date
date_range_picker()