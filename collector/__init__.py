from typing import Dict
from config import FREEPIK_BASE_URL, FREEPIK_COOKIES, OPENART_BASE_URL, OPENART_COOKIES, PIXLR_BASE_URL, PIXLR_COOKIES
from .api_base import APIBase
from .openart_api import OpenArtAPI
from .freepik_api import FreepikAPI
from .pixlr_api import PixlrAPI


apis: Dict[str, APIBase] = {
    # "freepik": OpenArtAPI(cookies_str=OPENART_COOKIES, base_url=OPENART_BASE_URL),
    # "openart": FreepikAPI(cookies_str=FREEPIK_COOKIES, base_url=FREEPIK_BASE_URL),
    "pixlr": PixlrAPI(cookies_str=PIXLR_COOKIES, base_url=PIXLR_BASE_URL),
}