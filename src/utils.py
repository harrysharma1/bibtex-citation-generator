from bs4 import BeautifulSoup
import requests
from datetime import date
class BibtexUtility():
    def extract_title(self, url):
        html = requests.get(url)
        body = html.content
        bs = BeautifulSoup(body, 'html.parser')
        return bs.title.string

    def get_current_date(self):
        today = date.today()
        return today.strftime("%d/%m/%Y")

    def get_current_year(self):
        today = date.today()
        return today.strftime("%Y")
