from flask import Flask, redirect, url_for, request, Response
import urllib
import urllib.request as urllib2

app = Flask(__name__)

# Change to redirector
redirector = "your.domain.com"
protocol = 'http'


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def hello(path):
    header = ""
    for key, value in request.headers.items():
        header += "%s: %s" % (key, value)

    url = protocol + '://' + redirector + '/' + path + "?" + request.query_string.decode("UTF-8")
    content = ""
    try:
        req = urllib2.Request(url)
        for key, value in request.headers.items():
            req.add_header(str(key), str(value))

        if request.method == "POST":
            req.data = request.data

        resp = urllib2.urlopen(req)
        content = Response(resp.read())

        for key, value in resp.info().items():
            content.headers[key] = value

        return content
    except urllib2.URLError:
        return "next gen"

    return content
