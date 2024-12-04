from cleaner import clean
from collector import apis
from config import SEARCH_PROMPTS

search_prompts = SEARCH_PROMPTS.split(";")

def collect(q: str):
    for api in apis.values():
        api.reset()
        api.set_query(q)
        api.execute()

if __name__ == "__main__":
    for q in search_prompts:
        collect(q)

    for api in apis.values():
        clean(api)
