from request_header import RequestHeader

from request import request

class FetchResponse:
  def __init__(self):
    self.request_header = None
    self.response_header = None
    self.response_body = None

  def set_request_header(_request_header: RequestHeader):
    self.request_header = _request_header

  def set_response_header(_response_header: String):
    self.response_header = _response_header

  def set_response_body(_response_body: String):
    self.response_body = _response_body

def fetch(_request_header: RequestHeader):
  # prepare the session object to store all session headers
  requests.Session()

  # get the target url
  url = _request_header.getRequestUrl()

  # take the RequestHeader object and put all the headers into the session
  [ session.headers.update(header_dict) for header_dict in _request_header.to_list() ]

  # send the request

  session_response = session.get(url)

  fetch_response = FetchResponse()
  fetch_response.set_request_header(_request_header)
  fetch_response.set_response_header(session_response.headers)
  fech_response.set_response_body(session_response.body)

  return fetch_response
