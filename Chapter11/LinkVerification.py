"""Write a program that, given the URL of a web page, will attempt to down-
load every linked page on the page. The program should flag any pages
that have a 404 “Not Found” status code and print them out as broken links."""

import requests, bs4
import bs4

url = input('Website to check 404 links: ')

res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem with the website")
    exit()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
print("Number of links: " + str(len(links)))
brokenLinks = []   # List of links that lead to a 404 page

for link in links:
    try:
        currentUrl = link['href']
        if currentUrl.startswith('http'):
            to_check = currentUrl

        elif currentUrl.startswith('https'):
            to_check = currentUrl

        elif currentUrl.startswith('//'):
            to_check = 'https:' + currentUrl

        elif currentUrl.startswith('#'):
            to_check = url + currentUrl

        result = requests.get(to_check)

        if result.status_code == 404:
            brokenLinks.append(to_check)

    except:
        continue

print("This website has " + str(len(brokenLinks)) + "broken links")
