import requests
from lxml import html


def parse_ukd_data():
    url = "https://ukd.edu.ua/"
    response = requests.get(url)
    tree = html.fromstring(response.content)
    specializations = tree.xpath('//*[@id="block-menyuukhederi"]/li[1]/div/div/div[2]/div/ul[1]/li')
    for spec in specializations:
        print(spec.text_content().strip())


parse_ukd_data()
