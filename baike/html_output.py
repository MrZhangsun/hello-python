class HtmlOutput(object):

    def __init__(self):
        self.data_repo = []

    def append_data(self, data):
        if data is None:
            return
        self.data_repo.append(data)

    def output_html(self):
        fout = open("python.html", "w")
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta content='text/html'; charset=utf-8>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table border=5px>")
        for data in self.data_repo:
            fout.write("<tr>")
            fout.write("<td width=30%%, align='center', style='color:#0000ff'>%s</td>" % data['url'])
            fout.write("<td width=35%%, align='center', style='color:#00ffff'>%s</td>" % data['title'].encode("utf-8"))
            fout.write("<td width=35%%, align='center', style='color:#ff00ff'>%s</td>" % data['para'].encode("utf-8"))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")