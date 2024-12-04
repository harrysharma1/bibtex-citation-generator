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
        self.subprocess = subprocess
        
    @abstractmethod
    def get_bibtex(self, url):
        pass

class OnlineBibtex(Bibtex):
    def __init__(self):
        super().__init__()
     
    
    def get_bibtex(self, url, type, key, author, last_accessed, release):
        if "https://arxiv.org" in url:
            self.arxiv_search.arxiv_to_bibtex(url)
        else:
            print("Starting generation...")
            text = "@{}".format(type)
            text += "{"
            text += " {},\n".format(key)
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
            text += "{}".format(release)
            text += "}\n}"
            self.subprocess.run("pbcopy", text=True, input=text)
            print("Finished generating:\n{}".format(text))
            print("Copied to clipboard")

class MiscBibtext(Bibtex):
    def __init__(self):
        super().__init__()
        
    def get_bibtex(self, url, type, key, author, last_accessed, release):
        print("Starting generation...")
        text = "@{}".format(type)
        text += "{"
        text += " {},\n".format(key)
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
        text += "{}".format(release)
        text += "}\n}"
        self.subprocess.run("pbcopy", text=True, input=text)
        print("Finished generating:\n{}".format(text))
        print("Copied to clipboard")