from abc import ABC, abstractmethod
import requests
import csv
import os
import time
from datetime import datetime
import re
from config.settings import SCRAPPING_DIR

class APIBase(ABC):
    def __init__(self, cookies_str, base_url):
        self.query = ""
        self.cookies = self._extract_cookies(cookies_str)
        self.base_url = base_url
        os.makedirs(self._dir())

    def _dir(self):
        return f"{SCRAPPING_DIR}/{self._name()}"

    def _extract_cookies(self, cookies_str):
        cookies = {}
        if not cookies_str:
            return cookies
        cookie_parts = cookies_str.split(';')
        for part in cookie_parts:
            key_value = part.strip().split('=', 1)
            if len(key_value) == 2:
                key, value = key_value
                cookies[key.strip()] = value.strip()
        return cookies

    def _save_to_csv(self, data_list, file_path):
        os.makedirs(SCRAPPING_DIR, exist_ok=True)
        with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data_list[0].keys())
            writer.writeheader()
            writer.writerows(data_list)

    @abstractmethod
    def _fetch_data(self):
        pass
 
    @abstractmethod
    def _name(self):
        pass

    @abstractmethod
    def _parse_data(self, json_response):
        pass

    def _clean_text(self, text):
        return re.sub(r" +", " ", re.sub(r"\n+", " ", text)).rstrip()

    def set_query(self, q: str):
        self.query = q

    def execute(self):
        while True:
            try:
                print(f"------------------------------------------------------------")
                # Fetch and parse the data
                json_response = self._fetch_data()
                
                if not json_response.get("items"):
                    print(f"[EXIT] [] Finished")
                    break
                
                data_list = self._parse_data(json_response)

                # Create a timestamped file name
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                csv_file_name = os.path.join(self._dir(), f"{self._name()}_{timestamp}.csv")

                # Save to CSV
                self._save_to_csv(data_list, csv_file_name)
                print(f"[SAVED] [] {csv_file_name}")

            except requests.exceptions.RequestException as e:
                print(f"[ERROR] [fetching data] {e}")

            print(f"[WAIT] wating 5s ...")
            time.sleep(10)

