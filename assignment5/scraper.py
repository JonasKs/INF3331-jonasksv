import re
import urllib.request
import urllib.error
from urllib.parse import urljoin

liste = []
urls = []

def find_emails(text):
    """A parser that takes a string and returns the e-mails found in it, according to the task specifications"""
    text = re.findall(r'([\w\.\+\-!#\$%&*/=\?\^_{|}~]+\@[\w]+[\w\.\+\-!#\$%&*/=\?\^_{|}~]*\.[a-z]{2,3})',text)
    return (text)

def find_hyperlinks(text):
    """A parser that takes a string and returns all the URL's found in it."""
    text = re.findall(r'<a\shref=[\"](http[s]?:\/\/[A-z0-9.\-~]+[\[A-z0-9\/.\-~]+]?)[\"]>',text)
    hyperlinks = ""
    for element in text:
        hyperlinks += "{}\n".format(element)
    return (hyperlinks) #return(text) instead if testing with test.py.. Inconsistensy is king

def all_the_emails(url, depth):
    """A scraper that takes an URL, fetches the URL, stores all E-mails to a list.
    When that is done, it finds all URL's, calls itself, appending list"""
    if depth > 0:
        try:
            with urllib.request.urlopen(url) as response: #Opens the url specified
                html = response.read() #reads url
                liste.extend(set(find_emails(str(html)))) #extends list (in top of file) with emails found
                urls = find_hyperlinks(str(html)) #Searches html for urls
                for element in urls.splitlines(): #Since my url function prints in lines, we iterate over those lines
                    newlink = urljoin(url, element)
                    all_the_emails(newlink,(depth-1)) #Recursive function. -1 on depth
        except urllib.error.HTTPError as e: #In case of HTTP error
            print("HTTP Error detected. Moving on")
        except urllib.error.URLError as e: #In case of URL error, e.g. cert error that I got
            print("Url error detected. Moving on")
    prefixes = ('//') #Prefix to remove the images
    for picture in liste[:]: #Iterates through the list and removes all words starting with //
        if picture.startswith(prefixes):
            liste.remove(picture)
    return(liste) #return the complete list of all e-mails (unique, we used set above)
url = "http://www.lucidtech.io"
depth = 2
print(all_the_emails(url,depth))

