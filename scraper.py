from html.parser import HTMLParser
from urllib.request import urlopen
from quanta import Article

class QuantaScraper(HTMLParser):
    """
    QuantaScraper gets all of the text off of an article from quantamagazine.com
    :return an Article object
    """
    def __init__(self):
        super().__init__()
        self.last_tag = None
        self._class = None
        self._title_class = "ml025 h3 noe mv0"
        self._author_class = "byline__author uppercase kern light small"
        self._date_class = "h6 o6 mv1 pv025"
        self._content_class = "post__content wysiwyg p theme__anchors--underline"
        self._data_tags = ["a", "p", "em"]
        self.article = Article()

    def handle_starttag(self, tag, attrs):
        try:
            if tag in ["p", "span", "h1", "div"] and attrs[0][0] == "class":
                self._class = attrs[0][1]
        except:
            pass
        self.last_tag = tag

    def handle_endtag(self, tag):
        if tag == "p" and self._class == self._content_class:
            self.article.add_contents("\n\n\t")

    def handle_data(self, data):
        if self._class == self._title_class:
            self.article.set_title(data)
        if self._class == self._author_class:
            self.article.set_author(data)
        if self._class == self._date_class:
            self.article.set_date(data)
        if self._class == self._content_class and self.last_tag in self._data_tags:
            self.article.add_contents(data.replace('\n', ''))

def main():
    scraper = QuantaScraper()
    article_url = "https://www.quantamagazine.org/artificial-neural-nets-grow-brainlike-navigation-cells-20180509/"
    response = urlopen(article_url)
    if response.getheader('Content-Type').split(";")[0] == 'text/html':
        html_bytes = response.read()
        html_string = html_bytes.decode("utf-8")
        scraper.feed(html_string)
    scraper.article.save()

if __name__ == "__main__":
    main()