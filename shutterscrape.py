from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time
import ssl
from PIL import Image

# For python3
from urllib.request import urlretrieve
import tkinter, tkinter.constants, tkinter.filedialog
import os

def askDialog():
    return tkinter.filedialog.askdirectory()

def inp(text):
    return input(text)

ssl._create_default_https_context = ssl._create_unverified_context


def remove_border(path):
    im = Image.open(path)
    w, h = im.size
    im = im.crop((0,0,w, h - 20))
    w, h = im.size

    if w == 260 and h == 260:
        im.save(path)
    else:
        os.remove(path)

def imagescrape():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(executable_path="/home/koshy/Desktop/projects/shutterscrape/chromedriver", options=chrome_options)
        driver.maximize_window()
        for i in range(1001, searchPage + 1):
            url = "https://www.shutterstock.com/search?searchterm=" + searchTerm + "&sort=popular&image_type=" + image_type + "&search_source=base_landing_page&language=en&page=" + str(i)
            print(url)
            driver.get(url)
            data = driver.page_source
            # data = driver.execute_script("return document.documentElement.ousterHTML")
            # print(data)
            print("Page " + str(i))
            scraper = BeautifulSoup(data, "lxml")
            img_container = scraper.find_all("img", {"class":"z_h_a z_h_b"})
            # print(img_container)
            for j in range(0, len(img_container)-1):
                img_src = img_container[j].get("src")
                name = img_src.rsplit("/", 1)[-1]
                try:
                    urlretrieve(img_src, os.path.join(scrape_directory, os.path.basename(img_src)))
                    remove_border(os.path.join(scrape_directory, os.path.basename(img_src)))
                    print("Scraped " + name)
                except Exception as e:
                    print(e)
        driver.close()
    except Exception as e:
        print(e)

# print("ShutterScrape v1.1")


while True:
    # while True:
    #     print("Please select a directory to save your scraped files.")
    #     scrape_directory = askDialog()
    #     if scrape_directory == None or scrape_directory == "":
    #         print("You must select a directory to save your scraped files.")
    #         continue
    #     break
    scrape_directory = "/home/koshy/Desktop/projects/shutterscrape/data"
    # while True:
    #     image_type = inp("Select image type ('a' for all or 'p' for photo): ")
    #     if image_type != "a" and image_type != "p":
    #         print("You must select 'a' for all or 'p' for photo.")
    #         continue
    #     break
    # if image_type == 'p':
    #     image_type = 'photo'
    # else:
    image_type = 'all'


    # while True:
        
    #     searchCount = int(inp("Number of search terms: "))
    #     if searchCount < 1:
    #         print("You must have at least one search term.")
    #         continue
    #     elif searchCount == 1:
    #         searchTerm = inp("Search term: ")
    #     else:
    #         searchTerm = inp("Search term 1: ")
    #         for i in range (1, searchCount):
    #             searchTermPart = inp("Search term " + str(i + 1) + ": ")
    #             searchTerm += "+" + searchTermPart
    #     break
    
    # while True:
    #     searchPage = int(input("Number of pages to scrape: "))
    #     if searchPage < 1:
    #         print("You must have scrape at least one page.")
    #         continue
    #     break
    searchCount = 2
    searchTerm = "floral+patterns"
    searchPage = 2000
    imagescrape()
    # print("Scraping complete.")
    # restartScrape = inp("Keep scraping? ('y' for yes or 'n' for no) ")
    # if restartScrape == "n":
        # print("Scraping ended.")
    break
