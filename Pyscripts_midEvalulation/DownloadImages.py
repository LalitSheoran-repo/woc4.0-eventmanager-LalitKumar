# Aim of this script is to scrap the trek images from IndiaHike website using BeautifulSoup library and store
# them locally.

import requests
# requests library to make get requests

from bs4 import BeautifulSoup
# Beautiful soup library to parse the html data and get required information

url = "https://indiahikes.com/himalayan-monsoon-treks-photostory/#gref"
# url to get images

response_data = requests.get(url)

soup = BeautifulSoup(response_data.content, 'lxml')
# retrieved data is parse with BeautifulSoup using lxml parser

figureElement = soup.findAll('figure')
# All the intended images falls under figure tag in received html content

# All the image are accessed individually
for i, trek_image in enumerate(figureElement):

    with open("trek_image{}.jpg".format(i),'wb') as file:
        # file is opened in writeBinary mode as data retrieved from
        # request will be in binary form

        img_url = trek_image.img.attrs['data-lazy-src']
        # source of the image was stored in data-lazy-src attribute of image tag

        response = requests.get(img_url)
        file.write(response.content)
        # received data in binary form will be written and stored as file