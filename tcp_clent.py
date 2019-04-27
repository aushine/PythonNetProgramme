import re
r = re.match(r"[^/]+(/[^?* ]*)", "GET /gitbook/fonts/fontawesome/fontawesome-webfont.woff?v=4.1.0 HTTP/1.1")
print(r.group(1))