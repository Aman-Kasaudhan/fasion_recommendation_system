import streamlit as st
import os
from PIL import Image

from model.upload import save_image_and_manage
from model.history import get_history
from model.search import search_products,load_data   # 👈 add this

st.set_page_config(page_title="Fashion App", layout="wide")

# ---------------- TITLE ----------------
st.title("🛍️ Fashion Recommendation System")

df=load_data()
# ---------------- TOP BAR (SEARCH + UPLOAD) ----------------
col1, col2 = st.columns([2, 1])

# 🔍 SEARCH
with col1:  
    query = st.text_input("🔍 Search product (shirt, jeans, dress...)")

# 📤 UPLOAD
with col2:
    uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg", "png", "jpeg"])


# ---------------- IMAGE UPLOAD FLOW ----------------
if uploaded_file:
    img_path = save_image_and_manage(uploaded_file)

    st.success("Image uploaded successfully ✅")
    st.image(img_path, width=200)

    st.session_state["query_image"] = img_path

    if st.button("🔍 Show Recommendations"):
        st.switch_page("pages/results.py")


# ---------------- SEARCH FLOW ----------------
elif query:
    results = search_products(df,name=query)

    st.subheader("🔍 Search Results")

    if len(results) > 0:
        cols = st.columns(5)

        for i, (_, row) in enumerate(results.iterrows()):
            with cols[i % 5]:
                if os.path.exists(row["img_path"]):
                    st.image(row["img_path"])
                    st.write(row["productDisplayName"])

                    if st.button("View", key=f"search_{i}"):
                        st.session_state["query_image"] = row["img_path"]
                        st.switch_page("pages/results.py")
                else:
                    st.write("Image not found")
    else:
        st.write("No results found")


# ---------------- HOME (DEFAULT HISTORY) ----------------
else:

    st.subheader("🕘 Recent Uploaded Images")
    history = get_history()

    if history :
        cols = st.columns(5)

        for i, img_path in enumerate(history):
            with cols[i % 5]:
                if os.path.exists(img_path):
                    st.image(img_path)

                    if st.button("View", key=f"img_{i}"):
                        st.session_state["query_image"] = img_path
                        st.switch_page("pages/results.py")
                else:
                    st.write("Image not found")

    else:
        st.write("No previous uploads yet")