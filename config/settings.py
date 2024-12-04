from dotenv import load_dotenv
import os

load_dotenv()

OPENART_COOKIES = os.getenv('OPENART_COOKIES')
OPENART_BASE_URL = "https://openart.ai/api/search"

FREEPIK_COOKIES = os.getenv('FREEPIK_COOKIES')
FREEPIK_BASE_URL = "https://www.freepik.com/api/regular/search"

SCRAPPING_DIR = os.getenv('SCRAPPING_DIR',"collected")

print(OPENART_COOKIES)
