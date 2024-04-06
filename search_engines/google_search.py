from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests
import os
import random

# Access environment variables
API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
CSE_ID = os.getenv("GOOGLE_SEARCH_CSE_ID")


def parse_link(link):
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant information from the page
        paragraphs = [p.text.strip() for p in soup.find_all('p')]

        # Ignore data if no paragraphs are found
        if not paragraphs:
            return None

        # Extract title
        title = soup.title.text.strip()

        # Extract images
        images = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                if src.startswith('http'):
                    images.append(src)
                elif src.startswith('/'):
                    # Handle relative URLs
                    images.append(link + src)

        # Select a random image if multiple images found
        random_image = random.choice(images) if images else None

        return {'title': title, 'paragraphs': paragraphs, 'image': random_image, 'link': link}
    except Exception as e:
        print(f"Error parsing link {link}: {e}")
        return None


def search_google(query):
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        result = service.cse().list(q=query, cx=CSE_ID).execute()
        return result['items']
    except Exception as e:
        print(f"Error searching Google: {e}")
        return []