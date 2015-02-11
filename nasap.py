#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""nasap - news as simple as possible

This is a simple tool to fetch full text posts based on a RSS/Atom feed and
store it as a simple textfile to later view it with a tool of your choice.

git repo: https://github.com/phavx/nasap/

Information about AUTHORS, TODO and LICENSE can be found in the respective file
"""

# standard libs
from io      import open
from os      import environ, makedirs, path
from urllib2 import urlopen
from sys     import argv, exit
from time    import gmtime, strftime

# external dependencies
import feedparser
import html2text
from   readability.readability import Document

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

def s_title(title):
    """replace '/' in the title to circumvent unix file path problems"""
    if "/" in title:
        return "_".join(title.split("/"))
    else:
        return title

def mkheader(feedtitle, feedlink, itemtitle, itemlink, date, time):
    """builds a nice looking header consiting of some box drawing and infos"""
    ft, fl, it, il, d ,t = feedtitle, feedlink, itemtitle, itemlink, date, time
    
    # calculate how much spacing we need so we can fill the lines nicely
    f_1 = " " * ( 76 - (len(ft[:53] + fl)) )
    f_2 = " " * ( 73 - (len(it[:53] + "..." + d + "-" + t) ) )
    
    # building a five line header, two for content, three for style
    return u"┏━" + 76 * u"━"                                       + u"━┓\n" \
         + u"┃ " + ft[:53]           + f_1 + fl                    + u" ┃\n" \
         + u"┣━" + 57 * u"━"               + u"┳"  + 18 * u"━"     + u"━┫\n" \
         + u"┃ " + it[:53]   + "..." + f_2 + u"┃ " +  d + " @" + t + u" ┃\n" \
         + u"┗━" + 57 * u"━"               + u"┻"  + 18 * u"━"     + u"━┛\n\n"

def mkfooter(itemlink):
    """adds footer containing link to the original source plus content links"""
    return "\n" + 80 * u"━" + "\nLinks:\n[*] " + itemlink

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

# list of links we've already seen so we can skip them
SEEN_FILE = FEED_DIR + "/.seen.links"
if path.exists(SEEN_FILE):
    if not path.isfile(SEEN_FILE):
        error("Error: %s needs to be a file." % SEEN_FILE, 1)
else:
    open(SEEN_FILE, 'a').close()
    
# loop over the feed's items and process them
for i in range(0, len(FEED["entries"])):
    # if we already processed the link earlier, skip processing it
    seen_links = open(SEEN_FILE).read()
    if FEED.entries[i].link in seen_links:
        continue
    
    html = Document(urlopen(FEED.entries[i].link).read()).summary()

    # stripping html tags and limiting the width to 80 characters
    h = html2text.HTML2Text(bodywidth=80)
    h.ignore_images = True
    body = h.handle(html)

    date, time = current_date_time()
    # some feed items have really long titles, so better truncate them
    filename = "[%s]-[%s] " + s_title(FEED.entries[i].title[:59]) % (date, time)

    # build the final product, a nice header, the content and enclosed links    
    product = mkheader(FEED.feed.title, FEED.feed.link, FEED.entries[i].title, \
                  FEED.entries[i].link, date, time) \
            + body \
            + mkfooter(FEED.entries[i].link)

    # finally, write out the finished product and store the link as already seen
    fh = open(FEED_DIR + "/" + filename, "w")
    fh.write(product)
    fh.close()
    
    sh = open(SEEN_FILE, 'a')
    sh.write(FEED.entries[i].link + "\n")
    sh.close()
    
