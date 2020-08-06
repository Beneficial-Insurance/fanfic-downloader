#finds the title using regex
import re, os
text_to_search = open('HarryAndDaphne.txt', 'r')
text_as_string = str(text_to_search)
a = re.search("""<b class=["']xcontrast_txt['"]>(.[^<(.){1}b>])*<(.){1}b>""", text_as_string)
print(text_to_search)
print(type(a))
print(a)
print(str(a))
