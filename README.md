# National Park Wallpaper Script

This Python script automatically sets your desktop background to a random photo of a UK national park using the Unsplash API. If the API fails (e.g., no internet connection), it falls back to locally downloaded images or a default fallback image.

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
cd national-park-wallpaper```
