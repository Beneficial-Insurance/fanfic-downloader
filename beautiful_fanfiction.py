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
def download_fanfic():
    res = requests.get(verify_url('Please enter url for the fanfic. \n'))
    #Check that the download works properly
    res.raise_for_status()
    #Create a Beautiful Soup object, uses ibuilt (I think?) Html parser.
    fanfiction_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return fanfiction_soup
#Rips out all the text within the .storytextp div
def get_text():
    print(type(fanfiction_soup))
    print_text = str(fanfiction_soup.select('.storytextp p'))
    #print(fanfiction_text)
    #This is the regex to find all <p> and <p blah blah class and code> tags '<p([^>])*>'
    print_text = re.sub('\[?<p([^>])*>', '    ', print_text)
    print_text = re.sub('</p>]?,?', '\n\n', print_text)
    print_text = re.sub('<.*[^ ]>', '', print_text)
    print(print_text)
    return print_text
#Save file as... ./fanfic
def save_file():
    text_file = open("HarryAndDaphne.txt", "w")
    n = text_file.write(print_text)
    text_file.close
#I suppose this is where init main() goes in c?
fanfiction_soup = download_fanfic()
print_text = get_text()
save_file()
