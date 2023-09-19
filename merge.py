# script under MIT license, Michael Scherer, 2023
# see the LICENSE file 

import sys
import feedparser
from feedgen.feed import FeedGenerator
import datetime

list_of_rss = sys.argv[1]
dest = sys.argv[2]

with open(list_of_rss, 'r') as l:
    items = []
    for f in l.readlines():
        try:
           feed = feedparser.parse(f)
        except e:
           # TODO fix uglyness later
           print(e) 
        for entry in feed.entries:
            if " AI " in entry.summary or " AI " in entry.title:
                items.append(entry)

fg = FeedGenerator()
fg.author({'name': "Ethan Hunt"})
fg.title('Atom feed for next.redhat.com')
fg.id("next-rss")

for i in items:
    fe = fg.add_entry()
    fe.title(i.title)
    fe.id(i['id'])
    fe.content(i.summary, type='xhtml')

fg.atom_file(dest)
