from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
from datetime import date
class BibtexUtility():
    def __init__(self):
        self.today = date.today()
    
    def extract_title(self, url):
        try:
            html = requests.get(url)
            html.raise_for_status()
            body = html.content
            bs = BeautifulSoup(body, 'html.parser')
            return bs.title.string
        except HTTPError as er:
            match (er.response.status_code):
                case 403:
                    print("{}: Unable to access the page".format(er.response.status_code))
                    return "<Unable to find title>"   
                case 404:
                    print("{}: Unable to find the page of copied URL")
                    return "<Unable to find title>"      
        except Exception as e:
            print("Unkown error has occurred:{}".format(e))
            return "<Unable to find title>"
    def author_lists(self, authors):
        authors_list = authors.split(',')
        formatted_text = ""
        for i in range(len(authors_list)):
            formatted_text += "{}".format(authors_list[i])
            if i < len(authors_list)-1:
                formatted_text += " and "
        return formatted_text

    def get_current_date(self):
        return self.today.strftime("%d/%m/%Y")

    def get_current_year(self):
        return self.today.strftime("%Y")
    
    def get_current_month(self):
        return self.today.strftime("%m")

    def extract_tags_with_author(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            bs = BeautifulSoup(response.content, 'html.parser')
            
            def contains_string(tag):
                return "author" in tag.get_text()
            
            tags_with_string = bs.find_all(contains_string)
            return tags_with_string
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return []