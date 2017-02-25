#!/usr/bin/env python3
# encoding: utf-8

"""
Run hnrss generator on HackerNews "New" feed, with some simple logging.

[It turns out this is not a very interesting feed, normally]

Note that hnrss attempts to create an automated summary of the linked websites.
On atypical websites, this process can sometimes hang. So it is best practice
to run this with a time and memory management tool.

I currently use and recommend https://github.com/pshved/timeout
"""

from hnrss import *

import logging

LOG_FILENAME = 'logs/hnrss.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    format="%(asctime)s :: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")


logging.info("Beginning to perform RSS creation...")
HN_NEW = HNrss(HN_NEW_URL, title="Unofficial HackerNews new-post RSS")

logging.debug("Creating NEW RSS feed...")
try:
    HN_NEW.generate_feed()
    with open("newrss.html", "w") as newfile:
        newfile.write(HN_NEW.feed.get_xml())
except Exception as e:
    logging.exception("Error occurred while creating NEW feed.")

logging.info("Ending RSS creation.")
