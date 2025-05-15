import streamlit as st
import os
from pathlib import Path

# Dummy credentials
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

    os.makedirs(UPLOAD_DESTINATION, exist_ok=True)

    # Initialize session state variables
    if "files_to_upload" not in st.session_state:
        st.session_state.files_to_upload = []
    if "failed_uploads" not in st.session_state:
        st.session_state.failed_uploads = []
    if "uploader_key" not in st.session_state:
        st.session_state.uploader_key = 0  # dynamic key to force reset

    # Reset button to clear uploader
    if st.button("🔄 Reset Upload"):
        st.session_state.files_to_upload = []
        st.session_state.failed_uploads = []
        st.session_state.uploader_key += 1  # trigger uploader reset
        st.experimental_rerun()

    # Upload widget with dynamic key
    uploaded_files = st.file_uploader(
        "Select one or more files from your computer",
        accept_multiple_files=True,
        type=None,
        key=f"uploader_{st.session_state.uploader_key}"
    )

    if uploaded_files:
        st.session_state.files_to_upload = []  # Clear list before adding
        st.session_state.failed_uploads = []

        for uploaded_file in uploaded_files:
            save_path = Path(UPLOAD_DESTINATION) / uploaded_file.name
            st.session_state.files_to_upload.append((uploaded_file, save_path))
            if save_path.exists():
                st.warning(f"⚠️ '{uploaded_file.name}' already exists and will be overwritten.")

        st.info(f"🗂️ {len(st.session_state.files_to_upload)} file(s) selected for upload.")

        if st.button("✅ Confirm Upload"):
            for uploaded_file, save_path in st.session_state.files_to_upload:
                try:
                    with open(save_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                except Exception as e:
                    st.session_state.failed_uploads.append(uploaded_file.name)

            if st.session_state.failed_uploads:
                st.success(f"🗂️ {len(st.session_state.files_to_upload)-len(st.session_state.failed_uploads)} file(s) successfully for upload.")
                st.error("❌ Some files could not be uploaded:")
                str_files = " ".join([f'"{fname}"' for fname in st.session_state.failed_uploads])
                st.write(f"Not loaded files: {str_files}")
            else:
                st.success("✅ All selected files uploaded successfully.")

    # Show files currently in destination
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
