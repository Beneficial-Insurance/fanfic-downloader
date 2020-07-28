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
        verify = re.match('^(https://www.fanfiction.net/s/)(\d)*.*', fanfic_url)
        #verify = re.match('(\d)', fanfic_url)
        if verify:
            return fanfic_url
            break
        else:
            print('The Url was not valid')
#Download Fanfic page
res = requests.get(verify_url('Please enter url for the fanfic'))
#Check that the download works properly
res.raise_for_status()
#Create a Beautiful Soup object, uses ibuilt (I think?) Html parser.
fanfiction_soup = bs4.BeautifulSoup(res.text, 'html.parser')
#Rips out all the text within the .storytextp div
text = fanfiction_soup.select('.storytextp p')
#Prints the fanfiction.
#print(text)
#WTF is this actually?
#print(type(text))
#It's a class. God damnit, they look really useful. I'll have to see about incorperating them later.
total_length_of_fic = len(text)
fanfiction_text = str(text)
print(fanfiction_text)
print_text = fanfiction_text.replace('<p>', '    ')
print_text = print_text.replace('</p>,', '\n\n')
print(print_text)
#Save file as... ./fanfic
text_file = open("HarryAndDaphne.txt", "w")
n = text_file.write(print_text)
text_file.close
