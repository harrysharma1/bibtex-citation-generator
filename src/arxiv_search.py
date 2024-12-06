from ssl import SSLEOFError, SSLError
from selenium import webdriver
import subprocess
import arxiv

class ArxivSearch():
    def __init__(self) -> None:
        self.arxiv_client = arxiv.Client()
    
    def arxiv_to_bibtex(self, url, type, key):
        full_url = url
        url = url.strip()
        url = url.replace("arxiv:", "")
        url = url.replace("https://", "")
        url = url.replace("www.", "")
        url = url.replace("arxiv.org/abs/", "")
        url = url.split('v')[0]
        xid = url.strip()
        try:
            search_by_id = arxiv.Search(id_list=[xid])
            first_result = next(self.arxiv_client.results(search_by_id))
            print("Starting generation...")
            text = ""
            text += "@{}".format(type) 
            text += "{"
            text += "{},\n".format(key)
            text += "   title = {"
            text += "{}".format(first_result.title)
            text += "},\n"
            text += "   author = {"
            for i in range(len(first_result.authors)):
                if i < len(first_result.authors)-1:
                    text += "{} and ".format(first_result.authors[i])
                else:
                    text += "{}".format(first_result.authors[i])
            text += "},\n"
            text += "   year = {"
            text += "{}".format(first_result.published.strftime("%Y"))
            text += "},\n"
            text += "   eprint = {"
            text += "{}".format(first_result.get_short_id())
            text += "},\n"
            text += "   archivePrefix = {arXiv"
            text += "},\n"
            text += "   primaryClass = {"
            text += "{}".format(first_result.primary_category)
            text += "},\n"
            text += "   url = {"
            text += "{}".format(first_result.entry_id)
            text += "},\n"
            text += "}"
            print("Finished generating:")
            print(text)
            subprocess.run("pbcopy", text=True, input=text)
            print("Copied to clipboard")
        except arxiv.HTTPError as e:
            print(f"HTTPError: Could not retrieve the paper. Status code: {e.status} for url: {full_url}")
        except StopIteration:
            print("Error: No results found for the given arXiv ID.")
        except SSLError as e:
            print(f"SSLError has occurred: {e}")
        except SSLEOFError as e:
            print(f"SSLEOFError has occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
      
class IEEESearch():
    def __init__(self):
        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument("headless")
        self.driver = webdriver.Chrome(options=browser_options)
      
        