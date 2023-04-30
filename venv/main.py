import requests
import sys
import site
import webbrowser

print(sys.prefix)
print(site.getsitepackages())


gugel = 'https://www.google.com'
response = requests.get(gugel)
if response.status_code == 200:
    webbrowser.open(gugel)
