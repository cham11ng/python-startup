# URL Library Module

from urllib.request import urlopen

x = urlopen("https://www.google.com")

print(x.read())
