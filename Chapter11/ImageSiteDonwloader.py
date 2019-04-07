"""Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that has
a search feature."""

#Note: I chose Flickr

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests, os, bs4, sys, time

keyword = sys.argv[1]
nImg = int(sys.argv[2])


def check_load_button():
    try:
        browser.find_element_by_class_name('alt')
    except NoSuchElementException:
        return False
    return True

#Open search page with the keyword in Flickr, only images
browser = webdriver.Firefox()
url = 'https://www.flickr.com/search/?text=' + keyword + '&media=photos'
browser.get(url)

htmlElem = browser.find_element_by_tag_name('html')

#Load at least nImg images
pics = browser.find_elements_by_class_name("overlay")
while len(pics) < nImg:
    time.sleep(5)
    if(check_load_button()):
        button = browser.find_element_by_class_name('alt')
        button.click()
    else:
        htmlElem.send_keys(Keys.END)

    #Update list
    pics = browser.find_elements_by_class_name("overlay")


#Using BeautifulSoup to download the images
folder = "flickr_" + keyword
os.makedirs(folder, exist_ok=True)

#Iterate through all images
contador = 0
for elem in pics:
    currentUrl = elem.get_attribute('href')
    res = requests.get(currentUrl)
    try:
        res.raise_for_status()
    except Exception as exc:
        print("Problem with current img, skipping to next one")
        continue

    soup = bs4.BeautifulSoup(res.text, features = "html.parser")
    #Find img src by class
    imgHtml = soup.find_all("img", class_="main-photo is-hidden")
    if imgHtml == []:
        print('Could not find the image, skipping...')
    else:
        imgUrl = imgHtml[0].get('src')
        imgUrl = 'https:' + imgUrl
        #print("Getting " + imgUrl)
        res = requests.get(imgUrl)

        try:
            res = requests.get(imgUrl)
            res.raise_for_status()
            correct_url = True
        except:
            print("Invalid url, skipping..")
            continue

        #Save image to folder
        name = folder + "/" + str(contador)
        print("Saving " + name)
        imageFile = open(name, 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        contador += 1

print("Done.")
browser.quit()
