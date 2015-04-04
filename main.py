from __future__ import unicode_literals, print_function, generators, division
from collections import Iterable
import wsgiref.util
import wsgiref.validate
import sys

__author__ = 'pahaz'
PY3 = sys.version_info[0] == 3

# MOCK environ
mock_environ = {}
wsgiref.util.setup_testing_defaults(mock_environ)


# MOCK start_response
is_start_response_call = False
start_response_status = None
start_response_headers = None


def mock_start_response(status, headers):
    global is_start_response_call
    global start_response_headers, start_response_status
    is_start_response_call = True
    start_response_status = status
    start_response_headers = headers

# IMPORT APP
from main import application

# INITIALIZE
if PY3:
    application = wsgiref.validate.validator(application)
result = application(mock_environ, mock_start_response)

# ASSERTS
assert isinstance(result, Iterable), "application() return isn't iterable obj"
assert is_start_response_call, "start_response isn't called"
assert start_response_status == "200 OK", "start_response status != '200 OK'"

# tearDown
if hasattr(result, 'close'):
    result.close()
