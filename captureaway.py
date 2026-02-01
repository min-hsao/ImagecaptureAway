# captureimage.py
# by Min-Hsao Chen (chatGPT 4.0)
# version 0.0007
# last updated: 05.26.2024

import requests

# Base URL for the images
base_url = "https://assets.awaytravel.com/spree/products/{product_id}/original/{image_name}.jpg"

# Dictionary of color names and their corresponding product IDs and image names
colors = {
    "Jet Black": {"product_id": "46182", "image_name": "95310acf-237d-4762-9619-f899a41073f5"},
    "Navy Blue": {"product_id": "45731", "image_name": "98d9c1f7-af5c-45cd-9113-464d27914182"},
    "Coast Blue": {"product_id": "46189", "image_name": "73f8dce5-5e75-4b6f-a117-261694ff6444"},
    "Olive Green": {"product_id": "46196", "image_name": "f6c463ce-29d6-446d-8cfd-652b65f97e24"},
    "Sea Green": {"product_id": "47249", "image_name": "d40617b8-1980-4ba2-a7e5-89348533dbf0"},
    "Cloud Gray": {"product_id": "46563", "image_name": "PDP_PC_Matte_Cloud_CAR_02"},
    "Clay Pink": {"product_id": "47841", "image_name": "PDP_PC_Matte_Clay_CAR_02"},
    "Sorbet Orange": {"product_id": "45983", "image_name": "970ee5d8-2ae3-4bf0-b93a-3604f79fedd6"},
    "Tango Red": {"product_id": "47992", "image_name": "b2b4583f-82e7-47fc-978a-a33188ae31d3"},
    "Salt White (Gloss)": {"product_id": "45777", "image_name": "0c167633-b870-4317-a5f9-97481d0094f4"},
    "Wave Blue (Gloss)": {"product_id": "42983", "image_name": "5d8efdc9-dc3f-4fe7-b1ef-3e6728923a3c"}
}

# Function to download an image
def download_image(image_url, file_name):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}")

# Loop through each color and download the image
for color_name, details in colors.items():
    image_url = base_url.format(product_id=details["product_id"], image_name=details["image_name"])
    download_image(image_url, f"{color_name}.jpg")
