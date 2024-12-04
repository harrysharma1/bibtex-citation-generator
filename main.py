import argparse
from src.bibtex import OnlineBibtex, MiscBibtext
from src.utils import BibtexUtility
import uuid

utility = BibtexUtility()

parser = argparse.ArgumentParser(prog="Bibtext Generator", description="Generate Bibtex from URLs.")
parser.add_argument("url", help="URL for document you would like to cite.")
parser.add_argument("-t", "--type", default="misc", help="The type of document you believe it is. It will default to @misc if not provided.")
parser.add_argument("-k", "--key", default=str(uuid.uuid4()), help="Citation key for bibtex. If not provided, it will default to a UUID string.")
parser.add_argument("-a", "--author", default="<Alter Please>", help="Author name(s). If not provided, will default to <Alter Please>")
parser.add_argument("-r", "--release", default=utility.get_current_year(), help="Release date of the article. If not provided, will default to current year.")
parser.add_argument("-l", "--last-accessed", default=utility.get_current_date(), help="Last accessed article date. If not provided, will default to current date.")

args = parser.parse_args()

match args.type:
    case "online":
        OnlineBibtex().get_bibtex(args.url, args.type, args.key, args.author, args.last_accessed, args.release)
    case "misc":
        MiscBibtext().get_bibtex(args.url, args.type, args.key, args.author, args.last_accessed, args.release)
    case _:
        "Error: No type provided"
