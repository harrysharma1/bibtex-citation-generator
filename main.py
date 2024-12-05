import argparse
from src.bibtex import OnlineBibtex, MiscBibtext
from src.utils import BibtexUtility
import uuid

utility = BibtexUtility()

parser = argparse.ArgumentParser(prog="Bibtext Generator", description="Generate Bibtex from URLs.")
subparsers = parser.add_subparsers(dest="command", help="Type of bibtex entry")

# @online
online_parser = subparsers.add_parser("online", help="Generate bibtex for online document.")
online_parser.add_argument("url", help="URL for document you would like to cite.")
online_parser.add_argument("-k", "--key", default=str(uuid.uuid4()), help="Citation key for bibtex. If not provided, it will default to a UUID string.")
online_parser.add_argument("-a", "--author", default="<Alter Please>", help="Author name(s). If not provided, will default to <Alter Please>")
online_parser.add_argument("-r", "--release", default=utility.get_current_year(), help="Release date of the article. If not provided, will default to current year.")
online_parser.add_argument("-l", "--last-accessed", default=utility.get_current_date(), help="Last accessed article date. If not provided, will default to current date.")

# @misc
misc_parser = subparsers.add_parser("misc", help="Generate bibtex for miscellaneous document.")
misc_parser.add_argument("url", help="URL for document you would like to cite.")
misc_parser.add_argument("-k", "--key", default=str(uuid.uuid4()), help="Citation key for bibtex. If not provided, it will default to a UUID string.")
misc_parser.add_argument("-a", "--author", default="<Alter Please>", help="Author name(s). If not provided, will default to <Alter Please>")
misc_parser.add_argument("-r", "--release", default=utility.get_current_year(), help="Release date of the article. If not provided, will default to current year.")
misc_parser.add_argument("-l", "--last-accessed", default=utility.get_current_date(), help="Last accessed article date. If not provided, will default to current date.")

args = parser.parse_args()

match args.command:
    case "online":
        OnlineBibtex().get_bibtex(args.url, args.command, args.key, args.author, args.last_accessed, args.release)
    case "misc":
        MiscBibtext().get_bibtex(args.url, args.command, args.key, args.author, args.last_accessed, args.release)
    case _:
        "Error: No type provided"
