from bibtex import Bibtex

class OnlineBibtex(Bibtex):
    def __init__(self):
        super().__init__()
        self.arxiv_search_object = self.get_arxiv_search_object()
    
    def get_bibtex(self, url):
        if "https://arxiv.org" in url:
            self.arxiv_search_object.arxiv_to_bibtex(url)
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
        