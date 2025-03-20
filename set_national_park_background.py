import os
import random
import requests
from subprocess import call

# Unsplash API key
API_KEY = "SET_TO_YOUR_API_KEY"

# Directory to save the images
image_dir = os.path.expanduser("~/Pictures/NationalParksUK")
os.makedirs(image_dir, exist_ok=True)

# Fallback image path (ensure this image exists)
fallback_image = os.path.expanduser("~/Pictures/NationalParksUK/SET_TO_DEFAULT")

# List of national parks in the UK
national_parks = [
    "Lake District National Park",
    "Snowdonia National Park",
    "Peak District National Park",
    "Yorkshire Dales National Park",
    "Exmoor National Park",
    "Northumberland National Park",
    "Brecon Beacons National Park",
    "Cairngorms National Park",
    "Loch Lomond and The Trossachs National Park",
    "Pembrokeshire Coast National Park",
    "New Forest National Park",
    "South Downs National Park",
    "Dartmoor National Park",
    "North York Moors National Park",
    "The Broads National Park",
    "Norfolk Coast National Park",
]

# Function to fetch a random image from Unsplash
def fetch_random_image(query):
    url = "https://api.unsplash.com/photos/random"
    headers = {
        "Authorization": f"Client-ID {API_KEY}"
    }
    params = {
        "query": query,
        "orientation": "landscape",
    }
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            image_url = data["urls"]["full"]
            image_path = os.path.join(image_dir, f"{query.replace(' ', '_')}.jpg")
            download_image(image_url, image_path)
            return image_path
        else:
            print(f"Failed to fetch image from Unsplash. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image from Unsplash: {e}")
        return None

# Function to download the image
def download_image(image_url, image_path):
    try:
        response = requests.get(image_url, timeout=10)
        if response.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(response.content)
            print(f"Image saved to: {image_path}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

# Function to set the background using feh
def set_background(image_path):
    call(["feh", "--bg-fill", image_path])

# Function to get a random local image
def get_random_local_image():
    images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith((".jpg", ".png"))]
    if images:
        return random.choice(images)
    else:
        return None

# Main function
def main():
    # Choose a random national park
    park = random.choice(national_parks)
    print(f"Setting background to a photo of {park}...")
    
    # Try to fetch a new image from Unsplash
    image_path = fetch_random_image(park)
    
    # If Unsplash fails, use a random local image
    if not image_path:
        print("Falling back to local images...")
        image_path = get_random_local_image()
    
    # If no local images are available, use the fallback image
    if not image_path:
        print("No local images found. Using fallback image...")
        image_path = fallback_image
    
    # Set the background
    if image_path:
        set_background(image_path)
        print(f"Background set to {image_path}")
    else:
        print("Failed to set background. No images available.")

if __name__ == "__main__":
    main()