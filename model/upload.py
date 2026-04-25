import os
import json
 

UPLOAD_FOLDER = "uploads"
HISTORY_FILE = "history.json"


def save_image_and_manage(uploaded_file):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

     
    # ext = uploaded_file.name.split(".")[-1]
    # filename = str(uuid.uuid4()) + "." + ext
    file_path = os.path.join(UPLOAD_FOLDER,uploaded_file.name )

    # save file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # load history safely
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                content = f.read().strip()
                history = json.loads(content) if content else []
        except:
            history = []
    else:
        history = []

     
    history = [h for h in history if h != file_path]

    # add new image
    history.insert(0, file_path)

    # keep only 10
    if len(history) > 7:
        old_images = history[7:]
        for img in old_images:
            if os.path.exists(img):
                os.remove(img)
        history = history[:7]

    # save
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

    return file_path