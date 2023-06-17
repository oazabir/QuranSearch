!#/usr/bin/python3
import urllib.request

translation = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/eng-abdelhaleem.json"
urllib.request.urlretrieve(translation, "abdelhaleem.json")
