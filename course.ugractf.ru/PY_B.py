import requests

r = requests.get("https://redirect.course.ugractf.ru/e996935903f107a4/")
print(r.text)

while r.status_code == 200:
    r = requests.get("https://" + r.text[10:])
    print(r.text)
