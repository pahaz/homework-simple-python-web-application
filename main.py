from wsgiref.simple_server import make_server

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


def run(host='', port=31338):
    print("It's work! Visit http://{host}:{port}/".format(
        host=host or 'localhost', 
        port=port))
    httpd = make_server(host, port, application)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
