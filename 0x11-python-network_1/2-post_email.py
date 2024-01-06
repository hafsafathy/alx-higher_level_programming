#!/usr/bin/python3
""" sends a POST request to the passed URL with the email"""
if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.req.Request(url, data)
    with urllib.req.urlopen(req) as response:
        print(response.read().decode("utf-8"))
