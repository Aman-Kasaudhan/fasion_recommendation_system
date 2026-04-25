import pandas as pd
import os

# load data
def load_data():
    df = pd.read_csv("fashion-dataset/styles.csv", on_bad_lines='skip')
    df = df.dropna().reset_index(drop=True)

    # create image path
    df['img_path'] = df['id'].apply(
        lambda x: os.path.join("fashion-dataset", "images", str(x) + ".jpg")
    )

    # ✅ convert columns to lowercase ONCE (faster search)
    df["productDisplayName"] = df["productDisplayName"].str.lower()
    df["gender"] = df["gender"].str.lower()
    df["masterCategory"] = df["masterCategory"].str.lower()
    df["subCategory"] = df["subCategory"].str.lower()
    df["baseColour"] = df["baseColour"].str.lower()

    return df


# search image
def search_products(df, name="", gender="", category="", subcategory="", color=""):
    result = df.copy()

     
    if name:
        name = name.lower()
        result = result[result["productDisplayName"].str.contains(name, na=False)]

   
    if gender:
        result = result[result["gender"] == gender.lower()]

    
    if category:
        result = result[result["masterCategory"] == category.lower()]

    
    if subcategory:
        result = result[result["subCategory"] == subcategory.lower()]

   
    if color:
        result = result[result["baseColour"] == color.lower()]

     
    result = result[result["img_path"].apply(os.path.exists)]

    return result.head(20)