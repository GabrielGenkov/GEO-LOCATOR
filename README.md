# GEO LOCATOR

This program utilizes the Google Maps Geolocation API to retrieve location information based on the provided address. Follow the instructions below to set up the program and obtain the necessary API key.

## Getting Started

### 1. Set Up Google Cloud Console Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.

### 2. Enable Geolocation API

1. In the Cloud Console, navigate to the "APIs & Services" > "Library" section.
2. Search for "Geolocation API" and enable it for your project.

### 3. Enable Billing

1. In the Cloud Console, navigate to the "Billing" section.
2. Enable billing for your project.

### 4. Create API Key

1. In the Cloud Console, navigate to the "APIs & Services" > "Credentials" section.
2. Create a new API Key.
3. Restrict the API key if needed (e.g., restrict by IP address).
4. Make note of the API Key; you will use it in the next steps.

### 5. Set Up .env File

1. Create a file named `.env` in the root directory of your project.
2. Add the following line to the `.env` file, replacing `your_actual_api_key` with the API key obtained in the previous step:

```
GOOGLE_MAPS_API_KEY=your_actual_api_key
```

Save the file.

## How to Use

1. Install required Python packages:

```bash
pip install -r requirements.txt
```
Run your Python script:

```bash
python main.py
```