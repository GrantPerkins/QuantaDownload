
class Article:
    """This object holds all of the information to a given quanta article"""

    def __init__(self):
        self.title = None
        self.author = None
        self.date = None
        self.contents = ""

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_date(self, date):
        self.date = date

    def add_contents(self, contents):
        self.contents += contents

    def save(self):
        with open("C:/Users/HP/Quanta/"+self.title+".txt", "w+") as f:
            f.write(self.title+"\n")
            f.write(self.author+"\n")
            f.write(self.date+"\n\n\t")
            f.write(self.contents)

