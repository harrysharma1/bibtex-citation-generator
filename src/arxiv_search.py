from ssl import SSLEOFError, SSLError
import arxiv

class ArxivSearch():
    def __init__(self) -> None:
        self.arxiv_client = arxiv.Client()
    
    def arxiv_to_bibtex(self, url):
        full_url = url
        url = url.strip()
        url = url.replace("arxiv:", "")
        url = url.replace("https://", "")
        url = url.replace("www.", "")
        url = url.replace("arxiv.org/abs/", "")
        url = url.split('v')[0]
        xid = url.strip()
        print(xid)
        try:
            search_by_id = arxiv.Search(id_list=[xid])
            first_result = next(self.arxiv_client.results(search_by_id))
            print(first_result.title)
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