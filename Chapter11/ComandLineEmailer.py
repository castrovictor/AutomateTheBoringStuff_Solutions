"""Write a program that takes an email address and string of text on the com-
mand line and then, using Selenium, logs into your email account and
sends an email of the string to the provided address. (You might want to set
up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook
or Twitter account."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys


recipient = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]


#Open Gmail
browser = webdriver.Firefox()
browser.get('http://gmail.com/')

#Enter username
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('my_email')
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(3)

# Password Login
pass_elem = browser.find_element_by_name('password')
pass_elem.send_keys('my_pass')
pass_elem.send_keys(Keys.ENTER)
time.sleep(5)

#Click new email button
newEmail = browser.find_element_by_class_name('z0')
newEmail.click()
time.sleep(5)

# Write email to
to_elem = browser.find_element_by_name('to')
to_elem.send_keys(recipient)

# Write subject
subject_elem = browser.find_element_by_name('subjectbox')
subject_elem.send_keys(subject)

#Write and send email
message_elem = browser.find_element_by_id(':qp')
message_elem.send_keys(message + Keys.TAB + Keys.ENTER)
time.sleep(5)
browser.quit()
