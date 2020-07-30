#A fanfiction downloader.
#Import necessary modules
import requests, bs4, re, os
#This is the basic url I'm trying to link
#https://www.fanfiction.net/s/11697407/1/Contractual-Invalidation
#The segments are as such:
#https://www.fanfiction.net/s/ (All of this is the same... unless they threw in the review thing for some reason)
#11697407 (The story ID)
#/1/ (The chapter number)
#Contractual-Invalidation (The fic name... irrelevent)
def verify_url(message):
    while True:
        fanfic_url = str(input(message))
        #Verifies that the start of the script is https://blah blah/story id/title
        verify = re.match('^(https://www.fanfiction.net/s/)(\d)*.*',fanfic_url)
        #verify = re.match('(\d)', fanfic_url)
        if verify:
            return fanfic_url
            break
        else:
            print('The Url was not valid')
#Download Fanfic page
def download_fanfic(message):
    res = requests.get(verify_url(str(message)))
    #Check that the download url goes to a page that returns the 200 ok status (The page exists)
    #Unfortunately, every ffn page returns 200 okay, that site was coded by a fuckwit. I'm gonna have to find a different method to make sure fanfic exists
    if res.status_code == requests.codes.ok:
        #Create a Beautiful Soup object, uses ibuilt (I think?) Html parser.
        fanfiction_soup = bs4.BeautifulSoup(res.text, 'html.parser')
        #Do I have to do this or can regex search whatever the data is before I turn it into a string? I have no clue, and I don't care.
        check = str((res.text.encode('utf8')))
        #Searches for the Story Not Found text that happens when a fic is requested that doesn't exist. There is probably a better way to do this but eh
        if re.search('Story Not Found', check) is None:
            print('Hi')
            return fanfiction_soup
        else:
            print('ERROR The URL requested does not have a fanfic on it.\nStopping Download')
            exit()
    else:
        print('Something wen\'t wrong.')
        exit()
#Rips out all the text within the .storytextp div
def get_text():
    print_text = str(fanfiction_soup.select('.storytextp p'))
    #This is the regex to find all <p> and <p blah blah class and code> tags '<p([^>])*>'
    print_text = re.sub('\[?<p([^>])*>', '    ', print_text)
    #This regex finds all </p> tags that are then replaced by \n\n
    print_text = re.sub('</p>]?,?', '\n\n', print_text)
    #Finds all the inline style that ffn uses. What are they from, the dark ages?
    print_text = re.sub('<.*[^ ]>', '', print_text)
    return print_text
def get_title():
    print_title = str(fanfiction_soup.select(''))
#Save file as... ./fanfic
def save_file():
    text_file = open("HarryAndDaphne.txt", "w")
    n = text_file.write(print_text)
    text_file.close
#I suppose this is where init main() goes in c?
fanfiction_soup = download_fanfic('Please enter the url of the fanfic that you want to download \n')
print_text = get_text()
save_file()
