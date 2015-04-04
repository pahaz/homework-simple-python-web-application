from __future__ import unicode_literals, print_function, generators, division

__author__ = 'pahaz'


def application(environ, start_response):
    assert environ.get('PATH_INFO') is not None, "environ['PATH_INFO'] is None"

    status = "200 OK"
    headers = [('Content-type', 'text/html; charset=utf-8')]
    body = """<!DOCTYPE html>
    <h1>Example-mini-application</h1>
    """

    start_response(status, headers)
    return [body.encode('utf-8')]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    PORT = 31338
    print("It's work! Visit http://localhost:{0}/".format(PORT))
    HTTPD = make_server('', PORT, application)
    HTTPD.serve_forever()
