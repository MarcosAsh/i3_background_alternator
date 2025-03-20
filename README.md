National Park Wallpaper Script

This Python script automatically sets your desktop background to a random photo of a UK national park using the Unsplash API. If the API fails (e.g., no internet connection), it falls back to locally downloaded images or a default fallback image.
Features

    Fetches a random landscape photo of a UK national park from Unsplash.

    Saves downloaded images to a local directory for offline use.

    Falls back to locally stored images if the API fails.

    Sets the wallpaper using feh (compatible with i3 and other lightweight window managers).

Requirements

    Python 3.x

    requests library (pip install requests)

    feh (for setting the wallpaper)

    Unsplash API key (get one from Unsplash Developer Portal)

Setup
1. Clone the Repository
bash
Copy

git clone https://github.com/your-username/national-park-wallpaper.git
cd national-park-wallpaper

2. Install Dependencies

Install the required Python library:
bash
Copy

pip install requests

Install feh (if not already installed):
bash
Copy

sudo apt install feh

3. Set Up Unsplash API Key

    Go to the Unsplash Developer Portal.

    Create a new application and get your API key (Client-ID).

    Replace YOUR_UNSPLASH_ACCESS_KEY in the script with your actual API key.

4. Create Local Directories

Create the directory for storing downloaded images:
bash
Copy

mkdir -p ~/Pictures/NationalParksUK

Add a fallback image (optional):
bash
Copy

cp /path/to/your/fallback.jpg ~/Pictures/fallback.jpg

Usage
Run the Script Manually
bash
Copy

python3 set_national_park_background.py

Set Up Automatic Execution
Option 1: i3 Config (Recommended for i3 Users)

    Open your i3 config file:
    bash
    Copy

    nano ~/.config/i3/config

    Add the following line:
    bash
    Copy

    exec --no-startup-id python3 /path/to/set_national_park_background.py

    Save and restart i3:
    bash
    Copy

    i3-msg restart

Option 2: Systemd (Recommended for All Users)

    Create a systemd service file:
    bash
    Copy

    sudo nano /etc/systemd/system/set-wallpaper.service

    Add the following content:
    ini
    Copy

    [Unit]
    Description=Set National Park Wallpaper
    After=network.target

    [Service]
    ExecStart=/usr/bin/python3 /path/to/set_national_park_background.py
    Restart=on-failure
    User=your-username

    [Install]
    WantedBy=default.target

    Enable and start the service:
    bash
    Copy

    sudo systemctl enable set-wallpaper.service
    sudo systemctl start set-wallpaper.service

Option 3: Startup Applications (GUI)

    Open "Startup Applications" from the application menu.

    Add a new startup program:

        Name: Set Wallpaper

        Command: python3 /path/to/set_national_park_background.py

        Comment: Run script to set wallpaper on startup.

Directory Structure
Copy

~/Pictures/
├── NationalParksUK/
│   ├── Lake_District_National_Park.jpg
│   ├── Snowdonia_National_Park.jpg
│   └── ...
└── fallback.jpg

Customization

    Add More Parks: Edit the national_parks list in the script to include additional parks.

    Change Fallback Image: Replace ~/Pictures/fallback.jpg with your preferred image.

    Use a Different Wallpaper Tool: Replace feh with another tool like nitrogen or wal.

Troubleshooting

    401 Unauthorized Error: Ensure your Unsplash API key is correct and properly set in the script.

    No Internet Connection: The script will fall back to locally stored images or the fallback image.

    feh Not Working: Install feh or replace it with another wallpaper-setting tool.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Enjoy your dynamic desktop backgrounds! 🌄
