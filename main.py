import argparse
from src.bibtex import OnlineBibtex, MiscBibtext
from src.utils import BibtexUtility
import uuid

utility = BibtexUtility()

parser = argparse.ArgumentParser(prog="Bibtext Generator", description="Generate Bibtex from URLs")
parser.add_argument("url")
parser.add_argument("-t", "--type", default="misc")
parser.add_argument("-k", "--key", default=uuid.uuid4())
parser.add_argument("-a", "--author")
parser.add_argument("-r", "--release", default=utility.get_current_year())
parser.add_argument("-l", "--last-accessed", default=utility.get_current_date())

args = parser.parse_args()

match args.type:
    case "online":
        OnlineBibtex().get_bibtex(args.url, args.key, args.author, args.last_accessed, args.release)
    case "misc":
        MiscBibtext().get_bibtex(args.url, args.type, args.type, args.author, args.last_accessed, args.release)
    case _:
        "Error: No type provided"
