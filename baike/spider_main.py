# coding=utf-8
from baike import url_manager, html_downloader, html_parser, html_output


class SpiderMain(object):
    # 构造方法
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self, url_root):
        count = 1
        self.urls.add_new_url(url_root)
        while self.urls.has_url():
            try:
                new_url = self.urls.next_url()
                print "count=%d, url=%s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.append_data(new_data)
                count = count + 1
                if count == 1000:
                    break
            except BaseException, e:
                print e
        self.output.output_html()


# main方法
# __name__：当文件被调用的时候该值为模块名（文件），当文件被执行的时候__name__就等于__main__，即：主函数
# Python代码的执行顺序是从上到下依次执行的，执行过程中除了定义的类和方法外，其他代码都会执行
if __name__ == "__main__":
    url_root = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(url_root)
