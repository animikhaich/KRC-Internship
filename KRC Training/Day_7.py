######################################################
## Internship @ KRC: DAY 7                          ##
## ANIMIKH AICH                                     ##
## RNS Institute of Technology, Bengaluru, India    ##
######################################################

# Python Files operation

import os

f = open('Input.txt','w')
line1 = "This is the first line to be written in the file \n"
f.write(line1)
line2 = "This is the Second line to be written in the file \n"
f.write(line2)
num = 28
line3 = "This line contains a number %d \n" %num
f.write(line3)
line4 = "This line contains a number using format Operator {} \n".format(num)
f.write(line4)
f.close()

print(os.getcwd())  # Prints out the Present working directory in the console
pwd = os.getcwd()
f = open('Input.txt','a')      #In append mode
f.write('Present working directory is: {} \n'.format(pwd))
f.write('Checking if the "Input.txt" exists or not: {} \n'.format(os.path.exists('Input.txt')))
f.write('\n\n----------------------------------------END OF FILE----------------------------------------')
f.close()

f = open('Input.txt','r')
file_contents = f.read()
print('File Contents: \n\n', file_contents)
f.close()


import dbm
db = dbm.open('Database','c')       # the 'c' is to create a file if it does not already exist
db['Intern 1'] = 'Animikh Aich'
db['Intern 2'] = 'Akhilesh V'
db['Intern 3'] = 'Himanshu'
db['Intern 4'] = 'Bipin'
db['Intern 5'] = 'Meghana B'
db['Intern 6'] = 'Akshaya'
db['Intern 7'] = 'Aishwarya'
db['Intern 8'] = 'Namratha'
db.close()

db = dbm.open('Database','c')
for i in range (1,9):
    string = 'Intern ' + str(i)
    print(db[string],end='    ')
db.close()


# Write a function called sed that takes as arguments a pattern string, a replacement
# string, and two filenames; it should read the first file and write the contents into the
# second file (creating it if necessary). If the pattern string appears anywhere in the file,
# it should be replaced with the replacement string.
# If an error occurs while opening, reading, writing or closing files, your program
# should catch the exception, print an error message, and exit.

def sed (pattern, replacement, ip, op):
    src = open(ip + '.txt', 'r')
    dst = open(op + '.txt', 'w')

    for lines in src:
        replace = lines.replace(pattern,replacement)
        dst.write(replace)

    src.close()
    dst.close()

sed('file', 'document', 'Input', 'Output')
print('\n\n\n\n\n\n\n')

# Secret Think Python Exercise
# If you are reading this, you are probably working on the urllib exercise from Think Python.
# Next, you should read the documentation of the urllib module at http://docs.python.org/lib/module-urllib.html
# Then go to www.uszip.com, which provides information about every zip code in the country. For example, the URL
# http://www.uszip.com/zip/02492
# provides information about Needham MA, including population, longitude and latitude, etc.
# Write a program that prompts the user for a zip code and prints the name and population of the corresponding town.
# Note: the text you get from uszip.com is in HTML, the language most web pages are written in. Even if you don't know HTML, you should be able to extract the information you are looking for.
# By the way, your program is an example of a "screen scraper." You can read more about this term at
# http://wikipedia.org/wiki/Screen_scraping


import urllib.request
from bs4 import BeautifulSoup as soup

# conn = urllib.request.urlopen('http://thinkpython.com/secret.html')
# page = soup(conn, 'html5lib')
# print(page.prettify())

# The actual Program starts here

base_url = 'http://www.uszip.com/zip/'
zip = input('Enter desired zip code: ')
zip_url = str(zip)

final_url = base_url + zip_url
raw_html = urllib.request.urlopen(final_url)
html = soup(raw_html, 'html5lib')

name = html.find("div",{"id":"page-container"}). \
    find("div",{"class":"container"}).find("div",{"class":"row"}). \
    div.find("div",{"class":"row"}).div.findAll('div')[4].hgroup.h2.text

population = html.find("div",{"id":"page-container"}). \
    find("div",{"class":"container"}).find("div",{"class":"row"}). \
    div.find("div",{"class":"row"}).div.findAll('div')[4].dl.dd.text

print('The Name of the city is: {}'.format(name))
print('Population of the city is: {}'.format(population))