import bs4
import sys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def getInfo():
    # Opens the connection and grabs the page
    try:
        # Reads in all of the html of the page

        url = "D:\\Documents\\GitHub\\Miscellaneous_Projects\\Plex Movie Scraper\\plexCode.HTML"
        page = open(url)
        page_soup = soup(page.read())

        # Gets movie title
        movies = page_soup.findAll("div", {"class": "MetadataPosterCell-titleContainer-24DI63"})
        for movie in movies:
            title = movie.a
            title = title["title"]
            print(title)


    except KeyboardInterrupt:
        print("Someone closed the program")

print("Opening CSV file...")

# Creates and opens the CSV file
try:
    filename = "plexMoviesList.csv"
    f = open(filename,"w")
except FileExistsError as e:
    print("ERROR: File not found")
    sys.exit()
except PermissionError as e:
    print("ERROR: Permission denied: File may need to be closed")
    sys.exit()

# Writes the CSV file's headers
headers = "title,year,rating\n"
f.write(headers)

print("Writing to CSV file...")
getInfo()

print("Finished writing to CSV file")

f.close()

print("COMPLETE: Program has finished running")
