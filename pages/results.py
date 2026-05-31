import streamlit as st
import os

from model.recommender import extract_feature
from model.knnmodel import get_neighbors
from utils.helper import load_product_from_image
from model.upload import save_image_and_manage
st.set_page_config(page_title="Results", layout="wide")

st.title("🛍️ Recommended Product")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if "query_image" not in st.session_state:
    st.warning("No image selected. Go back to home.")
    st.stop()

img_path = st.session_state["query_image"]
  
st.subheader("🔍 Selected Image")

col1, col2 = st.columns([1, 2])
 
with col1:
    if os.path.exists(img_path):
        st.image(img_path)
        
    else:
        st.write("Image not found")
    # save_image_and_manage(img_path)
    # print(img_path)

 
with col2:
    #    print(img_path)
       product_json = load_product_from_image(img_path)

        # Myntra JSON format

       if product_json:

        data = product_json.get("data", {}) if product_json else {}
         

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
  
features = extract_feature(img_path)
 
indices, filenames = get_neighbors(features)

st.subheader("✨ Similar Products")

 
cols = st.columns(5)

for i, idx in enumerate(indices):
    with cols[i % 5]:
        rec_img = filenames[idx].replace("/","\\")
        
        new_path = rec_img.replace("..\\", "")
        

        print(new_path)
        # rec_img = os.path.join(BASE_DIR, filenames[idx])
        # print("path",rec_img)
        if os.path.exists(new_path):
            st.image(new_path)
            # st.image("../fashion_dataset/images/1911.jpg")

            # count = os.listdir('.')
            if st.button("View", key=f"img_{i}"):
                st.session_state["query_image"] = new_path
                # save_image_and_manage(rec_img)
                
                st.switch_page("pages/results.py")
                # pass

        else:
            st.write("No Image")
            

         
            product_json = load_product_from_image(rec_img)

    
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
