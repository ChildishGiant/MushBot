from lxml import html
import requests

def run(client, msg, args):
    page = requests.get('http://www.touretteshero.com/safe/tics/?random=true')
    tree = html.fromstring(page.content)
    tics = tree.xpath('//a[@class="tic-title-link"]/text()')
    firstSaid = tree.xpath('//li[@class="ticmeta_startyear"]/text()')
    print("{0} - {1}. Please support Touretteshero at http://www.touretteshero.com/donate/".format(tics[0].encode("utf-8"),firstSaid[0]))
