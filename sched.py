#! /usr/bin/python

from lxml import html
import requests
import sys

url = sys.argv[1]

hmap = {
"pony-american": "(Po) American",
"pony-national": "(Po) National",
"bronco-american": "(B) American",
"bronco-national": "(B) National",
"mustang-american": "(M) American",
"mustang-national": "(M) National",
"pinto-american": "(Pi) American",
"pinto-national": "(Pi) National",
}

header = ["CV PONY Baseball",hmap[url] + " Division",hmap[url] + " Division-Group","NA"]

divisionpage = requests.get("http://cvinterleague.clubsetup.com/division/%s" % (url))
divisiontree = html.fromstring(divisionpage.content)

teams = ["http://cvinterleague.clubsetup.com/" + x.get('href') for x in divisiontree.xpath('//a[contains(@href,\'schedule_results\')]')]

for teamurl in teams: 
  page = requests.get(teamurl)
  tree = html.fromstring(page.content)

  schedtable = tree.xpath('//div[@id="content-content"]/table')
  data = [x for x in schedtable[0].xpath('tbody/tr')]
  for data in [[y.text_content() for y in x.xpath('td')] for x in schedtable[0].xpath('tbody/tr')]:
    date = (data[0].split())[1]
    print ','.join(header + [data[3],data[5],date])
