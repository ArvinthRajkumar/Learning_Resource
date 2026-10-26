from urllib.parse import urlparse, parse_qs, urlencode, quote, urljoin, urlunparse
u = urlparse("https://user@example.com:8443/search/items?q=red+shoes&page=2&tag=a&tag=b#top")
print(u.scheme, u.hostname, u.port, u.path, u.fragment)
print(parse_qs(u.query))
print(urlencode({"q": "red shoes & socks", "page": 3}), "|", quote("a b/c?d", safe=""))
print(urljoin("https://example.com/docs/guide/", "../api/v1"), "|", urlunparse(("https", "example.com", "/x", "", "a=1", "")))
