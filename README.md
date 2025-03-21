# National Park Wallpaper Script

This Python script automatically sets your desktop background to a random photo of a UK national park using the Unsplash API. If the API fails (e.g., no internet connection), it falls back to locally downloaded images or a default fallback image. You can easily change this to any theme you want. It is made to work with i3 but can easily be used for other window managers with a few tweaks.

---

## Features
- Fetches a random landscape photo of a UK national park from Unsplash.
- Saves downloaded images to a local directory for offline use.
- Falls back to locally stored images if the API fails.
- Sets the wallpaper using `feh` (compatible with i3 and other lightweight window managers).

---

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- `feh` (for setting the wallpaper)
- Unsplash API key (get one from [Unsplash Developer Portal](https://unsplash.com/developers))

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/national-park-wallpaper.git
cd national-park-wallpaper
```

### 2. Install Dependencies
Install the required Python library:
```bash
pip install requests
```
Install `feh`:
```bash
sudo apt install feh
```

### 3. Set up Unsplash API Key

1.Go to the Unsplash Developer Portal.
2.Create a new application to get your API key.
3.Replace the API key in the file with yours.

### 4. Create Local Directories

Create the directory for storing the downloaded images:
```bash
mkdir -p ~/Pictures/NationalParksUK
```

Run the script once to download an image and set it as the fallback in-case you dont have wifi.

---

## Usage

Run the script manually:
```bash
python3 set_national_park_background.py
```

# Set up automatic execution
1. Open your i3 config file:
```bash
nano ~/.config/i3/config
```

2. Add the following line to the bottom of the config file (set the path to wherever you saved it to):
```bash
exec --no-startup-id python3 /path/to/set_national_park_background.py
```

3. Save and restart i3:
```bash
i3-msg restart
```

---

## Running with Docker

To run the `i3_wallpaper_rotation` script using Docker:

1. Build the Docker image:

   ```bash
   docker build -t i3_wallpaper_rotation:latest .
    ```

2. Build the Docker container: 
```bash
docker run --rm i3_wallpaper_rotation:latest
```

Ensure that Docker is installed and running on your system. For more information on using Docker with Python applications, refer to the Docker documentation.

---

# Troubleshooting

- 401 Unauthorized Error: Ensure your Unsplash API key is correct and properly set in the script.
- No Internet Connection: The script will fall back to locally stored images or the fallback image.
- feh Not Working: Install `feh` or replace it with another wallpaper-setting tool.

---

# Licence

This project is licensed under the MIT License. See the LICENSE file for details.

--- 

Enjoy your dynamic desktop backgrounds! 🌄 
Please contact me if you have any issues!