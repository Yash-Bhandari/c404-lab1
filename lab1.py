import requests

# print(requests.__version__)

requests.get("http://google.com/")

source = requests.get(
    "https://raw.githubusercontent.com/Yash-Bhandari/c404-lab1/main/lab1.py"
)
print(source.text)
