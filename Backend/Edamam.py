import requests
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Edamam.py
import requests

def fetch_recipes(query, app_id, app_key):
    """Fetch recipes from Edamam's API based on a search query."""
    url = "https://api.edamam.com/search"
    params = {
        "q": query,
        "app_id": app_id,
        "app_key": app_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch recipes", response.status_code, response.text)
