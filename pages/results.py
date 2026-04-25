import streamlit as st
import os

from model.recommender import extract_feature
from model.knnmodel import get_neighbors
from utils.helper import load_product_from_image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Results", layout="wide")

st.title("🛍️ Recommended Products")

# ---------------- CHECK SESSION ----------------
if "query_image" not in st.session_state:
    st.warning("No image selected. Go back to home.")
    st.stop()

img_path = st.session_state["query_image"]


# ---------------- SHOW SELECTED IMAGE ----------------
st.subheader("🔍 Selected Image")

col1, col2 = st.columns([1, 2])

# LEFT SIDE → IMAGE
with col1:
    if os.path.exists(img_path):
        st.image(img_path)
    else:
        st.write("Image not found")

# RIGHT SIDE → DETAILS
with col2:
       
       product_json = load_product_from_image(img_path)

        # Myntra JSON format

       if product_json:

        data = product_json.get("data", {}) if product_json else {}
        # data = product_json.get("data", {})

        st.markdown(f"## {data.get('productDisplayName', 'Unknown')}")

        st.write(f"💰 Price: ₹{data.get('price', 'N/A')}")
        st.write(f"🎨 Color: {data.get('baseColour', 'N/A')}")
        # st.write(f"👕 Type: {data.get('articleType', 'N/A')}")
        # st.write(f"🧥 Category: {data.get('masterCategory', 'N/A')}")
        st.write(f"🧑 Gender: {data.get('gender', 'N/A')}")
        st.write(f"📅 Season: {data.get('season', 'N/A')}")
        st.write(f"⭐ Rating: {data.get('myntraRating', 'N/A')}")

       else:
        st.warning("No product details found")
 
# ---------------- FEATURE EXTRACTION ----------------
features = extract_feature(img_path)

# ---------------- GET RECOMMENDATIONS ----------------
indices, filenames = get_neighbors(features)

st.subheader("✨ Similar Products")

# ---------------- DISPLAY GRID ----------------
cols = st.columns(5)

for i, idx in enumerate(indices):
    with cols[i % 5]:
        rec_img = filenames[idx]

        if os.path.exists(rec_img):
            st.image(rec_img)
            # st.image(img_path)
            if st.button("View", key=f"img_{i}"):
                st.session_state["query_image"] = img_path
                st.switch_page("pages/results.py")

        else:
            st.write("No Image")

        # ✅ LOAD PRODUCT JSON PER IMAGE
        product_json = load_product_from_image(rec_img)

        # Myntra JSON format
        data = product_json.get("data", {}) if product_json else {}

        # ---------------- PRODUCT DETAILS ----------------
        st.markdown(f"**{data.get('productDisplayName', 'Unknown')}**")
        st.write(f"Price :  ₹{data.get('price', 'N/A')}")
        st.write(f"Color :  {data.get('baseColour', '')}")
        # st.write(f"👕 {data.get('articleType', '')}")

        # ---------------- CLICK TO RE-RECOMMEND ----------------
        # if st.button(" ca", key=f"rec_{i}"):
        #     st.session_state["query_image"] = rec_img
        #     st.switch_page("pages/results.py")

        #     st.image(img_path, use_column_width=True)