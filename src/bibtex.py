from abc import abstractmethod
from arxiv_search import ArxivSearch
import uuid


class Bibtex():
    def __init__(self):
        self.citation_key = uuid.uuid4()
        
    @abstractmethod
    def get_bibtex(self, url):
        pass
    
    def get_arxiv_search_object():
        return ArxivSearch()
        
