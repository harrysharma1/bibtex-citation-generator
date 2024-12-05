from bs4 import BeautifulSoup
import requests
from datetime import date
class BibtexUtility():
    def __init__(self):
        self.today = date.today()
    
    def extract_title(self, url):
        html = requests.get(url)
        body = html.content
        bs = BeautifulSoup(body, 'html.parser')
        return bs.title.string

    def get_current_date(self):
        return self.today.strftime("%d/%m/%Y")

    def get_current_year(self):
        return self.today.strftime("%Y")
    
    def get_current_month(self):
        return self.today.strftime("%m")
