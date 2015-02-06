#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
nasap - news as simple as possible

This is a simple tool to fetch full text posts based on a RSS/Atom feed and
store it as a simple textfile to later view it with a tool of your choice.

git repo: https://github.com/phavx/nasap/

Information about AUTHORS, TODO and LICENSE can be found in the respective file
"""

# standard libs
from io import open
from os import environ, makedirs, path
from urllib2 import urlopen
from sys import argv, exit
from time import gmtime, strftime

# external dependencies
import feedparser
import html2text
from readability.readability import Document

# functions
def error(msg, code):
    """prints an error message and exits the program with the given code"""
    print msg
    exit(code)

def current_date_time():
    """create current date and time in case the feed item doesn't provide it"""
    return strftime("%Y-%m-%d", gmtime()), strftime("%H:%M", gmtime())

def check_create_dir(directory):
    """if the passed directory doesn't exist, try to create it"""
    if path.exists(directory):
        if path.isdir(directory):
            return True
        else:
            return False
    else:
        makedirs(directory)
        return True

# for now nasap doesn't have a config file or runtime options, so make changes
# in this section if needed
#
# the basedir where all feed items will be stored
NEWS_DIR = environ["HOME"] + "/news"


# some basic sanity checks
if not check_create_dir(NEWS_DIR):
    error("Error: %s exists, but isn't a directory!" % NEWS_DIR, 1)

if len(argv) != 2:
    exit(1)


URL = argv[1]
REFERRER = "/".join(URL.split("/")[:3])
FEED = feedparser.parse(URL, referrer=REFERRER)

# if we don't already have a directory for this feed, create it
FEED_DIR = NEWS_DIR + "/" + FEED.feed.title
if not check_create_dir(FEED_DIR):
    error("Error: feed directory %s could not be created." % FEED_DIR, 1)

# loop over the feed's items and process them
for i in range(0, len(FEED["entries"])):
    html = Document(urlopen(FEED.entries[i].link).read()).summary()

    # stripping html tags and limiting the width to 80 characters
    h = html2text.HTML2Text(bodywidth=80)
    h.ignore_images = True
    body = h.handle(html)

    # some feed items have really long titles, so better truncate them
    filename = FEED.entries[i].title[:59]
    date, time = current_date_time()
    posted = "%s-%s" % (date, time)    

    # it's just text, but a nice layout certainly isn't bad, so construct it
    u_line = u"┏" + 78 * u"━"             + u"┓\n"
    ufill = 76 - len(FEED.feed.title[:53] + FEED.feed.link)
    header = u"┃ " + FEED.feed.title[:53] + ufill * " " + FEED.feed.link  + u" ┃\n"
    m_line = u"┣" +  59 *u"━" + u"┳" + 18* u"━" + u"┫\n"
    bfill = 74 - (len(FEED.entries[i].title[:53] + " ... " ) + len(posted))
    subline = u"┃ " + FEED.entries[i].title[:53] + " ... " + bfill * " " + u"┃ " + posted + u" ┃\n"    
    b_line = u"┗" + 59 * u"━" + u"┻" + 18 * u"━" + u"┛\n\n"
    title = FEED.entries[i].title + "\n\n"
    pre_links = "\n" + 80 * u"━" + "\nLinks:\n[*] " + FEED.entries[i].link
    
    product = u_line + header + m_line + subline + b_line + title + body + pre_links

    # finally, write out the finished product
    fh = open(FEED_DIR + "/" + "[" + date +"]-[" + time + "]" + " " + filename, "w")
    fh.write(product)
    fh.close()
    
