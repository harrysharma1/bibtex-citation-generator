import argparse
from ssl import SSLEOFError, SSLError
import uuid
from bs4 import BeautifulSoup
import requests
from datetime import date
import subprocess
import arxiv
import string
arxiv_client = arxiv.Client()

def extract_title(url):
    html = requests.get(url)
    body = html.content
    bs = BeautifulSoup(body, 'html.parser')
    return bs.title.string

def get_current_date():
    today = date.today()
    return today.strftime("%d/%m/%Y")

def get_current_year():
    today = date.today()
    return today.strftime("%/Y")

def arxiv_to_bibtex(url):
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
        first_result = next(arxiv_client.results(search_by_id))
        print(first_result.title)
    except arxiv.HTTPError as e:
        print(f"HTTPError: Could not retrieve the paper. Status code: {e.status}")
    except StopIteration:
        print("Error: No results found for the given arXiv ID.")
    except SSLError as e:
        print(f"SSLError has occurred: {e}")
    except SSLEOFError as e:
        print(f"SSLEOFError has occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

parser = argparse.ArgumentParser(prog="Bibtext Generator", description="Generate Bibtex from URLs")
parser.add_argument("url")
parser.add_argument("-t", "--type", default="misc")
parser.add_argument("-k", "--key", default=uuid.uuid4())
parser.add_argument("-a", "--author")
parser.add_argument("-r", "--release", default=get_current_year())
parser.add_argument("-l", "--last-accessed", default=get_current_date())

args = parser.parse_args()

def online_bibtex():
    if "https://arxiv.org" in args.url:
       arxiv_to_bibtex(args.url) 
    else:
        print("Starting generation...")
        text = "@{}".args.type
        text += "{"
        text += " {},\n".format(args.key)
        text += "   author = {"
        author_name = ", ".join(args.author.split(' ')[::-1])
        text += "{}".format(author_name)
        text += "},\n"
        text += "   title = {"
        text += "{}".format(extract_title(args.url))
        text += "},\n"
        text += "   url = {"
        text +="{}".format(args.url)
        text +="},\n"
        text +="   addendum = {last accessed: "
        text += "{}".format(args.last_accessed)
        text += "},\n"
        text += "   year = {"
        text += "{}".format(args.release)
        text += "}\n}"
        subprocess.run("pbcopy", text=True, input=text)
        print("Finished generating:\n{}".format(text))
        print("Copied to clipboard")
        
def misc_bibtex():
    print("Starting generation...")
    text = "@{}".format(args.type)
    text += "{"
    text += " {},\n".format(args.key)
    text += "   author = {"
    author_name = ", ".join(args.author.split(' ')[::-1])
    text += "{}".format(author_name)
    text += "},\n"
    text += "   title = {"
    text += "{}".format(extract_title(args.url))
    text += "},\n"
    text += "   url = {"
    text +="{}".format(args.url)
    text +="},\n"
    text +="   addendum = {last accessed: "
    text += "{}".format(args.last_accessed)
    text += "},\n"
    text += "   year = {"
    text += "{}".format(args.release)
    text += "}\n}"
    subprocess.run("pbcopy", text=True, input=text)
    print("Finished generating:\n{}".format(text))
    print("Copied to clipboard")

match args.type:
    case "online":
        online_bibtex()
    case "misc":
        misc_bibtex()  
    case _:
        "Error: No type provided"
