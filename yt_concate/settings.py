from dotenv import load_dotenv
import os

API_KEY = os.getenv('API_KEY')
load_dotenv()


DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'caption')