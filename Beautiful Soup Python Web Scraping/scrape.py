import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/CPUs-Processors/Category/ID-34?Tpk=processors'

# Opens the connection and grabs the page
uClient = uReq(my_url)

# Reads in all of the html of the page
page_html = uClient.read()

# Initiates HTML Parser
page_soup = soup(page_html, "html.parser")

# Prints specific parts of the HTML
# print(page_soup.h1)
# print(page_soup.body.span)

#Grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})
# print(containers)

# Outputs how many containers were found
# print(len(containers))

# =========== How to get info from one container===========
# == Prints more specific details as you get closer to finding the info you want
# = Chooses the first container to test on
# contain = containers[0]
# = Then goes deeper and deeper
# contain = contain.find("div","item-info")
# contain = contain.div
# contain = contain.a
# contain = contain.img

# == Above details can be combined for final to get the brand name:
# contain = containers[0].find("div","item-info").div.a.img
# brand = contain["title"]

# =========== Getting Product Title ===========

# == Gets all the item-title classes
# title_container = containers[0].findAll("a",{"class":"item-title"})
# == Gives you a list where the first element has the title as text
# title_container = title_container[0].text
# print(title_container[0].text)

# =========== Looping through the containers ===========

#To open a file:
filename = "products.csv"
f = open(filename,"w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.find("div","item-info").div.a.img["title"]
    title = container.findAll("a",{"class":"item-title"})[0].text
    shipping = container.findAll("li",{"class":"price-ship"})[0].text.strip()
    # print("Brand: " + brand)
    # print("Title: " + title)
    # print("Shipping: " + shipping)

    #Writes to the file
    f.write(brand + "," + title.replace(",","|") + "," + shipping + "\n")

# Closes the file
f.close()
# Closes the webpage connection
uClient.close()