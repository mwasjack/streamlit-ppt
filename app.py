import streamlit as st
from PIL import Image
import os
import re

# --- Streamlit page setup ---
st.set_page_config(page_title="Workshop 1 Presentation", layout="wide")

# --- Slide directory path ---
SLIDE_DIR = "slides"

# --- Helper function to sort files numerically ---
def natural_sort_key(text):
    return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', text)]

# --- List slide image files and sort them ---
slide_files = sorted(
    [f for f in os.listdir(SLIDE_DIR) if f.lower().endswith(".png")],
    key=natural_sort_key
)

# --- Sidebar radio menu for navigation ---
selected_slide = st.sidebar.radio("Select Slide", slide_files)

# --- Display selected slide ---
st.title("📊 Workshop 1: The Anatomy of Failure")

if selected_slide in slide_files:
    slide_path = os.path.join(SLIDE_DIR, selected_slide)
    image = Image.open(slide_path)

    st.header(f"{selected_slide}")
    st.image(image, use_container_width=True)

    with open(slide_path, "rb") as file:
        st.download_button(
            label="⬇️ Download This Slide",
            data=file,
            file_name=selected_slide,
            mime="image/png"
        )
