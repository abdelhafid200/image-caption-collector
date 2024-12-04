from collector import FreepikAPI
from collector import OpenArtAPI
from config.settings import FREEPIK_BASE_URL,FREEPIK_COOKIES,OPENART_BASE_URL,OPENART_COOKIES
from search import search_prompts

def collect(q: str):
    openart = OpenArtAPI(cookies_str=OPENART_COOKIES, base_url=OPENART_BASE_URL)
    openart.set_query(q)
    openart.execute()

    freepik = FreepikAPI(cookies_str=FREEPIK_COOKIES, base_url=FREEPIK_BASE_URL)
    freepik.set_query(q)
    freepik.execute()

if __name__ == "__main__":
    for q in search_prompts:
        collect(q)