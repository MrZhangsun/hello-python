class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.ord_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.ord_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None and len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_url(self):
        return len(self.new_urls) != 0

    def next_url(self):
        if not self.has_url():
            return None
        next_url = self.new_urls.pop()
        self.ord_urls.add(next_url)
        return next_url
