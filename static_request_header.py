from request_header import RequestHeader

class StaticRequestHeader(metaclass=RequestHeader):
  def __init__(self):
    self.request_header = []

  def append(self, header: dict):
    self.request_header.append(header)

  def to_list(self):
      return self.request_header

def create_static_request_header_from_string(_headers: String):
  static_request_header = StaticRequestHeader()

  for line in _headers.splitlines():
    header_key = re.search('(.*?):', line).group(0)
    _header_value = header_key[header_key+1:]
    header_value = ""
    if _header_value.length > 0
      header_value = _header_value

    header = {header_key: header_value}
    static_request_header.append(header)

  return header
