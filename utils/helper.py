import os
import json

def get_id_from_path(path):
    return os.path.basename(path).split(".")[0]



STYLE_FOLDER = "fashion-dataset/styles"

def load_product_from_image(img_path):
    try:
      
        product_id = os.path.basename(img_path).split(".")[0]

        json_path = os.path.join(STYLE_FOLDER, product_id + ".json")

        if os.path.exists(json_path):
            with open(json_path, "r") as f:
                return json.load(f)

    except:
        pass

    return {}