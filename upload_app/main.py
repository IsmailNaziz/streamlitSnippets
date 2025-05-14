# app.py
import streamlit as st
import os
from pathlib import Path

# Dummy credentials (in production, use hashed passwords and secure storage)
USER_CREDENTIALS = {
    "usr": "usr",
}

# Folder to store uploaded files
UPLOAD_DESTINATION = r"C:\Users\33768\Documents\Projects\streamlitSnippets\upload_app\destination"

def login():
    st.title("Login")

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
        else:
            st.error("Invalid username or password")


def main_app():
    st.title("Upload Your Files")
    st.write(f"Logged in as: `{st.session_state.username}`")

    # Ensure the upload destination exists
    os.makedirs(UPLOAD_DESTINATION, exist_ok=True)

    # Upload multiple files
    uploaded_files = st.file_uploader(
        "Select one or more files from your computer",
        accept_multiple_files=True,
        type=None
    )

    # Display file status
    files_to_upload = []
    if uploaded_files:
        st.subheader("Selected Files:")
        for uploaded_file in uploaded_files:
            save_path = Path(UPLOAD_DESTINATION) / uploaded_file.name
            if save_path.exists():
                st.warning(f"⚠️ '{uploaded_file.name}' already exists and will be overwritten.")
            else:
                st.info(f"🟢 '{uploaded_file.name}' is ready to upload.")
            files_to_upload.append((uploaded_file, save_path))

        if st.button("Confirm Upload"):
            for uploaded_file, save_path in files_to_upload:
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
            st.success("✅ All selected files uploaded successfully.")

    # Show files in the destination folder
    st.subheader("Files in Upload Folder:")
    files = os.listdir(UPLOAD_DESTINATION)
    if files:
        for file in files:
            st.write(f"- {file}")
    else:
        st.info("No files uploaded yet.")


def main():
    if st.session_state.get("authenticated", False):
        main_app()
    else:
        login()


if __name__ == "__main__":
    main()
