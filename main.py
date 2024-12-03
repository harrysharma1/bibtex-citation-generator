import argparse
import uuid
from bs4 import BeautifulSoup
import requests
from datetime import date

def extract_title(url):
    html = requests.get(url)
    body = html.content
    bs = BeautifulSoup(body, 'html.parser')
    return bs.title.string

def get_current_date():
    today = date.today()
    return today.strftime("%d/%m/%Y")

parser = argparse.ArgumentParser(prog="Bibtext Generator", description="Generate Bibtex from URLs")
parser.add_argument("url")
parser.add_argument("-k", "--key", default=uuid.uuid4())
parser.add_argument("-a", "--author")
parser.add_argument("-r", "--release", default=get_current_date() )

args = parser.parse_args()


text = "@online"
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
text +="    addendum = {last accessed: "

text += "{}".format(args.release)


print(text)