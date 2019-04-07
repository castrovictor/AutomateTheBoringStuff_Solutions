"""Write a program that checks the websites of several web comics and auto-
matically downloads the images if the comic was updated since the program’s
last visit. Your operating system’s scheduler (Scheduled Tasks on Windows,
launchd on OS X, and cron on Linux) can run your Python program once
a day. The Python program itself can download the comic and then copy
it to your desktop so that it is easy to find."""

import os, datetime, bs4, requests

def checkXkcd(lastUrl):
    # Download all XKCD comic released after the given url
    url = 'https://xkcd.com/'

    #Get latest comic URl to compare with lastUrl
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.txt, features="html.parser")
    prevImg = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

    #If the url is not the same, start downloading from lastUrl
    if url == lastUrl:
         print('No new XKCD comics have been published since last check')
    else:
        url = lastUrl
        while not url.endswith('#'):
            #Download the page
            #print('Downloading page %s...' % url)
            res = requests.get(url)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, features= "html.parser")
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Could not find the comic image.')
            else:
                comicUrl = 'http:' + comicElem[0].get('src')
                # Download the image
                print('Downloading image %s...' % (comicUrl))

                correct_url = False
                try:
                    res = requests.get(comicUrl)
                    res.raise_for_status()
                    correct_url = True
                except:
                    print("Invalid url, skipping..")

                if(correct_url):
                    # Save the image to ./xkcd.
                    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                    for chunk in res.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()

            # Get the Prev button's url.
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')

    # Return url of last comic downloaded without /#
    return url[:-2]



os.makedirs('XkcdComics', exist_ok=True)
# File containing latest comic URL checked

# File containing latest comic URL checked. It must exists and have last comic information
with open('./XkcdComics/last_downloaded.txt') as f:
    info = f.read().splitlines()
    date = info[0]
    lastXkcd = info[1]

date = datetime.datetime.now().strftime('%H:%M:%S on %d/%m/%Y')
print('Last comic check = ' + date)

# Run functions and rewrite file with 'new' URLs
xkcdUrl = checkXkcd(lastXkcd)

with open('./XkcdComics/last_downloaded.txt', 'w') as f:
    f.write(date + '\n')
    f.write(xkcdUrl + '\n')

print('Done.')
