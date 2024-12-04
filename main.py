import argparse
import uuid
from bs4 import BeautifulSoup
import requests
from datetime import date
import subprocess

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

parser = argparse.ArgumentParser(prog="Bibtext Generator", description="Generate Bibtex from URLs")
parser.add_argument("url")
parser.add_argument("-t", "--type", default="misc")
parser.add_argument("-k", "--key", default=uuid.uuid4())
parser.add_argument("-a", "--author")
parser.add_argument("-r", "--release", default=get_current_year())
parser.add_argument("-l", "--last-accessed", default=get_current_date())

args = parser.parse_args()

def online_bibtex():
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
