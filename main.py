import argparse
import uuid
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(prog="Bibtext Generator", description="Generate Bibtex from URLs")
parser.add_argument("url")
parser.add_argument("-k", "--key",default=uuid.uuid4())
parser.add_argument("-a", "--author")
parser.add_argument("-r", "--release")

args = parser.parse_args()


text = "@online"
text += "{"
text += "{},\n".format(args.key)
text += "author = {"

author_name = ", ".join(args.author.split(' ')[::-1])
text += "{}".format(author_name)
text += "},\n"
text += "title = {}"


print(text)