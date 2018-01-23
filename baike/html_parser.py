import urlparse

import bs4
import re


class HtmlParser(object):

    def parser(self, url, cont):
        if url is None or cont is None:
            return None
        soup = bs4.BeautifulSoup(cont, "html.parser", from_encoding="utf-8")
        return self._get_new_urls(url, soup), self._get_new_data(url, soup)

    def _get_new_urls(self, url, soup):
        new_urls = set()
        # https://baike.baidu.com/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6
        links = soup.find_all("a", href=re.compile("/item/"))
        for link in links:
            short_link = link["href"]
            full_link = urlparse.urljoin(url, short_link)
            new_urls.add(full_link)
        return new_urls

    def _get_new_data(self, url, soup):
        result_data = {}
        result_data["url"] = url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        result_data["title"] = title_node.get_text()

        # <div class="para" label-module="para">Python
        para_node = soup.find("div", class_="para")
        result_data["para"] = para_node.get_text()
        return result_data