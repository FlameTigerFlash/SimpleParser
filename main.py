import requests
from bs4 import BeautifulSoup

counter = 1

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/97.0.4692.71 Safari/537.36"}

for pg in range(1, 44):
    url = f"https://leetcode.com/problemset/all/?page={pg}"
    page = requests.get(url, headers=headers).text
    doc = BeautifulSoup(page, "html.parser")
    tasks = doc.find_all(class_="h-5 hover:text-primary-s dark:hover:text-dark-primary-s")

    for task in tasks:
        print(task.text)
print(f"Всего задач {counter}.")
