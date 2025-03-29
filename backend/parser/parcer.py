import threading
import requests
import json
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import uuid


class BaseParser(ABC):
    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def save_to_json(self, data):
        pass


class HackatonsParser(BaseParser):
    def __init__(self, url):
        self.url = url
        self.json_file = "parsed_data.json"

    def parse(self):
        print(f"Запуск парсинга {self.url}")
        response = requests.get(self.url)
        if response.status_code == 200:
            url = "https://feeds.tildaapi.com/api/getfeed/"
            params = {
                "feeduid": "617755803461",
                "recid": "488755787",
                "c": "1743238105418",
                "size": "",
                "slice": "1",
                "sort[date]": "desc",
                "filters[date][>]": "now",
                "getparts": "true"
            }
            headers = {
                "accept": "*/*",
                "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "priority": "u=1, i",
                "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"macOS\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site"
            }
            referrer = "https://www.xn--80aa3anexr8c.xn--p1acf/"

            response = requests.get(url, headers=headers, params=params)
            print(response.json()['posts'][0])  # Если ответ в JSON-формате
            events = []
            for post in response.json()['posts']:
                title = post['title']
                description = post['descr']
                image_url = post['image']
                print(len(post['postparts']))
                format = post['postparts'][1]['parttitle']
                place = None
                if format != 'online' and len(post['postparts']) > 2:
                    place = post['postparts'][2]['parttitle']
                registration_url = post['url']
                start_date = post['date']
                type = "hacatons"
                if place is not None:
                    events.append({
                            "title": title,
                            "type": type,
                            "start_date": start_date,
                            "image_url": image_url,
                            "description": description,
                            "registration_url": registration_url,
                            "format": format,
                            "place": place,
                        })
                else:
                    events.append({
                        "title": title,
                        "type": type,
                        "start_date": start_date,
                        "image_url": image_url,
                        "description": description,
                        "registration_url": registration_url,
                        "format": format
                    })
            self.save_to_json(events)
        else:
            print("Ошибка загрузки страницы")

    def save_to_json(self, data):
        with open(self.json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Данные сохранены в JSON")



class ParserManager:
    def __init__(self):
        self.parsers = []

    def add_parser(self, parser):
        self.parsers.append(parser)

    def run_parsers(self):
        threads = []
        for parser in self.parsers:
            thread = threading.Thread(target=parser.parse)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()


if __name__ == "__main__":
    parcer = ParserManager()
    parcer.add_parser(HackatonsParser("https://www.xn--80aa3anexr8c.xn--p1acf/"))
    parcer.run_parsers()
