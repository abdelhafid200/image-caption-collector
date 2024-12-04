from dotenv import load_dotenv
import os

load_dotenv()

OPENART_COOKIES = os.getenv('OPENART_COOKIES')
OPENART_BASE_URL = "https://openart.ai/api/search"

FREEPIK_COOKIES = os.getenv('FREEPIK_COOKIES')
FREEPIK_BASE_URL = "https://www.freepik.com/api/regular/search"

COLLECTED_DIR = os.getenv('SCRAPPING_DIR',"collected")
CONSIDER_MAX_ITERATON = os.getenv('CONSIDER_MAX_ITERATON',"1")
MAX_ITERATON = int(os.getenv('MAX_ITERATON',5))
TRY_MANY = int(os.getenv('TRY_MANY',3))
WATING = os.getenv('WATING',"1")

SEARCH_PROMPTS = os.getenv('SEARCH_PROMPTS',"")
