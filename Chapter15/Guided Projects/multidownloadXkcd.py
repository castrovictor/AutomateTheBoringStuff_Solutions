#! python3
# multipledownloadXkcd.py - Doenloads XKCD comics using multiple threads

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)

def downloadXckd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        print('Downloading page https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the url of the comic image
        comicElem = soup.select('#comic img')
        if comicElem = []:
            print('Could not find the comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the imagt to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.wirte(chunk)
            imageFile.close()

# Create and start the Thread object

# a list of all the Thread objects
downloadThreads = []
# loops 14 times, create 14 threads
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXckd, args=(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
