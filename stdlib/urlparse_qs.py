from urllib.parse import parse_qs, urlparse


# https://tools.ietf.org/html/rfc3986

url = "http://user:password@host:80/pathseg1/pathseg2;param1;param2=v1,v2?field1=value1&field2=value2#fragment"
print('urlstring:', url)

parsed_url = urlparse(url)
print('parsed:', parsed_url)

print("scheme:", parsed_url.scheme)
print("netloc:", parsed_url.netloc)
print("username:", parsed_url.username)
print("password:", parsed_url.password)
print("hostname:", parsed_url.hostname)
print("port:", parsed_url.port)
print("path:", parsed_url.path)
print("params:", parsed_url.params)
print("query:", parsed_url.query)
print("fragment:", parsed_url.fragment)

# & or ; separator
print("parsed query string:", parse_qs(parsed_url.query))
