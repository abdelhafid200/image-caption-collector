import requests
from collector import APIBase

class PixlrAPI(APIBase):
    def __init__(self, cookies_str, base_url):
        super().__init__(cookies_str, base_url)
        self.pagination = {"currentPage": 1}
        
    def reset(self):
        self.pagination = {"currentPage": 1}

    def next(self):
        self.pagination["currentPage"] = self.pagination["currentPage"] + 1

    def _fetch_data(self):
        print(self.base_url + f"/{self.pagination["currentPage"]}")
        response = requests.get(self.base_url + f"/{self.pagination["currentPage"]}")
        response.raise_for_status()
        return response.json()
    
    def name(self):
        return "pixlr"

    def _parse_data(self, json_response):
        data_list = []
        items = json_response.get("data", {}).get("docs", [])
        for item in items:
            print(item)
            data_list.append({
                "id": item.get("primary"),
                "description": self._clean_text(item.get("prompt", "")),
                "image_web": item.get("images", [])[0].get("preview"),
                "image_url": item.get("images", [])[0].get("medium"),
                "width": item.get("width"),
                "height": item.get("height"),
            })
        return data_list
