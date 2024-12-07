from abc import abstractmethod
from src.arxiv_search import ArxivSearch
from src.utils import BibtexUtility
import subprocess
import uuid


class Bibtex():
    def __init__(self):
        self.citation_key = uuid.uuid4()
        self.arxiv_search = ArxivSearch()
        self.utility_function = BibtexUtility()
       
        
    @abstractmethod
    def get_bibtex(self, url):
        pass

class OnlineBibtex(Bibtex):
    def __init__(self):
        super().__init__()
     
    
    def get_bibtex(self, url, type, key, author, last_accessed, release_year):
        if "https://arxiv.org" in url:
            self.arxiv_search.arxiv_to_bibtex(url, type, key)
        elif "https://ieeexplore.ieee.org" in url:
            pass
        else:
            print("Starting generation...")
            text = "@{}".format(type)
            text += "{"
            text += "{},\n".format(key)
            text += "   author = {"
            text += "{}".format(self.utility_function.author_lists(author))
            text += "},\n"
            text += "   title = {"
            text += "{}".format(self.utility_function.extract_title(url))
            text += "},\n"
            text += "   url = {"
            text +="{}".format(url)
            text +="},\n"
            text +="   addendum = {last accessed: "
            text += "{}".format(last_accessed)
            text += "},\n"
            text += "   year = {"
            text += "{}".format(release_year)
            text += "}\n}"
            subprocess.run("pbcopy", text=True, input=text)
            print("Finished generating:\n{}".format(text))
            print("Copied to clipboard")

class MiscBibtext(Bibtex):
    def __init__(self):
        super().__init__()
        
    def get_bibtex(self, url, type, key, author, last_accessed, release_year):
        if "https://arxiv.org" in url:
            self.arxiv_search.arxiv_to_bibtex(url, type, key)
        else:      
            print("Starting generation...")
            text = "@{}".format(type)
            text += "{"
            text += "{},\n".format(key)
            text += "   author = {"
            author_name = ", ".join(author.split(' ')[::-1])
            text += "{}".format(author_name)
            text += "},\n"
            text += "   title = {"
            text += "{}".format(self.utility_function.extract_title(url))
            text += "},\n"
            text += "   url = {"
            text +="{}".format(url)
            text +="},\n"
            text +="   addendum = {last accessed: "
            text += "{}".format(last_accessed)
            text += "},\n"
            text += "   year = {"
            text += "{}".format(release_year)
            text += "}\n}"
            subprocess.run("pbcopy", text=True, input=text)
            print("Finished generating:\n{}".format(text))
            print("Copied to clipboard")

class InproceedingsBibtex(Bibtex):
    def __init__(self):
        super().__init__()
        
    def get_bibtex(self, url, type, key, title, author):
        text = ""
        text += "@{}".format(type)
        text += "{"
        text += "{},\n".format(key)
        text += "   title = {"
        if title is None:
            text += "{}".format(self.utility_function.extract_title(url))
        else:
            text += "{}".format(title)
        text += "},\n"
        text += "   author = {"
        text += "{}".format(self.utility_function.extract_tags_with_author(url))
        text += "},\n" 
        print(text)