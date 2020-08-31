
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


def scrape():

    first_url="https://mars.nasa.gov/news/"
    response = requests.get(first_url)
    newsoup=bs(response.text,'html.parser')

    title=newsoup.title.string
    new_p=newsoup.p.string

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    secondurl="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(secondurl)


    for x in range(1):
        html=browser.html
        soup=bs(html,"html.parser")
        images=soup.find_all('img',class_="fancybox-image")
    #imgsrc=[image['src'] for image in images]
    #featured_image_url=secondurl+imgsrc[0]
    img_src = "/spaceimages/images/mediumsize/PIA19952_ip.jpg"
    featured_image_url = 'https://www.jpl.nasa.gov' + img_src

    third_url="https://space-facts.com/mars/"
    table=pd.read_html(third_url)
    table=table[0]
    html_table = table.to_html()

    fourth_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]
    mars_dict = {
            "news_title":title,
            "news_paragraph":new_p,
            "featured_image_url":featured_image_url,
            "table": html_table,
            "hemisphere_image_urls":hemisphere_image_urls
        }
    browser.quit()
    return mars_dict








